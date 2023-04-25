from django.http import HttpResponse
from django.shortcuts import render


def login_view(request):
    return HttpResponse(render(request, 'userlogin/login.html'))