from django.urls import path

from app3.views import *


urlpatterns = [
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('index/',index,name='index'),
     # 使用token 进行登录校验
    path('my_login/',my_login,name='my_login'),
    # 使用session进行登录
    path('session_login/',session_login,name='session_login'),
    path('session_index/',session_index,name='session_index'),
    path('icon/',icon,name='icon')

]