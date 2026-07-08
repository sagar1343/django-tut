from django.shortcuts import render, redirect
from .models import Job

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
        return render(request, "jobform.html")


def delete_job(request, id):
    if request.method == "POST":
        job = Job.objects.get(id=id)
        job.delete()
    return redirect("/")


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
