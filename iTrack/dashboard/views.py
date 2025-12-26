from django.shortcuts import render, get_object_or_404
from .models import ScrapedJob, Job
from django.contrib.auth.decorators import login_required
from .forms import Job_Form, ScrapedJobForm, CompanyForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse




# Create your views here.
@login_required
def dashboard_View(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, "dashboard/dashboard.html", {"jobs": jobs})

@login_required
def createJob_View(request):
    if request.method == 'POST':
        form = Job_Form(request.POST)
        if form.is_valid():
            schedule = form.save()
    else:
        form = Job_Form()

    return render(request, 'dashboard/createJob.html', {
        'form': form
    })   

@login_required
def createCompany_View(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            schedule = form.save()
    else:
        form = CompanyForm()

    return render(request, 'dashboard/createCompany.html', {
        'form': form
    })   

@login_required
def createScrapedJob_View(request):
    if request.method == 'POST':
        form = ScrapedJobForm(request.POST)
        if form.is_valid():
            schedule = form.save()
    else:
        form = ScrapedJobForm()

    return render(request, 'dashboard/createScrapedJob.html', {
        'form': form
    })   



@login_required
def add_jobView(request, scraped_job_id):
    scraped_job = get_object_or_404(ScrapedJob, id=scraped_job_id)

    Job.objects.get_or_create(
        user=request.user,
        scraped_job=scraped_job,
        defaults={
        "title": scraped_job.title,
        "company": scraped_job.company,
        "link": scraped_job.link,
        "source": scraped_job.source,
        "status": "interested",
    },
    )

    return redirect("dashboard:dashboard")

@login_required
def scraped_jobsView(request):
    query = request.GET.get("q", "") 
    if query:
        jobs = ScrapedJob.objects.filter(title__icontains=query)
    else:
        jobs = ScrapedJob.objects.all()
    
    return render(request, "dashboard/scraped_jobs.html", {
        "scraped_jobs": jobs,
        "query": query 
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  
        else:
            error = "Invalid username or password"
            return render(request, "registration/login.html", {"error": error})

    return render(request, "registration/login.html")

@login_required
def update_job_status(request, job_id):
    job = get_object_or_404(Job, id=job_id, user=request.user)

    new_status = request.POST.get("status")
    if new_status in dict(Job.STATUS_CHOICES):
        job.status = new_status
        job.save()

    return HttpResponse(status=204)