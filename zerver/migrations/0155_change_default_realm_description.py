# Generated by Django 1.11.11 on 2018-04-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0154_fix_invalid_bot_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realm",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
