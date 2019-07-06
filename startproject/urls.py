

from django.contrib import admin
from django.urls import path,include
#from django.conf.urls.static. import static
from django.urls import path
from django.conf import settings
#import blog.views
import wordcount.views

# 특별한 일이 없으면 적용할정도의 import 경로나 메소드를 확인하도록하자.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',wordcount.views.home, name = "home"), # 이렇게 name 에다가 패스를 해주시면 간단히 설명을 해준다 
    path('about/',wordcount.views.about, name = "about"), # 경로들을 잘설정을 해줍니다.
    path('count/',wordcount.views.count, name = "count"), # 탬플릿 태그를 이용하여서 한다.
    path('method/',wordcount.views.method, name = "method"),
  #  path('blog/', include('blog.urls')),
]
