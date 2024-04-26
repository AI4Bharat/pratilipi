# Generated by Django 4.1.5 on 2024-04-24 07:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0014_onboardorganisationaccount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="notes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=1000),
                blank=True,
                default=None,
                null=True,
                size=None,
            ),
        ),
    ]
