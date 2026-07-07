from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    company_name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    logo = models.ImageField(upload_to="logo")

    def __str__(self):
        return f"{self.company_name} - {self.title}"
