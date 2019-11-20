from django.conf.urls import url
from django.urls import path

from appin.views import *

urlpatterns = [
    path('index/',index),
    # 127.0.0.1/appin/paramsl/1000/
    # 表达式:<类型:参数名>
    path('params1/<int:id>/',params1,name='p1'),
    # 127.0.0.1/appin/paramsl/dddsa/
    path('params2/<str:name>/',params2),
    # 传多个参数
    path('params3/<int:id>/<int:id2>/',params3,name='p3'),
    #
    path('params4/<uuid:uid>/',params4),
    path('params5/<str:year>/<str:month>/<str:day>/',
         Params5.as_view(),name='p5'),
    # django2.0以下写法
    url('params6/(\d+)(\d+)',params6,name='p6'),
    url('params7/(?P<name1>\d+)/(?P<name2>\w+)',params7),


    # 先访问注册地址，实现注册功能后跳转到登录页面
    # 登录功能实现后，跳转到首页页面
    path('register/',register)

    ]