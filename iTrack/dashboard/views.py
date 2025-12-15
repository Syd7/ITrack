from django.shortcuts import render
from .models import Opening  # make sure Opening is imported


# Create your views here.
def dashboard_View(request):
    openings = Opening.objects.all()  # get all openings
    return render(request, 'dashboard/dashboard.html', {'openings': openings})