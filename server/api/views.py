from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from django.middleware.csrf import get_token
from django.core import serializers
from django.db.models import Max,OuterRef,Subquery,F
import json
from api.models import Rates
import datetime

@api_view(["GET"])
def viewAllRates(request):
    if (request.method=="GET"):

        #to get distinct values ordering valueslist and distinct is needed based on which field needs to be distinct
        #when flat is true, tuples are eliminated so [[1],[2]] would become [1,2]

        #aggregate() will return a single dictionary value but distinct() will return a queryset and so aggregate and distinct isnt allowed
        # rates=Rates.objects.order_by().distinct("quote_currency").aggregate(Max("date")).values() 
        #.values does grouping
        #

        rates=Rates.objects.filter(quote_currency=OuterRef("quote_currency")).order_by("-date").annotate(latest_date=Max("date")).values("latest_date")[:1]
        # rates=Rates.objects.filter(quote_currency=OuterRef("quote_currency")).annotate(latest_date=Max("date")).values("latest_date")[:1]
        subquery=Subquery(rates)

        result=Rates.objects.filter(date=subquery).values()
  

        # final_query=Rates.objects.filter(quote_currency=subquery)
        # print("and this",final_query)
        # date=datetime.date(2024,5,29)
        # rates=Rates(date=date,quote_currency="JPY",exchange_rate=101.3)
        # rates.save()
        # print(rates)
        
        return JsonResponse(list(result),safe=False)
    
@api_view(["GET"])
def viewHistoricalRates(request,quoteCurrency):
    if (request.method=="GET"):

        #entry of lkr would be taken as LKR
        formattedQuoteCurrency=quoteCurrency.upper()

        #taking the current date and going back 30 days
        date=datetime.datetime.now()-datetime.timedelta(days=30)

        #using __greaterthan to filter dates greater than the date that was calculated 30 days ago
        #you can import "Q" from django models and this basically allows you to do OR operations
        #at the end of the operation add .values() so that the model instances arent includes which means no metadata included in result
        historicalRates=Rates.objects.filter(date__gt=date).filter(quote_currency=formattedQuoteCurrency).values() 

        print(historicalRates)
        
        #serializing data to convert from queryset to json and parsing the string object to an object to be displayed
        return JsonResponse(list(historicalRates),safe=False)

@api_view(["GET"])
def currentExchangeRate(request,quoteCurrency):
    if (request.method=="GET"):
        
        # rates=Rates.objects.filter(quote_currency=quote_currency).aggregate(Max("exchange_rate")) this will get you the max value of a certain field

        formattedQuoteCurrency=quoteCurrency.upper() #entry of lkr would be taken as LKR

        #aggregate doesnt return a queryset it returns a dictionary and you have to use dictionaryname.get("max_field") like aggregate(max_field=Max("date"))
        latestDate=Rates.objects.filter(quote_currency=formattedQuoteCurrency).aggregate(Max("date"))
        
        latestRate=Rates.objects.filter(date=latestDate.get("date__max")).filter(quote_currency=formattedQuoteCurrency).values()
   
        return JsonResponse(list(latestRate),safe=False)
    


# subquery = Rates.objects.filter(
#     quote_currency=OuterRef('quote_currency')
# ).values('quote_currency').annotate(max_rate=Max('rate')).values('max_rate')[:1]
#if we take a query like this, the OuterRef is referencing the quote_currency after the annotate and values operations have been applied to the initial
#query