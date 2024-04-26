# Generated by Django 4.1.5 on 2024-04-26 06:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0015_alter_onboardorganisationaccount_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="onboardorganisationaccount",
            name="email_domain_name",
            field=models.CharField(
                blank=True,
                help_text="Organization email domain",
                max_length=512,
                null=True,
                verbose_name="organization_email_domain",
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="email",
            field=models.EmailField(
                help_text="Organization owner email address",
                max_length=254,
                unique=True,
                verbose_name="email_address",
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="interested_in",
            field=models.CharField(
                help_text="Interested in Translation, Transcription, VoiceOver",
                max_length=512,
                verbose_name="interested_in",
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="notes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=1000),
                blank=True,
                default=None,
                help_text="Notes provided while updating the status of the onboarding request",
                null=True,
                size=None,
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="org_portal",
            field=models.CharField(
                help_text="Organization website portal",
                max_length=512,
                verbose_name="org_portal",
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="orgname",
            field=models.CharField(
                help_text="Title of Organization",
                max_length=512,
                verbose_name="orgname",
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="purpose",
            field=models.TextField(
                blank=True,
                help_text="Purpose for using Chitralekha",
                max_length=2000,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="source",
            field=models.TextField(
                blank=True,
                help_text="Source from where user came to know about Chitralekha",
                max_length=2000,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="onboardorganisationaccount",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("ON_HOLD", "On Hold"),
                    ("APPROVED", "Approved"),
                    ("REJECTED", "Rejected"),
                ],
                default="PENDING",
                help_text="Current status of organization onboard request",
                max_length=35,
                verbose_name="Onboarding Status",
            ),
        ),
    ]
