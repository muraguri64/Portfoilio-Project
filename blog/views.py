from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from .models import Blog


# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html',{'blogs':blogs})

def details(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detail_blog})

@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            blog = Blog()
            blog.title    = request.POST['title']
            blog.image    = request.FILES['image']
            blog.body     = request.POST['body']
            blog.pub_date = timezone.datetime.now()

            blog.save()
            return redirect('allblogs')
        else:
             return render(request,'blog/create.html',{'error':'All fields are required'})

    else:
        return render(request,'blog/create.html')
