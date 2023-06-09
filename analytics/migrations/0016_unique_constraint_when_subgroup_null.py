# Generated by Django 2.2.10 on 2020-02-29 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0015_clear_duplicate_counts"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="installationcount",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="realmcount",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="streamcount",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="usercount",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="installationcount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=False),
                fields=("property", "subgroup", "end_time"),
                name="unique_installation_count",
            ),
        ),
        migrations.AddConstraint(
            model_name="installationcount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=True),
                fields=("property", "end_time"),
                name="unique_installation_count_null_subgroup",
            ),
        ),
        migrations.AddConstraint(
            model_name="realmcount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=False),
                fields=("realm", "property", "subgroup", "end_time"),
                name="unique_realm_count",
            ),
        ),
        migrations.AddConstraint(
            model_name="realmcount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=True),
                fields=("realm", "property", "end_time"),
                name="unique_realm_count_null_subgroup",
            ),
        ),
        migrations.AddConstraint(
            model_name="streamcount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=False),
                fields=("stream", "property", "subgroup", "end_time"),
                name="unique_stream_count",
            ),
        ),
        migrations.AddConstraint(
            model_name="streamcount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=True),
                fields=("stream", "property", "end_time"),
                name="unique_stream_count_null_subgroup",
            ),
        ),
        migrations.AddConstraint(
            model_name="usercount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=False),
                fields=("user", "property", "subgroup", "end_time"),
                name="unique_user_count",
            ),
        ),
        migrations.AddConstraint(
            model_name="usercount",
            constraint=models.UniqueConstraint(
                condition=models.Q(subgroup__isnull=True),
                fields=("user", "property", "end_time"),
                name="unique_user_count_null_subgroup",
            ),
        ),
    ]
