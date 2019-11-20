from django.urls import path
from app2.views import *

urlpatterns =[
    path('stu_add', stu_add),
    path('stu_info/',stu_info),
    path('grade_add_stu/',grade_add_stu),
    path('grade_stu/',grade_stu),
    path('stu_cou/',stu_cou),

]