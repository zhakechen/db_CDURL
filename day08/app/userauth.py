# 定义一个用户验证类

from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication

from app.models import User
from utils.errors import ParamsException


class MyUserAuthentication(BaseAuthentication):

    def authenticate(self, request):

        token = request.query_params.get('token')
        if not token:
            raise ParamsException({'code':1007,'msg':'无法访问'})

        user_id = cache.get(token)
        if not user_id:
            raise ParamsException({'code':1008,'msg':'无法访问'})
        user = User.objects.get(pk=user_id)
        return user,token