from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from models import Alert
import json

# Create your views here.
@csrf_exempt
def alert(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        data = json.loads(request.body)
        Alert.objects.create(name=data["alertName"], address=data["alertAddress"], slack_webhook=data["alertSlackWebhook"])
        HttpResponse(json.dumps({"status": "ok"}), content_type="text/json")

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
