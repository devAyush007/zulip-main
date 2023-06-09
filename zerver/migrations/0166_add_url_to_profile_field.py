# Generated by Django 1.11.11 on 2018-04-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0165_add_date_to_profile_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customprofilefield",
            name="field_type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Short text"),
                    (2, "Long text"),
                    (4, "Date"),
                    (5, "URL"),
                    (3, "Choice"),
                ],
                default=1,
            ),
        ),
    ]
