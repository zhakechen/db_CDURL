import re
from datetime import datetime

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

import logging

logger = logging.getLogger(__name__)

# 中间件的执行顺序，先执行process_request方法
# 第一个中间件先执行，依次往下，
# process_response 方法执行顺序，最后一个中间件先执行，第一个中间件追后执行


# 注意，process_request方法要么不写，return,或者return None
#        process_response方法一定要返回响应，return response
class Test1Middleware(MiddlewareMixin):
    def process_request(self,request):
        print('test1 process_request')

    def process_response(self,request,response):
        print('test1 process_request')
        return response


    def process_view(self,request,view_func,view_args,view_kwargs):
        print('test1 process_request')



class Test2Middleware(MiddlewareMixin):
    def process_request(self,request):
        print('test2 process_request')

    def process_response(self,request,response):
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('test2 process_request')


class LoginRequireMiddleware(MiddlewareMixin):

    def process_request(self,request):
        # 实现登录校验功能


        # 不需要做登录校验的地址
        not_need_login = ['/app3/login/','/app3/session_login/','/goods/*']
        path = request.path
        # 商城中商品地址，如/goods/1/  /goods/3/

        # if path in not_need_login:
        #     return None

        for not_path in not_need_login:
            if re.match(not_path,path):
                return None

        # 需要登录校验的地址才会执行以下代码
        user_id = request.session.get('user_id')
        if not user_id:
            # 没登录，就重定向
            return redirect(reverse('app3:session_login'))


class LoginMiddleware(MiddlewareMixin):

    def process_request(self,request):
        request.init_time = datetime.now()
        return None

    def process_response(self,request,response):

        try:
            # 日志要记录：响应状态码，报错信息，响应内容，请求地址，请求参数,请求时间
            content = response.content

            status_code = response.status_code

            path = request.path

            params = request.GET if len(request.GET.keys())\
                else request.POST

            count_time = datetime.now() - request.init_time

            info = f'{path} {params} {count_time} {status_code} {content}'
            # 使用logger接收日志信息
            logger.info(info)

        except Exception as e:

            logging.critical(e)
        return response
