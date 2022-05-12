from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from job.models import Job
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from job.forms import JobForms
from job.mixin import CheckUserMixins
from account.models import Profiles
from apply.models import Apply
from apply.forms import ApplyForm

# Create your views here.


class HomePageView(ListView):
    template_name = "home/index.html"
    context_object_name = "jobs"
    model = Job


class JobDetailsView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = "home/details.html"
    context_object_name = "job"
    slug_url_kwarg = "job_slug"
    form_class = ApplyForm
    success_url = reverse_lazy("root:home")

    def get_context_data(self, **kwargs):

        job_slug = self.kwargs.get("job_slug" or None)
        context = super().get_context_data(**kwargs)
        context["job"] = get_object_or_404(Job, slug=job_slug)

        return context

    def form_valid(self, form):

        user = get_object_or_404(Profiles, email=self.request.user.email)
        job = get_object_or_404(Job, slug=self.kwargs.get("job_slug"))

        setField = form.save(commit=False)
        setField.apply_job = job
        setField.apply_applicant = user
        setField.save()
        return super(JobDetailsView, self).form_valid(form)


class JobCreatePage(CheckUserMixins, CreateView):
    template_name = "home/jobcreate.html"
    model = Job
    form_class = JobForms
    success_url = reverse_lazy("root:home")

    def form_valid(self, form):
        # user=get_object_or_404(email)
        setUser = form.save(commit=False)
        setUser.job_company = self.request.user
        setUser.save()
        return super(JobCreatePage, self).form_valid(form)
