# Generated by Django 1.11.24 on 2019-09-24 00:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0281_zoom_oauth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="zoom_api_key",
        ),
        migrations.RemoveField(
            model_name="realm",
            name="zoom_api_secret",
        ),
        migrations.RemoveField(
            model_name="realm",
            name="zoom_user_id",
        ),
    ]
