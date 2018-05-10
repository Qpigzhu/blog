from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType
# Create your views here.

def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    context['type_name'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html',context)

def blog_datail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk = blog_pk)
    return render_to_response('blog/blog_detail.html',context)

def blogs_type(request,type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk = type_pk)
    context['blog_type'] = blog_type
    context['blogs'] = Blog.objects.filter(type_name = blog_type)
    context['type_name'] = BlogType.objects.all()
    return render_to_response('blog/blogs_type.html',context)