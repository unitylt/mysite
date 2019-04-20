from django.db import models
from django.contrib.auth.models import User  # Django自带作者模块
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail


class BlogType(models.Model):
    '博客分类,对应blog_type'
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


# 初始化APP所需要的数据类型  涉及到数据库字段所以每次修改要同步数据库
class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)  # 创建标题类型字段并且最大长度不超过50
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()  # 内容 长文本
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 作者
    read_details = GenericRelation(ReadDetail)

    created_time = models.DateTimeField(auto_now_add=True)  # 创作时间
    last_updated_time = models.DateTimeField(auto_now_add=True)  # 修改时间







    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']  # 负号倒序 时间

'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)  # 阅读次数 默认为零
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)  # 一对一关系
'''