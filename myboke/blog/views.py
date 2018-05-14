from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from .models import Blog,BlogType
# Create your views here.

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator =Paginator(blogs_all_list,10) #每页10篇
    page_num = request.GET.get('page',1) #获取Url的页面参数(GET请求)
    page_of_blogs = paginator.get_page(page_num) #获取当前页数的内容


    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs']  = page_of_blogs
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
    context['type_name'] = BlogType.objects.all()
    blogs_all_list = Blog.objects.filter(type_name = blog_type)
    paginator =Paginator(blogs_all_list,10) #每页10篇
    page_num = request.GET.get('page',1) #获取Url的页面参数(GET请求)
    page_of_blogs = paginator.get_page(page_num) #获取当前页数的内容
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs

    return render_to_response('blog/blogs_type.html',context)