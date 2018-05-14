from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from .models import Blog,BlogType
# Create your views here.

def blog_list(request):
    blogs_all_list = Blog.objects.all()
    paginator =Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER) #每页10篇
    page_num = request.GET.get('page',1) #获取Url的页面参数(GET请求)
    page_of_blogs = paginator.get_page(page_num) #获取当前页数的内容
    #获取当前页面前后各2页的页码范围
    current_page_num = page_of_blogs.number #获取当前页数
    page_range = list(range(max(current_page_num - 2,1),current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2 , paginator.num_pages)+1))
    # 加上省页面标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs']  = page_of_blogs
    context['page_range'] = page_range
    context['type_name'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html',context)

def blog_datail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk = blog_pk)
    return render_to_response('blog/blog_detail.html',context)

def blogs_type(request,type_pk):

    context = {}
    blog_type = get_object_or_404(BlogType,pk = type_pk)
    blogs_all_list = Blog.objects.filter(type_name = blog_type)
    paginator =Paginator(blogs_all_list,settings.EACH_PAGE_BLOGS_NUMBER) #每页10篇
    page_num = request.GET.get('page',1) #获取Url的页面参数(GET请求)
    page_of_blogs = paginator.get_page(page_num) #获取当前页数的内容

    #获取当前页面前后各2页的页码范围
    current_page_num = page_of_blogs.number #获取当前页数
    page_range = list(range(max(current_page_num - 2,1),current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2 , paginator.num_pages)+1))
    # 加上省页面标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0,'...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0,1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_type'] = blog_type
    context['type_name'] = BlogType.objects.all()
    return render_to_response('blog/blogs_type.html',context)