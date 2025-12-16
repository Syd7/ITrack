from django.shortcuts import render
from .models import Opening 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard_View(request):
    openings = Opening.objects.all()  
    
    return render(request, 'dashboard/dashboard.html', {'openings': openings})