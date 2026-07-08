from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("jobs/", views.create_job, name="create-job"),
    path("jobs/<int:id>/delete", views.delete_job, name="delete-job"),
    path("jobs/<int:id>/updates", views.update_job, name="update-job"),
    path("register/", views.register_user, name="register-user"),
    path("login/", views.login_user, name="login-user"),
    path("logout/", views.logout_user, name="logout-user"),
]
