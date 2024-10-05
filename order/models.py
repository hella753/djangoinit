from django.db import models
from django.contrib.auth.models import User
from store.models import Category
import datetime


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=datetime.date.today)
    order_status = models.CharField(max_length=100)
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_customer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='order_customer_id'
    )
    order_address= models.CharField(max_length=100)
    order_category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=5,
        db_column='order_category_id'
     )

    def __str__(self):
        return (f"Order {self.order_id} made by {self.order_customer_id} "
                f"on {self.order_date.strftime("%m/%d/%Y")} "
                f"| status {self.order_status}")