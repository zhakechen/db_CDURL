from django import forms
from django.contrib.auth.hashers import check_password

from app3.models import User


class UserRegisterForm(forms.Form):
    # 定义需要校验你的字段（required=True 必填字段）
    name = forms.CharField(required=True,
                           max_length=10,
                           min_length=3,
                           error_messages={
                               'required':'账号必填',
                               'max_length':'账号长度必须小于10',
                               'min_length': '账号长度必须大于3',
                           })

    pwd = forms.CharField(required=True,min_length=3,max_length=10,
                          error_messages={'required':'请填写密码',
                                          'max_length': '账号长度必须小于10',
                                          'min_length': '账号长度必须大于3',})

    pwd1 = forms.CharField(required=True,min_length=3,max_length=10,
                          error_messages={'required':'请填写密码',
                                          'max_length': '账号长度必须小于10',
                                          'min_length': '账号长度必须大于3',})

    def clean(self):
        # 用于校验提交方法的所有字段
        name = self.cleaned_data.get('name')
        # 1.判断账号是否存在，如果存在，给提示信息
        if User.objects.filter(username=name).exists():
            raise forms.ValidationError({'name':'账号已存在，请更换注册账号'})
        # 2.判断密码和确认密码是否正确
        pwd = self.cleaned_data.get('pwd')
        pwd1 = self.cleaned_data.get('pwd1')
        if pwd != pwd1:
            raise forms.ValidationError({'pwd':'密码不一致'})
        return self.cleaned_data

    # def clean_name(self):
    #     # clean_field()只校验一个字段
    #     name = self.cleaned_data.get('name')
    #     if User.objects.filter(username=name).exists():
    #         raise forms.ValidationError('账号已经存在')
    #
    #
    #     return self.cleaned_data.get('name')


class UserLoginForm(forms.Form):
    # 定义需要校验你的字段（required=True 必填字段）
    name = forms.CharField(required=True,
                           max_length=10,
                           min_length=3,
                           error_messages={
                               'required':'账号必填',
                               'max_length':'账号长度必须小于10',
                               'min_length': '账号长度必须大于3',
                           })

    pwd = forms.CharField(required=True,min_length=3,max_length=10,
                          error_messages={'required':'请填写密码',
                                          'max_length':'密码长度必须小于10',
                                          'min_length':'密码长度必须大于3',})


    def clean(self):
        username = self.cleaned_data.get('name')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError({'name':'账号不存在，请去注册'})
        password = self.cleaned_data.get('pwd')
        user = User.objects.get(username=username)
        if not check_password(password,user.password):
            raise forms.ValidationError({'pwd':'账号或密码不正确'})

        return self.cleaned_data