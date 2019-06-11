"""startproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import wordcount.views

# 특별한 일이 없으면 적용할정도의 import 경로나 메소드를 확인하도록하자.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcount.views.home, name = "home"), # 이렇게 name 에다가 패스를 해주시면 간단히 설명을 해준다 
    path('about/',wordcount.views.about, name = "about"), # 경로들을 잘설정을 해줍니다.
    path('count/',wordcount.views.count, name = "count"), # 탬플릿 태그를 이용하여서 한다.
]
