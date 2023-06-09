# Generated by Django 1.11.5 on 2017-10-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0004_remove_deployment_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remotepushdevicetoken",
            name="token",
            field=models.CharField(db_index=True, max_length=4096),
        ),
        migrations.AlterField(
            model_name="remotepushdevicetoken",
            name="user_id",
            field=models.BigIntegerField(db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name="remotepushdevicetoken",
            unique_together={("server", "token")},
        ),
    ]
