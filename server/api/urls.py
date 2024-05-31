from django.urls import path
from . import views

urlpatterns=[
    path("view-rates",views.viewAllRates,name="view-rates"),
    path("view-historical-rates/<str:quote_currency>",views.viewHistoricalRates,name="view-historical-rates")
]