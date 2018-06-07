
from django.urls import path
from  . import views

urlpatterns = [

    path('', views.allblogs, name="allblogs"),
    path('create/', views.create, name="create_blog"),
    path('<int:blog_id>/',views.details, name="blog_detail")
]
