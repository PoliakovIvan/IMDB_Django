from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.userlogin.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.mainpage.urls'))
]
