from django.contrib import admin
from .models import BlogType, Blog


@admin.register(BlogType)  # 装饰器的作用大概是注册吧  下同
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):  # 后台要显示的代码   初始化的数据显示在admin中要逐个添加
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'last_updated_time')

'''
@admin.register(ReadNum)  # 装饰器的作用大概是注册吧  下同
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')
'''