# Generated by Django 1.11.18 on 2019-01-31 22:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("corporate", "0006_nullable_stripe_customer_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="billingprocessor",
            name="log_row",
        ),
        migrations.RemoveField(
            model_name="billingprocessor",
            name="realm",
        ),
        migrations.DeleteModel(
            name="Coupon",
        ),
        migrations.DeleteModel(
            name="Plan",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="has_billing_relationship",
        ),
        migrations.RemoveField(
            model_name="customerplan",
            name="licenses",
        ),
        migrations.DeleteModel(
            name="BillingProcessor",
        ),
    ]
