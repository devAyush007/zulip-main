# Generated by Django 1.11.26 on 2020-01-06 01:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0258_enable_online_push_notifications_default"),
    ]

    operations = [
        migrations.CreateModel(
            name="MissedMessageEmailAddress",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("email_token", models.CharField(db_index=True, max_length=34, unique=True)),
                (
                    "timestamp",
                    models.DateTimeField(db_index=True, default=django.utils.timezone.now),
                ),
                ("times_used", models.PositiveIntegerField(db_index=True, default=0)),
                (
                    "message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.Message"
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
