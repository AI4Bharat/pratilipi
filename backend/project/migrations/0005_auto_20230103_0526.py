# Generated by Django 3.2.16 on 2023-01-03 05:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0004_auto_20221228_0519"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="default_description",
            field=models.TextField(
                blank=True,
                help_text="Default Task Description in this Project",
                max_length=400,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="default_eta",
            field=models.DateTimeField(
                blank=True, default=None, null=True, verbose_name="Default_ETA"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="default_priority",
            field=models.CharField(
                blank=True,
                choices=[
                    ("P1", "Priority No 1"),
                    ("P2", "Priority No 2"),
                    ("P3", "Priority No 3"),
                    ("P4", "Priority No 4"),
                ],
                max_length=2,
                null=True,
                verbose_name="Default_Priority",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="default_target_languages",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("en", "English"),
                        ("hi", "Hindi"),
                        ("as", "Assamese"),
                        ("bn", "Bengali"),
                        ("brx", "Bodo"),
                        ("gu", "Gujarati"),
                        ("kn", "Kannada"),
                        ("ks", "Kashmiri"),
                        ("gom", "Konkani"),
                        ("mai", "Maithili"),
                        ("ml", "Malayalam"),
                        ("mr", "Marathi"),
                        ("mni", "Manipuri"),
                        ("ne", "Nepali"),
                        ("or", "Oriya"),
                        ("pa", "Punjabi"),
                        ("sa", "Sanskrit"),
                        ("sd", "Sindhi"),
                        ("si", "Sinhala"),
                        ("ta", "Tamil"),
                        ("te", "Telugu"),
                        ("ur", "Urdu"),
                    ],
                    default=None,
                    max_length=50,
                    null=True,
                ),
                blank=True,
                default=None,
                null=True,
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="default_task_types",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    blank=True,
                    choices=[
                        ("TRANSCRIPTION_EDIT", "Transcription Edit"),
                        ("TRANSCRIPTION_REVIEW", "Transcription Review"),
                        ("TRANSLATION_EDIT", "Translation Edit"),
                        ("TRANSLATION_REVIEW", "Translation Review"),
                    ],
                    default=None,
                    max_length=50,
                    null=True,
                ),
                blank=True,
                default=None,
                null=True,
                size=None,
            ),
        ),
    ]
