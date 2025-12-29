"""Direct users to appropriate urls depending on needs."""
from django.urls import path
from .views import createJob_View, createCompany_View, createScrapedJob_View, scraped_jobsView, add_jobView, login_view, update_job_status, myJobs_View, dashboard_View

app_name = "dashboard"

urlpatterns = [
    path('dashboard/myJobs', myJobs_View, name='myJobs'),
    path('dashboard', dashboard_View, name='dashboard'),
    path('dashboard/createJob', createJob_View, name='createJob'),
    path('dashboard/createCompany', createCompany_View, name='createCompany_View'),
    path('dashboard/createScrapedJob', createScrapedJob_View, name='createScrapedJob_View'),
    path("scraped-jobs/", scraped_jobsView, name="scraped_jobs"),
    path("jobs/add/<int:scraped_job_id>/", add_jobView, name="add_job"),
    path("login/", login_view, name="login"),
    path("job/<int:job_id>/status/",update_job_status,name="update_job_status"),
]