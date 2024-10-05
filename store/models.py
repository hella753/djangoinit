from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()
    category_product_count = models.IntegerField(default=0)
    category_image = models.CharField(max_length=10000, default="")

    def __str__(self):
        return f"{self.category_name} | {self.category_product_count} items"
