# Generated by Django 1.11.6 on 2018-04-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0152_realm_default_twenty_four_hour_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customprofilefield",
            name="field_type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Short text"), (2, "Long text")], default=1
            ),
        ),
    ]
