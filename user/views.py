from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.exceptions import logger_user
from . import models
from .serializers import BookInfoSerializer
from .models import BookInfo

# Create your views here.
class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = models.Profile.objects.get(username=username)
            print('username='+username+'    password='+password)
            if user.check_password(password) and user.is_active:
                # payload = jwt_payload_handler(user)
                # token = jwt_encode_handler(payload)
                # models.Profile.objects.filter(user_code=user.user_code).update(token=token)
                # user.token = token
                return user
            else:
                return None
                # return '密码错误！'
        except Exception as e:
            print(e)
            return None
            # return '账号不存在'

def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    logger_user.info("user的问题")
    return HttpResponse("hello the world!")



class BookInfoViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer