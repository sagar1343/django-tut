from django.urls import path
from .views import home, create_job, delete_job

urlpatterns = [
    path("", home, name="home"),
    path("jobs/", create_job, name="create-job"),
    path("jobs/<int:id>/delete", delete_job, name="delete-job"),
]
