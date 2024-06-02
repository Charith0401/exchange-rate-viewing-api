#DRF.spectacular basically uses views and serializers to help describe a rest endpoint and a serializer basically does data conversion
#data fields that are in a model (done by the serializer)

from rest_framework import serializers
from api.models import Rates

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rates
        fields=["date","base_currency","quote_currency","exchange_rate"]