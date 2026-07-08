from .models import Job


def site_name(request):
    jobcount = Job.objects.count()
    return {"website_name": "LakshyaIn", "job_count": jobcount}
