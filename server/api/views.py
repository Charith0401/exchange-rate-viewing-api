from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.core import serializers
import json
from api.models import Rates
import datetime

# Create your views here.

#you can import "Q" from django models and this basically allows you to do OR operations

@api_view(["GET"])
def viewAllRates(request):
    if (request.method=="GET"):
        rates=Rates.objects.all()
        # date=datetime.date(2024,5,28)
        # rates=Rates(date=date,quote_currency="LKR",exchange_rate=298.3)
        # rates.save()
        serializedRates=serializers.serialize("json",rates)
        return JsonResponse(json.loads(serializedRates),safe=False)
    
@api_view(["GET"])
def viewHistoricalRates(request,quote_currency):
    if (request.method=="GET"):
        formatted_quote_currency=quote_currency.upper() #entry of lkr would be taken as LKR

        date=datetime.datetime.now()-datetime.timedelta(days=30) #taking the current date and going back 30 days
        historicalRates=Rates.objects.filter(date__gt=date).filter(quote_currency=formatted_quote_currency) #using __greaterthan to filter dates greater than the date that was calculated 30 days ago

        return JsonResponse(json.loads(serializers.serialize("json",historicalRates)),safe=False) #serializing data to convert from queryset to json and parsing the string object to an object to be displayed
