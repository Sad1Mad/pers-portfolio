from django.db import models


# Create your models here.
class Projects(models.Model):
    titleProject = models.CharField(max_length=50)
    descriptionProject = models.CharField(max_length=200)
    urlProject = models.URLField(blank=True)
    imageProject = models.ImageField(upload_to="portfolio/images")

