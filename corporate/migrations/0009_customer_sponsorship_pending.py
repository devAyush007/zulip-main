# Generated by Django 2.2.13 on 2020-06-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corporate", "0008_nullable_next_invoice_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="sponsorship_pending",
            field=models.BooleanField(default=False),
        ),
    ]
