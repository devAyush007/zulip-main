# Generated by Django 1.11.16 on 2018-12-30 10:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0199_userstatus"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="preregistrationuser",
            name="invited_as_admin",
        ),
    ]
