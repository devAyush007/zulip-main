# Generated by Django 3.2.7 on 2021-10-12 21:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0363_send_read_receipts_user_setting"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usergroup",
            old_name="members",
            new_name="direct_members",
        ),
    ]
