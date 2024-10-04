from django.db import models


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=100)
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_customer_id = models.IntegerField()
    order_address= models.CharField(max_length=100)
    order_category_id = models.IntegerField(null=True)
