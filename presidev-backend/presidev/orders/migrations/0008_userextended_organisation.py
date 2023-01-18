# Generated by Django 4.1 on 2023-01-11 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0007_rename_orders_order_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="userextended",
            name="organisation",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="orders.organisation",
            ),
        ),
    ]
