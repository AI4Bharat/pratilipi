# Generated by Django 4.0.5 on 2022-07-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transcript", "0002_alter_transcript_transcript_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transcript",
            name="transcript_type",
            field=models.CharField(
                choices=[
                    ("machine_generated", "machine_generated"),
                    ("human_edited", "human_edited"),
                    ("manually_created", "manually_created"),
                    ("original_source", "original_source"),
                ],
                default="machine_generated",
                max_length=50,
                verbose_name="transcript_type",
            ),
        ),
    ]
