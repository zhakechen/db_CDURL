# 定义一个异常类

from rest_framework.exceptions import APIException

class ParamsException(APIException):

    def __init__(self, msg):

        self.detail= msg

