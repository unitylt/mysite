from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User  # 自带的admin管理

class Comment(models.Model):
    # 评论对象 可以对应任何类型字段
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)  # 外键关联
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')  # 这两个参数对应上面创建的

    # 评论内容
    text = models.TextField()  # textfield 可以不限制字数
    comment_time = models.DateTimeField(auto_now_add=True)  # ()创建这条记录自动添加时间
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 删除评论不影响用户数据

    class Meta:
        ordering = ['-comment_time']  # 评论按照时间倒序
