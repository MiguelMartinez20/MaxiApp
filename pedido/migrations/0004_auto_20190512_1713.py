# Generated by Django 2.2.1 on 2019-05-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_remove_order_order_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]