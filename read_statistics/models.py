from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.fields import exceptions
from django.utils import timezone

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)  # 阅读数量默认为零
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

# 如果找到对应的数据就返回(阅读量),没有找到就默认0
class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0

# 记录更详细的阅读数量 加入每天统计
class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now) # 定义日期统计字段 默认为当前时间--需导入相应模块
    read_num = models.IntegerField(default=0)    # 阅读次数 默认为零
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')  # 这两个参数对应上面创建的
