from django.db import models


class StudentInfo(models.Model):
    s_addr = models.CharField(max_length=100,null=True)
    s_phone = models.CharField(max_length=11,null=True)


    class Meta:
        db_table = 'tb_student_info'


class Grade(models.Model):
    g_name = models.CharField(max_length=10,unique=True,null=False)

    class Meta:
        db_table= 'tb_grade'

class Course(models.Model):
    c_name = models.CharField(max_length=10,unique=True,null=False)

    class Meta:
        db_table = 'tb_course'



class Student(models.Model):
    s_name = models.CharField(max_length=10,unique=True,null=False)
    s_age = models.IntegerField(default=18)
    a_gender = models.BooleanField(default=1)
    s_create_time = models.DateTimeField(auto_now_add=True)
    # 定义一对一的关系
    info = models.OneToOneField(StudentInfo,
                                on_delete=models.CASCADE,
                                )
    # 定义一对多的关联关系，Foreignkey只能定义在多的一方
    g = models.ForeignKey(Grade,on_delete=models.CASCADE,null=True,
                          )

    c = models.ManyToManyField(Course)

    class Meta:
        db_table = 'tb_student'

    # 定义多对多关联关系，需要中间表

