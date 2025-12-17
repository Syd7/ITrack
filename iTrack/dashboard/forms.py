from django import forms
from .models import Job, Company, ScrapedJob


class Job_Form(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'company', 'link', 'status', 'notes']    


class CompanyForm(forms.ModelForm):
    """Creates a form to add activity_name"""

    class Meta:
        """Create fields for the form and link ArticleImage model."""

        model = Company
        fields = ['company_name', 'decription']
class ScrapedJobForm(forms.ModelForm):
    class Meta:
        model = ScrapedJob
        fields = ['title', 'link', 'source']

