# Generated by Django 1.11.14 on 2018-09-25 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("zerver", "0189_userprofile_add_some_emojisets"),
    ]

    operations = [
        migrations.CreateModel(
            name="BillingProcessor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("state", models.CharField(max_length=20)),
                ("last_modified", models.DateTimeField(auto_now=True)),
                (
                    "log_row",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.RealmAuditLog"
                    ),
                ),
                (
                    "realm",
                    models.OneToOneField(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="zerver.Realm"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Coupon",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("percent_off", models.SmallIntegerField(unique=True)),
                ("stripe_coupon_id", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("stripe_customer_id", models.CharField(max_length=255, unique=True)),
                ("has_billing_relationship", models.BooleanField(default=False)),
                (
                    "realm",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.Realm"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("nickname", models.CharField(max_length=40, unique=True)),
                ("stripe_plan_id", models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
