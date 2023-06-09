# Generated by Django 3.1.7 on 2021-04-07 01:54

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0314_muted_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="RealmPlayground",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "url_prefix",
                    models.TextField(validators=[django.core.validators.URLValidator()]),
                ),
                ("name", models.TextField(db_index=True)),
                (
                    "pygments_language",
                    models.CharField(
                        db_index=True,
                        max_length=40,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Invalid characters in pygments language",
                                regex="^[ a-zA-Z0-9_+-./#]*$",
                            )
                        ],
                    ),
                ),
                (
                    "realm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.realm"
                    ),
                ),
            ],
            options={
                "unique_together": {("realm", "name")},
            },
        ),
    ]
