# Generated by Django 3.2.9 on 2021-12-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0022_remotezulipserver_create_audit_log_backfill"),
    ]

    operations = [
        migrations.AddField(
            model_name="remotezulipserver",
            name="deactivated",
            field=models.BooleanField(default=False),
        ),
    ]
