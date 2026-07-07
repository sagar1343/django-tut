from django.shortcuts import render, redirect
from .models import Job
from django.http import HttpResponse

# Create your views here.


def home(request):
    jobs = Job.objects.all()
    return render(request, "index.html", {"jobs": jobs})


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
        return render(request, "addform.html")


def delete_job(request, id):
    if request.method == "POST":
        job = Job.objects.get(id=id)
        job.delete()
    return redirect("/")
