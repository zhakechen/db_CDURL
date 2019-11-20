from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app2.models import StudentInfo, Student, Grade, Course


def stu_add(request):
    if request.method == 'GET':
        return render(request,'stu_info.html',)
    if request.method == 'POST':
        # 1.获取数据
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        addr = request.POST.get("addr")
        photo = request.POST.get("photo")
        # 2.判断拓展表字段是否填写，填了就创建
        if addr or photo:
            info = StudentInfo.objects.create(
                s_addr = addr,
                s_phone= photo
            )
        # 3.判断拓展表是否创建，如果创建
        # 则在创建学生表
        stu = Student()
        stu.s_name = username
        stu.s_age = age
        stu.s_gender = gender
        if info:
            # stu.info = info
            stu.info_id = info.id

        # stu.info = '关联对象'
        # stu.info_id = '主键值'
        stu.save()


        return HttpResponse('添加成功')

def stu_info(request):
    if request.method == 'GET':
        # 知道姓名查手机号等
        # stu = Student.objects.filter(s_name='等等').first()
        # print(stu.info)
        # info = stu.info
        # print(info.s_addr)

        # 知道手机号，查人

        info = StudentInfo.objects.filter(s_phone='12345678901').first()
        # 如果OneToOneField中没定义relate_name参数
        # 通过拓展表查询学生信息，info.student
        print(info.student)
        # 如果OneToOneField中没定义relate_name参数
        # 通过拓展表查询学生信息，info.related_name参数

        print(info.a)


def grade_add_stu(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        stus = Student.objects.all()
        return render(request,'grade.html',
                      {'stus':stus,'grades':grades})
    if request.method == 'POST':
        # 获取数据
        g = request.POST.get('g')
        sid = request.POST.get('sid')
        # 2.一对多关联关系
        for id in sid:
            stu = Student.objects.get(pk=id)
            # stu.g = '关联对象'
            stu.g = g
            stu.save()

        return HttpResponse('分配成功')


def grade_stu(request):
    if request.method == 'GET':
        # 知道学生电话，查询班级信息
        info = StudentInfo.objects.filter(s_phone='12345678901').first()
        # stu = info.a
        # stu = info.g
        grade = info.a.g
        print(grade)

        # 2.查询python
        g = Grade.objects.first(g_name='python').first()
        #2.1  定义ForeignKey时，没有指定related_name
        #   g.学生模型小写_set.filter().all()
        #`  `stus = g.student_set.all()
        # 2.2 定义定义ForeignKey时，指定related_name参数
        #   g.related_name参数.all()

        stus = g.student_set.all()

        return HttpResponse('查询成功')

def stu_cou(request):
    if request.method == 'GET':
        stu = Student.objects.get(pk=1)
        stu.c.all()
        # 向中间表中加数据
        cou = Course.objects.get(pk=2)
        # stu.c.add(cou)
        # 1.1)在定义ManyToManyFile时，没有定义related_naem参数
        # cou.student_set.add(stu)
        # 1.2)在定义义ManyToManyFile时，有定义related_naem参数
        cou.d.add(stu)
        # 删除中间表加入数据
        #stu.c.remove(cou)

        return HttpResponse('多对多数据关联成功')

def delete_info(request):
    if request.method == 'GET':

        g= Grade.objects.get(pk=1)

        g.delete()
        return HttpResponse('on_delete操作')