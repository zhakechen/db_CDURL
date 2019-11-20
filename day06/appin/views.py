from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.d
from django.urls import reverse
from django.views import View


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def params1(request,id):
    if request.method == 'GET':

        return HttpResponse('参数:%d'%id)

def params2(request,name):
    if request.method == 'GET':

        return HttpResponse('name:%s'%name)

def params3(request,id,id2):
    if request.method == 'GET':

        return HttpResponse('id:%d,id:%d'%(id,id2))

def params4(request,uid):
    if request.method == 'GET':

        return HttpResponse('uid:%s'% uid)

class Params5(View):

    def get(self,*args,**kwargs):

        return HttpResponse('%s年%s月%s日'%(kwargs['year'],
                                         kwargs['month'],
                                         kwargs['day']))


def params6(request,name1,name2):
    if request.method == 'GET':
        return HttpResponse('参数1:%s,参数2:%s'% (name1,name2))

def params7(request,name1,name2):
    if request.method == 'GET':
        return HttpResponse('参数1:%s,参数:%s'%(name1,name2))


def register(request):
    if request.method == 'GET':

        return render(request,'register.html')

    if request.method == 'POST':
        # 如果只使用render渲染页面，浏览器地址不会有变化
        # return redirect('/appin/login')
        # reverse('namespase')
        print(reverse('p2:p1',kwargs={'id':111}))
        # return redirect('appin/params1/111')
        # return redirect(reverse('p2:p1',kwargs={'id':1234}))
        # return redirect(reverse('p2:p3',kwargs={'id':123,'id2':321}))
        return redirect(reverse('p2:p5',kwargs={'year':2019,'month':11,'day':13}))




def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

