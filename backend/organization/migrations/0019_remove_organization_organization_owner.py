# Generated by Django 4.1.5 on 2024-08-02 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("organization", "0018_auto_20240802_1056"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="organization_owner",
        ),
    ]
