from datetime import datetime, timedelta
import uuid

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app3.form import UserRegisterForm, UserLoginForm
from app3.models import User, UserToken, UserImage
from utils.function import login_check


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    if request.method == 'POST':
        # 技术:1.form表单的使用
        # 2.密码的处理make_password
        form = UserRegisterForm(request.POST)
        # .is_valid():判断表单验证是否通过，通过返回True,
        if form.is_valid():
            # 校验无问题、账号不存在，密码和确认密码一致
            username = form.cleaned_data.get('name')
            password = make_password(form.cleaned_data.get('pwd'))
            User.objects.create(username=username,
                                password=password)
            return redirect(reverse('app3:login'))


        error = form.errors
        return render(request,'register.html',{'errors':error})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # 保存登录成功的状态
            # coolie  session
            # request.COOKIES['name'] = form.cleaned_data.get('name')

            # return redirect(reverse('app3:index'))
            res =redirect(reverse('app3:index'))
            name = form.cleaned_data.get('name')
            # cookie 是存在前段的一个文本，文本大小有限制
            # cookie 中数据是明文存储的，敏感信息不能存
            res.set_cookie('name',name,max_age=3000)
            return res

        errors = form.errors
        return render(request,'login.html',{'errors':errors})

def index(request):
    if request.method == 'GET':
        # name = request.COOKIES.get('name')
        # if name:
        #     return HttpResponse('我的首页，先登录')
        # else:
        #     return redirect(reverse('app3:register'))
        token = request.COOKIES.get('token')
        # 如果请求的cookie中没有token,表示用户一定没有登录
        if not token:
            return redirect(reverse('app3:my_login'))
        user_token = UserToken.objects.filter(token=token).first()
        if not user_token:
            return redirect(reverse('app3:my_login'))
        # TODO判断时间是否过期
        return HttpResponse('我的首页，登录后才能访问')

def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # 1.将登陆的标识符token写入到响应cookie中，然后丢给前段进行保存
            token = uuid.uuid4().hex
            res = redirect(reverse('app3:index'))
            res.set_cookie('token',token,max_age=3000)
            # 2.将登录标识符token和当前登录的人进行绑定
            # 实现方式：mysql ,redis
            name = form.cleaned_data.get('name')
            user = User.objects.get(username=name)
            timeout = datetime.now() + timedelta(minutes=50)
            # 2.1)判断当前登录用户是否在user_token表中加入了数据
            # 2.2）如果有数据，则更新token和timeout字段
            # 2.3)如果没有数据，则新建token和user的关联关系
            user_token = UserToken.objects.filter(user=user).first()
            if user_token:
                user_token.token = token
                user_token.timeout = timeout
                user_token.save()
            else:

                UserToken.objects.create(token=token,user=user,
                                     timeout=timeout)

            return res

            pass
        errors = form.errors
        return render(request, 'login.html', {'errors': errors})

def session_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            user = User.objects.get(username=username)
            # 操作session其实完成了两个操作
            # 1.向前端的cookie中设置登录标识符叫session
            # 2.向后端的django_session表中存登录标识符

            request.session['user_id'] = user.id
            request.session.modified = True

            return redirect(reverse('app3:session_index'))

        errors = form.errors
        return render(request, 'login.html', {'errors': errors})


# @login_check
def session_index(request):
    if request.method == 'GET':
        # # 先从前端的cookie中拿到登录标识符sessionid
        # # 然后从django_session表中去找sesssion_key字段
        # # 最后在从session_data中获取键值对user_id
        # user_id = request.session.get('user_id')
        # if user_id:
        #
        #     return HttpResponse('登录后才能访问')
        # else:
        #     return redirect(reverse('app3:session_login'))
        # return HttpResponse('登录后才能访问')



        # user_id = request.session.get('user_id')
        # user =User.objects.get(pk=user_id)
        print('session_index 方法被调用')
        return render(request,'xindex.html')


def icon(request):
    if request.method == 'GET':
        images = UserImage.objects.all()
        return render(request,'article_add.html',{'images':images})
    if request.method == 'POST':
        # 取图片
        icon = request.FILES.get('images')
        # 将图片保存到media文件夹中，且数据表到字段中存储图片到相对路径
        UserImage.objects.create(images=icon)
        return HttpResponse('图片上传成功')