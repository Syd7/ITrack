from django.core.management.base import BaseCommand
from jobspy import scrape_jobs
from dashboard.models import ScrapedJob, Company
import pandas as pd
import os

class Command(BaseCommand):
    help = "Scrape jobs using python-jobspy and export to Excel"

    def handle(self, *args, **kwargs):
        self.stdout.write("Scraping jobs using python-jobspy...")

        # ------------------------
        # Scrape jobs
        # ------------------------
        jobs = scrape_jobs(
            site_name=["indeed", "google", "zip_recruiter", "glassdoor"],
            search_term="Tech Intern",
            location="Philippines",
            results_wanted=50,
            hours_old=72,
            country_indeed="Philippines"
        )

        if jobs.empty:
            self.stdout.write(self.style.WARNING("No jobs found!"))
            return

        # Normalize columns
        jobs.columns = jobs.columns.str.upper()

        # ------------------------
        # Save to Excel
        # ------------------------
        excel_path = os.path.join(os.getcwd(), "scraped_jobs.xlsx")
        try:
            jobs.to_excel(excel_path, index=False)
            self.stdout.write(self.style.SUCCESS(f"Jobs exported to {excel_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to export Excel: {e}"))

        # ------------------------
        # Save to Django models
        # ------------------------
        created_count = 0
        for _, row in jobs.iterrows():
            company_name = row.get("COMPANY", "Unknown Company")
            title = row.get("TITLE", "No Title")
            link = row.get("JOB_URL", "")
            source = row.get("SITE", "Unknown")

            if not link:
                continue

            company, _ = Company.objects.get_or_create(
                company_name=company_name, defaults={"description": ""}
            )

            job_obj, created = ScrapedJob.objects.get_or_create(
                link=link,
                defaults={
                    "title": title,
                    "company": company,
                    "source": source
                }
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"Scraped and saved {created_count} new jobs to DB")
        )
