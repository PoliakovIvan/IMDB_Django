
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.userlogin.urls', namespace='auth')),
    path('admin/', admin.site.urls),
    path('', include('apps.mainpage.urls', namespace='mainpage')),
   
]
