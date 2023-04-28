from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import login

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST['email'])

        if user.check_password(request.POST['password']):
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/'))
        
    return HttpResponse(render(request, 'userlogin/login.html'))