from django.contrib import admin


from .models import Blog
# Register your models here.

class blogInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_summary', 'pub_date')

    def body_summary(self,obj):
        return obj.body[:50] + "..."

admin.site.register(Blog, blogInfoAdmin)
