from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from dashboard.models import ScrapedJob, Company


class Command(BaseCommand):
    help = "Scrape jobs from python.org"

    def handle(self, *args, **kwargs):
        url = "https://www.python.org/jobs/"
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        jobs = soup.select("ol.list-recent-jobs li")

        created_count = 0

        for job in jobs:
            title_el = job.select_one("h2 a")
            company_el = job.select_one(".listing-company-name")
            link_el = job.select_one("h2 a")

            if not title_el or not company_el or not link_el:
                continue

            title = title_el.text.strip()
            company_name = company_el.text.replace("Company:", "").strip()
            link = "https://www.python.org/" + link_el["href"]

            raw_company = company_name
            if raw_company.startswith("New "):
                raw_company = raw_company[4:].strip()

            if raw_company.startswith(title):
                company_name = raw_company[len(title):].strip(" —-")
            else:
                company_name = rawcompany

            company,  = Company.objects.get_or_create(
                company_name=company_name,
                defaults={"description": ""}
            )

            job_obj, created = ScrapedJob.objects.get_or_create(
                link=link,
                defaults={
                    "title": title,
                    "company": company,
                    "source": "python.org"
                },
            )

            if created:
                created_count += 1


        self.stdout.write(
            self.style.SUCCESS(f"Scraped {created_count} new jobs")
        )