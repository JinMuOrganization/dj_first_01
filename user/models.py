import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_books'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle



class Profile(AbstractUser):
    """
    用户信息
    """
    USER_STATUS = (
        (0, "可用"),
        (1, "不可用"),
    )
    phone = models.CharField(verbose_name='手机号', help_text='手机号', max_length=20, blank=True, null=True)
    create = models.DateTimeField(verbose_name='创建时间', help_text='创建时间', default=datetime.datetime.now)
    user_status = models.IntegerField(verbose_name='人员状态', choices=USER_STATUS, help_text='人员状态', default=0)
    token = models.CharField(verbose_name='token', help_text='token', max_length=500, default='')
    pwd_uptime = models.DateTimeField(verbose_name='密码修改时间', default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.phone