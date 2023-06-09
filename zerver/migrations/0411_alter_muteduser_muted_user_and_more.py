# Generated by Django 4.0.7 on 2022-09-15 09:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0410_alter_stream_can_remove_subscribers_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="muteduser",
            name="muted_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="muted",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="muteduser",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="muter",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
