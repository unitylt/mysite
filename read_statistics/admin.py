from django.contrib import admin
from .models import ReadNum, ReadDetail


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):  # 后台要显示的代码   初始化的数据显示在admin中要逐个添加
    list_display = ('read_num', 'content_object')


@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):  # 后台要显示的代码   初始化的数据显示在admin中要逐个添加
    list_display = ('date', 'read_num',  'content_object')

