from django.shortcuts import render
from .models import ScrapedJob 
from django.contrib.auth.decorators import login_required
from .forms import Job_Form, ScrapedJobForm, CompanyForm


# Create your views here.
@login_required
def dashboard_View(request):
    openings = ScrapedJob.objects.all()  
    return render(request, 'dashboard/dashboard.html', {'openings': openings})

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