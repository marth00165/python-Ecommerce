from django.conf import settings
from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def _str_(self):
        return self.title


class OrderItem(models.Model):
    pass

    def _str_(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def _str_(self):
        return self.title

