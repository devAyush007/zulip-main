# Generated by Django 1.11.14 on 2018-08-22 06:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0012_coupon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="billing_user",
        ),
    ]
