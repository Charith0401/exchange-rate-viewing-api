from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.core import serializers
from django.db.models import Max
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
def viewHistoricalRates(request,quoteCurrency):
    if (request.method=="GET"):
        formattedQuoteCurrency=quoteCurrency.upper() #entry of lkr would be taken as LKR

        date=datetime.datetime.now()-datetime.timedelta(days=30) #taking the current date and going back 30 days
        historicalRates=Rates.objects.filter(date__gt=date).filter(quote_currency=formattedQuoteCurrency) #using __greaterthan to filter dates greater than the date that was calculated 30 days ago

        return JsonResponse(json.loads(serializers.serialize("json",historicalRates)),safe=False) #serializing data to convert from queryset to json and parsing the string object to an object to be displayed

@api_view(["GET"])
def currentExchangeRate(request,quoteCurrency):
    if (request.method=="GET"):
        # rates=Rates.objects.filter(quote_currency=quote_currency).aggregate(Max("exchange_rate")) this will get you the max value of a certain field

        formattedQuoteCurrency=quoteCurrency.upper() #entry of lkr would be taken as LKR

        #aggregate doesnt return a queryset it returns a dictionary and you have to use dictionaryname.get("max_field") like aggregate(max_field=Max("date"))
        latestDate=Rates.objects.filter(quote_currency=formattedQuoteCurrency).aggregate(Max("date"))
        
        latestRate=Rates.objects.filter(date=latestDate.get("date__max")).filter(quote_currency=formattedQuoteCurrency)
   
        return JsonResponse(json.loads(serializers.serialize("json",latestRate)),safe=False)