from django.urls import path
from .views import blog_datail,blog_list,blogs_type,blog_date
urlpatterns = [
    path('',blog_list,name='blog_list'),
    path('<int:blog_pk>',blog_datail,name = 'blog_datail'),
    path('type/<int:type_pk>',blogs_type,name = 'blogs_type'),
    path('date/<int:year>/<int:month>',blog_date,name = 'blog_date'),
]