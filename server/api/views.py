from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.core import serializers
import json
from api.models import Rates

# Create your views here.

@api_view(["GET"])
def viewRates(request):
    if (request.method=="GET"):
        rates=Rates.objects.all()
        
        serializedRates=serializers.serialize("json",rates)
        return JsonResponse(json.loads(serializedRates),safe=False)
# @api_view(["POST"])
# def addRates(request):
#     if (request.method=="POST"):
#         date=
#         base_currency=models.CharField(default="USD")
#         quote_currency=models.CharField()
#         exchange_rate=models.DecimalField(decimal_places=1,max_digits=4)
