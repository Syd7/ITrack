from django import forms
from .models import Job, Company, ScrapedJob


class Job_Form(forms.ModelForm):

    class Meta:
        model = Job
        fields = ['title', 'company', 'link', 'status', 'notes']    
        widgets = {
            "title": forms.TextInput(attrs={
                "class": (
                    "w-full h-12 rounded-lg "
                    "bg-gray-50 dark:bg-[#101922] "
                    "border-gray-200 dark:border-[#324d67] "
                    "text-slate-900 dark:text-white text-base px-4 "
                    "focus:ring-2 focus:ring-primary/20 "
                    "focus:border-primary "
                    "placeholder:text-slate-400 dark:placeholder:text-slate-600 "
                    "transition-all"
                ),
                "placeholder": "e.g. Software Engineer Intern",
                "required": True,
            }),
            "company": forms.Select(attrs={
                "class": (
                    "w-full h-12 rounded-lg "
                    "bg-gray-50 dark:bg-[#101922] "
                    "border-gray-200 dark:border-[#324d67] "
                    "text-slate-900 dark:text-white text-base px-4 "
                    "focus:ring-2 focus:ring-primary/20 "
                    "focus:border-primary "
                    "placeholder:text-slate-400 dark:placeholder:text-slate-600 "
                    "transition-all"
                ),
                "placeholder": "e.g. Google",
                "required": False,
            }),
            "link": forms.TextInput(attrs={
                "class": (
                    "w-full h-12 rounded-lg bg-gray-50 dark:bg-[#101922] border-gray-200 dark:border-[#324d67] text-slate-900 dark:text-white text-base pl-4 pr-10 focus:ring-2 focus:ring-primary/20 focus:border-primary placeholder:text-slate-400 dark:placeholder:text-slate-600 transition-all"
                ),
                "placeholder": "e.g. linkedin.com/jobs/...",
                "required": True,
            }),
            "status": forms.Select(attrs={
                "class": (
                    "w-full h-12 rounded-lg "
                    "bg-gray-50 dark:bg-[#101922] "
                    "border-gray-200 dark:border-[#324d67] "
                    "text-slate-900 dark:text-white text-base "
                    "pl-4 pr-10 "
                    "focus:ring-2 focus:ring-primary/20 "
                    "focus:border-primary "
                    "appearance-none transition-all cursor-pointer"
                ),
            }),
           "notes": forms.Textarea(attrs={
                "class": (
                    "w-full min-h-[160px] rounded-lg "
                    "bg-gray-50 dark:bg-[#101922] "
                    "border border-gray-200 dark:border-[#324d67] "
                    "text-slate-900 dark:text-white text-base p-4 "
                    "focus:ring-2 focus:ring-primary/20 focus:border-primary "
                    "placeholder:text-slate-400 dark:placeholder:text-slate-600 "
                    "transition-all resize-y"
                ),
                "placeholder": (
                    "Paste the job description here or add your own notes "
                    "about the role, salary range, or specific requirements..."
                ),
            }),


        }


class CompanyForm(forms.ModelForm):
    """Creates a form to add activity_name"""

    class Meta:
        """Create fields for the form and link ArticleImage model."""

        model = Company
        fields = ['company_name', 'description']

class ScrapedJobForm(forms.ModelForm):
    class Meta:
        model = ScrapedJob
        fields = ['title', 'company', 'link', 'source']

