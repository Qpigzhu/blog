import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum,ReadDetail


def read_statistics_once_read(request,obj):
    """

    控制层阅读计数函数，返回一个cookie_key
    """
    ct = ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read'%(ct,obj.pk)
    if not request.COOKIES.get(key):
        readnum,created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        date = timezone.now().date()
        readDetail,created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk,date=date)
        readDetail.read_num += 1
        readDetail.save()
        return key

def get_seven_read_day(content_type):
    today = timezone.now().date()
    read_nums = []
    dates = []
    for i in range(7,0,-1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type,date=date)
        result = read_details.aggregate(read_num_sum = Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    print(read_nums)
    return dates,read_nums

def get_hot_blog_today(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type,date=today).order_by('-read_num')
    return read_details[:7]


def get_hot_blog_yesterday(content_type):
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(content_type=content_type,date=yesterday).order_by('-read_num')
    return read_details[:7]

