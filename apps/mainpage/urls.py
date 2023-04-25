from django.urls import path
from apps.userlogin.views import hello

app_name = 'mainpage'

urlpatterns = [
    path('', hello),
]