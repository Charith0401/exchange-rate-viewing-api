from django.urls import path
from . import views

urlpatterns=[
    path("view-rates",views.viewRates,name="view-rates")
]