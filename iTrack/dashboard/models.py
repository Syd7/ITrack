
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ["company_name"]

class ScrapedJob(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField(unique=True)
    source = models.CharField(max_length=50)
    date_scraped = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"{self.title} @ {self.company}"

    class Meta:
        ordering = ["-date_scraped"]

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ("applied", "Applied"),
        ("rejected", "Rejected"),
        ("offer", "Offer Received"),
        ("interview", "Interview Scheduled"),
        ("interested", "Marked Interested"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey("Job", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class Job(models.Model):
    STATUS_CHOICES = [
        ("interested", "Interested"),
        ("applied", "Applied"),
        ("rejected", "Rejected"),
        ("offer", "Offer"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField()
    scraped_job = models.ForeignKey(ScrapedJob, on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="interested"
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        creating = self.pk is None

        old_status = None
        if not creating:
            old_status = (
                Job.objects
                .filter(pk=self.pk)
                .values_list("status", flat=True)
                .first()
            )

        super().save(*args, **kwargs)

        if creating or old_status != self.status:
            Activity.objects.create(
                user=self.user,
                job=self,
                type=self.status
            )

    def __str__(self):
        return f"{self.title} @ {self.company}"

    class Meta:
        ordering = ["-created_at"]
