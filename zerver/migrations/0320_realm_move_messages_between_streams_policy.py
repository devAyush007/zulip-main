# Generated by Django 3.1.7 on 2021-04-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0319_realm_giphy_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="move_messages_between_streams_policy",
            field=models.PositiveSmallIntegerField(default=2),
        ),
    ]
