from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,ReadDetail
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length= 10)
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    type_name = models.ForeignKey(BlogType,on_delete = models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    read_datails = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add = True)
    last_update_time =models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']


