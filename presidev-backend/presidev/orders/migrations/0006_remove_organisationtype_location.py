# Generated by Django 4.1 on 2023-01-10 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_alter_location_county_alter_location_first_line_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organisationtype",
            name="location",
        ),
    ]
