# 在执行函数之前插入一些额外代码
# 装饰器实现的步骤：
# 1.外层函数嵌套内层函数
# 2.外层函数返回内层函数
# 3.内层函数返回外层函数的参数
from functools import wraps

from django.shortcuts import redirect
from django.urls import reverse

from app3.models import User


def login_check(f):

    @wraps(f)
    def check(request,*args,**kwargs):
        # 登录才返回f(),没登录不反回(),而是重定向到登录地址

        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.get(id=user_id)
            request.user = user
            return f(request,*args,**kwargs)
        else:
            return redirect(reverse('app3:session_login'))

    return check