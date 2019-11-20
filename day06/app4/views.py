from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from app2.models import Student


def stus(request):
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        # 1.使用切片完成分页
        # stus = Student.objects.all()[(page-1)*3:page*3]


        # 使用django自带的库paginator
        stus = Student.objects.all()
        p = Paginator(stus,3)
        stus = p.page(page)
        return render(request,'stus.html',{'stus':stus})
