# Generated by Django 1.11.16 on 2018-12-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corporate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="default_discount",
            field=models.DecimalField(decimal_places=4, max_digits=7, null=True),
        ),
    ]