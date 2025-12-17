from django.contrib import admin
from .models import Company, ScrapedJob, Job


class CompanyAdmin(admin.ModelAdmin):
    model = Company


class ScrapedJobAdmin(admin.ModelAdmin):
    """Create admin for Article."""

    model = ScrapedJob

class JobAdmin(admin.ModelAdmin):
    model = Job


admin.site.register(Company, CompanyAdmin)
admin.site.register(ScrapedJob, ScrapedJobAdmin)
admin.site.register(Job, JobAdmin)