# Generated by Django 5.1.1 on 2024-10-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_address_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_category_id',
            field=models.IntegerField(null=True),
        ),
    ]
