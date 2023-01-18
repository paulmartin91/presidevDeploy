# Generated by Django 4.1 on 2023-01-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="orders",
        ),
        migrations.AddField(
            model_name="item",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="orders",
            field=models.ManyToManyField(through="orders.OrderItems", to="orders.item"),
        ),
    ]
