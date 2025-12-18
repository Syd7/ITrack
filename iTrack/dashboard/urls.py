"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import dashboard_View, createJob_View, createCompany_View, createScrapedJob_View, scraped_jobsView, add_jobView

app_name = "dashboard"

urlpatterns = [
    path('dashboard/', dashboard_View, name='dashboard'),
    path('dashboard/createJob', createJob_View, name='createJob'),
    path('dashboard/createCompany', createCompany_View, name='createCompany_View'),
    path('dashboard/createScrapedJob', createScrapedJob_View, name='createScrapedJob_View'),
    path("scraped-jobs/", scraped_jobsView, name="scraped_jobs"),
    path("jobs/add/<int:scraped_job_id>/", add_jobView, name="add_job"),
]