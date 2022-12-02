from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def alert(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

@csrf_exempt
def login(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

@csrf_exempt
def dashboard(request):
    if request.method == 'GET':
        pass
