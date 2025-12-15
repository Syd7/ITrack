from django.contrib import admin
from .models import Company, Opening, Job


class CompanyAdmin(admin.ModelAdmin):

    model = Company


class OpeningAdmin(admin.ModelAdmin):
    """Create admin for Article."""

    model = Opening

class JobAdmin(admin.ModelAdmin):
    model = Job


admin.site.register(Company, CompanyAdmin)
admin.site.register(Opening, OpeningAdmin)
admin.site.register(Job, JobAdmin)