from django.urls import path
from . import views

urlpatterns = [
    # 称之为路由 所有的网址设置
    # http://localhost:8000/blog/1   ''之间就是具体URL
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name="blogs_with_date"),


]