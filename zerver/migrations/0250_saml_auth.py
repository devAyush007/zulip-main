# Generated by Django 1.11.23 on 2019-09-19 00:50

import bitfield.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0249_userprofile_role_finish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realm",
            name="authentication_methods",
            field=bitfield.models.BitField(
                ["Google", "Email", "GitHub", "LDAP", "Dev", "RemoteUser", "AzureAD", "SAML"],
                default=2147483647,
            ),
        ),
    ]
