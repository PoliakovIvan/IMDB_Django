from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def hello(request):
    return HttpResponse('Hello')

@login_required
def abc(request):
    return HttpResponse('abc')

