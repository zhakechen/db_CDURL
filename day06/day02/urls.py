"""day02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static  # 手动导包

from day02.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app2.urls')),
    # django 2.0 以上
    path('appin/',include(('appin.urls','appin'),namespace='p2')),
    # django 2.0以下
    # path('appin/', include('appin.urls', 'appin', namespace='p2')),
    path('app3/',include(('app3.urls','app3'),namespace='app3')),
    path('app4/',include('app4.urls')),
    path('app5/',include('app5.urls')),
]

urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)