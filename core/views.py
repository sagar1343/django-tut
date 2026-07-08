from django.shortcuts import render, redirect
from .models import Job
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    jobs = Job.objects.all()
    return render(request, "index.html", {"jobs": jobs})


@login_required
def create_job(request):
    if request.method == "POST":
        Job.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            company_name=request.POST.get("company_name"),
            location=request.POST.get("location"),
            salary=request.POST.get("salary"),
            logo=request.FILES.get("logo"),
        )
        return redirect("/")
    else:
        return render(request, "jobform.html")


@login_required
def delete_job(request, id):
    if request.method == "POST":
        job = Job.objects.get(id=id)
        job.delete()
    return redirect("/")


@login_required
def update_job(request, id):
    job = Job.objects.get(id=id)
    if request.method == "POST":
        job.title = request.POST.get("title")
        job.description = request.POST.get("description")
        job.salary = request.POST.get("salary")
        job.company_name = request.POST.get("company_name")
        job.location = request.POST.get("location")

        if request.FILES.get("logo"):
            job.logo = request.FILES.get("logo")
        job.save()
        return redirect("/")

    return render(request, "jobform.html", {"job": job})


def register_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        exist = User.objects.filter(username=username).exists()
        if exist:
            messages.warning(
                request=request, message="Already registered user, please try login"
            )
            return redirect("/login")
        password = request.POST.get("password")
        User.objects.create_user(username=username, password=password)
        messages.success(request=request, message="registration successfull")
        return redirect("/login")
    return render(request, "registration.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()
        if not user:
            messages.error(request=request, message="user not registered")
            return redirect("/register")

        authenticated_user = authenticate(request, username=username, password=password)
        if not authenticated_user:
            messages.error(request=request, message="invalid username or password")
            return redirect("/login")

        login(request=request, user=authenticated_user)
        messages.success(
            request=request, message=f"Welcome back {request.user.username}"
        )
        return redirect("/")
    return render(request, "login.html")


def logout_user(request):
    logout(request=request)
    messages.success(request=request, message="Logout Succesfull")
    return redirect("/login")
