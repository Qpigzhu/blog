from django import template
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from comment.forms import CommentForm


#创建模板对象
register = template.Library()


#注册函数
@register.simple_tag
def get_comment_count(obj):
	blog_content_type = ContentType.objects.get_for_model(obj)
	return Comment.objects.filter(content_type=blog_content_type,object_id=obj.pk).count()


	
@register.simple_tag
def get_comment_form(obj):
	blog_content_type = ContentType.objects.get_for_model(obj)
	form = CommentForm(initial={'content_type':blog_content_type.model,'object_id':obj.pk,'reply_comment_id':0})
	return form