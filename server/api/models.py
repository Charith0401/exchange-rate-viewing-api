from django.db import models

# Create your models here.

class Rates(models.Model):
    date=models.DateField(auto_now=True)
    base_currency=models.CharField(default="USD")
    quote_currency=models.CharField()
    exchange_rate=models.DecimalField(decimal_places=1,max_digits=4)

    def __str__(self):
        return (self.quote_currency)

