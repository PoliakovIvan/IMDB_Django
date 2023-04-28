from django.urls import path


from apps.userlogin.views import login_view

app_name = 'userlogin'

urlpatterns = [
    path('login/', login_view),
    
]