from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/blog/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def summary(self):
        sum = self.body[:50] + "..."
        return sum

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
