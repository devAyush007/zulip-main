# Generated by Django 3.2.9 on 2021-11-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("confirmation", "0010_alter_confirmation_expiry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="confirmation",
            name="expiry_date",
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]
