from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns=[
    path("view-rates",views.viewAllRates,name="view-rates"),
    path("view-historical-rates/<str:quoteCurrency>",views.viewHistoricalRates,name="view-historical-rates"),
    path("view-exchange-rate/<str:quoteCurrency>",views.currentExchangeRate,name="view-exchange-rate"),
    path('api/schema/', SpectacularAPIView.as_view())
]