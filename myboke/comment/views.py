from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render,redirect
from django.urls import  reverse
from .models import Comment
# Create your views here.

def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    user = request.user
    #数据检查
    if not request.user.is_authenticated:
        return render(request,'error.html',{'massage':'用户未登录','redirect_to':reverse})
    text = request.POST.get('text','').strip()
    if text == '':
        return render(request, 'error.html', {'massage': '评论内容为空','redirect_to':reverse})
    try:
        content_type = request.POST.get('content_type','')
        object_id = int(request.POST.get('object_id',''))
        model_class = ContentType.objects.get(model = content_type).model_class() #获取具体的对象
        model_obj = model_class.objects.get(pk=object_id)
    except Exception as e:
        return render(request, 'error.html', {'massage': '评论对象不存在','redirect_to':reverse})

    #检查通过，保存数据
    comment = Comment()
    comment.user = user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)
