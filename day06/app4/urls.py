from django.urls import path

from app4.views import stus

urlpatterns = [
    path('stus/',stus)
]