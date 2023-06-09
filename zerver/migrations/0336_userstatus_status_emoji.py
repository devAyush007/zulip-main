# Generated by Django 3.2.5 on 2021-07-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0335_add_draft_sync_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="userstatus",
            name="emoji_code",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userstatus",
            name="emoji_name",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="userstatus",
            name="reaction_type",
            field=models.CharField(
                choices=[
                    ("unicode_emoji", "Unicode emoji"),
                    ("realm_emoji", "Custom emoji"),
                    ("zulip_extra_emoji", "Zulip extra emoji"),
                ],
                default="unicode_emoji",
                max_length=30,
            ),
        ),
    ]
