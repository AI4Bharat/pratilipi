# Generated by Django 4.0.5 on 2022-07-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("transcript", "0003_alter_transcript_transcript_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transcript",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("hi", "Hindi")],
                default="English",
                max_length=50,
                verbose_name="transcription_language",
            ),
        ),
    ]
