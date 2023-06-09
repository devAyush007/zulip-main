# Generated by Django 3.2.5 on 2021-07-15 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("zerver", "0333_alter_realm_org_type"),
        ("corporate", "0011_move_exempt_from_from_license_number_check_to_customer_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="ZulipSponsorshipRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "org_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Unspecified"),
                            (10, "Business"),
                            (20, "Open-source project"),
                            (30, "Education (non-profit)"),
                            (35, "Education (for-profit)"),
                            (40, "Research"),
                            (50, "Event or conference"),
                            (60, "Non-profit (registered)"),
                            (70, "Government"),
                            (80, "Political group"),
                            (90, "Community"),
                            (100, "Personal"),
                            (1000, "Other"),
                        ],
                        default=0,
                    ),
                ),
                ("org_website", models.URLField()),
                ("org_description", models.TextField(default="")),
                (
                    "realm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.realm"
                    ),
                ),
                (
                    "requested_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
