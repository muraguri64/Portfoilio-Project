from django.contrib import admin


from .models import Blog
# Register your models here.

class blogInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'body_summary', 'pub_date')

    def body_summary(self,obj):
        return obj.body[:50] + "..."

    body_summary.short_description = 'Summary'
admin.site.register(Blog, blogInfoAdmin)
