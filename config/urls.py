
from django.contrib import admin
from django.urls import path, include

from apps.mainpage.views import hello, abc

urlpatterns = [
    path('auth/', include('apps.userlogin.urls')),
    path('admin/', admin.site.urls),
    path('', hello),
    path('abc/', abc),
   
]
