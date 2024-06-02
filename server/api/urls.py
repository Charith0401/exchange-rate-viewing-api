from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns=[
    path("view-rates",views.viewAllRates,name="view-rates"),
    path("view-historical-rates/<str:quoteCurrency>",views.viewHistoricalRates,name="view-historical-rates"),
    path("view-exchange-rate/<str:quoteCurrency>",views.currentExchangeRate,name="view-exchange-rate"),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]