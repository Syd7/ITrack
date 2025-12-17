
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ["company_name"]

class Job(models.Model):
    STATUS_CHOICES = [
        ("interested", "Interested"),
        ("applied", "Applied"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    link = models.URLField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="interested"
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} @ {self.company}"

    class Meta:
        ordering = ["-created_at"]

class ScrapedJob(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    link = models.URLField(unique=True)
    source = models.CharField(max_length=50)
    date_scraped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} @ {self.company}"

    class Meta:
        ordering = ["-date_scraped"]

