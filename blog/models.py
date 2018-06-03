from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/blog/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
