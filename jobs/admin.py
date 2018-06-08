from django.contrib import admin

from .models import Job
# Register your models here.

class jobsInfoAdmin(admin.ModelAdmin):
    list_display = ('summary','image')



admin.site.register(Job,jobsInfoAdmin)
