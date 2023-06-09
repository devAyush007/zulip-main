# Generated by Django 1.11.16 on 2018-12-06 21:36

from django.db import migrations, models

EMAIL_ADDRESS_VISIBILITY_EVERYONE = 1


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0192_customprofilefieldvalue_rendered_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="email_address_visibility",
            field=models.PositiveSmallIntegerField(default=EMAIL_ADDRESS_VISIBILITY_EVERYONE),
        ),
    ]
