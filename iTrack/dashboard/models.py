
from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ["company_name"]

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
            return self.job_name
    
    
class Opening(models.Model):

    opening_name = models.CharField(max_length=255)
    job_name = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opening_name

    class Meta:
        ordering = ["-creation_date"]

