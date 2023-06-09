# Generated by Django 1.10.5 on 2017-02-15 06:18
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0053_emailchangestatus"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="icon_source",
            field=models.CharField(
                choices=[("G", "Hosted by Gravatar"), ("U", "Uploaded by administrator")],
                default="G",
                max_length=1,
            ),
        ),
        migrations.AddField(
            model_name="realm",
            name="icon_version",
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
