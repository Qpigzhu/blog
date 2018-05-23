import datetime
from django.utils import timezone
from django.shortcuts import render,redirect
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db.models import Sum
from django.contrib import auth
from django.urls import  reverse #反向解释页面
from read_statistics.utils import get_seven_read_day,get_hot_blog_today,get_hot_blog_yesterday
from blog.models import Blog


def get_7_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
                .filter(read_datails__date__lt=date,read_datails__date__gte=date) \
                .values('id','title') \
                .annotate(read_num_sum = Sum('read_datails__read_num')) \
                .order_by('-read_num_sum')
    return blogs[:7]


def home_datil(request):
    #获取类型
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates,read_nums = get_seven_read_day(blog_content_type)

    #7天热门博客缓存
    get_7_hot_blogs_vlaue = cache.get('get_7_hot_blogs')
    if get_7_hot_blogs is None:
        get_7_hot_blogs_vlaue = get_7_hot_blogs()
        cache.set('get_7_hot_blogs',get_7_hot_blogs_vlaue,3600)

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['hot_blog_today'] = get_hot_blog_today(blog_content_type)
    context['hot_blog_yesterday'] = get_hot_blog_yesterday(blog_content_type)
    context['hot_blog_for_7_days'] = get_7_hot_blogs_vlaue
    return render(request,'home.html',context)

def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password', '')
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER',reverse('home'))    #获取请求头
    if user is not None:
        auth.login(request, user)
        return redirect(referer)
    else:
        return render(request,'error.html',{'massage':'用户名或密码不正确'})