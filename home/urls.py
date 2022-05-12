from django.urls import path
from .views import HomePageView, JobDetailsView, JobCreatePage

app_name = "root"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("job_detail/<slug:job_slug>/", JobDetailsView.as_view(), name="job-details"),
    path("job_create/", JobCreatePage.as_view(), name="job-create"),
]
