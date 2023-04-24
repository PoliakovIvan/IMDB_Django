from django.urls import path

from apps.userlogin.views import hello

app_name = 'userlogin'

urlpatterns = [
    path('', hello),
]