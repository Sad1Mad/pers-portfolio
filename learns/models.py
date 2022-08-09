from django.db import models

class Learn(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    titleLearn = models.CharField(max_length=50)
    descriptionLearn = models.CharField(max_length=50)
    postLearn = models.CharField(max_length=500)
    dataLearn = models.DateTimeField(auto_now_add=True)