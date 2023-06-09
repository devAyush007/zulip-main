# Generated by Django 3.2.7 on 2021-10-10 10:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0364_rename_members_usergroup_direct_members"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usergroup",
            name="direct_members",
            field=models.ManyToManyField(
                related_name="direct_groups",
                through="zerver.UserGroupMembership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="usergroupmembership",
            name="user_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="zerver.usergroup",
            ),
        ),
        migrations.AlterField(
            model_name="usergroupmembership",
            name="user_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
