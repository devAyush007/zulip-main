# Generated by Django 1.11.20 on 2019-04-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0221_subscription_notifications_data_migration"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="fluid_layout_width",
            field=models.BooleanField(default=False),
        ),
    ]
