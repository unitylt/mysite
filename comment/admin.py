from django.contrib import admin
from .models import Comment


@admin.register(Comment)  # 注册对应的模型
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'text', 'comment_time', 'user')