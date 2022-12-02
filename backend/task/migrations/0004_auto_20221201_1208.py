# Generated by Django 3.2.16 on 2022-12-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0003_alter_task_eta"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "NEW"),
                    ("SELECTED_SOURCE", "SELECTED_SOURCE"),
                    ("INPROGRESS", "INPROGRESS"),
                    ("COMPLETE", "COMPLETE"),
                ],
                default=None,
                max_length=35,
                verbose_name="Task Status",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.CharField(
                choices=[
                    ("TRANSCRIPTION_EDIT", "Transcription Edit"),
                    ("TRANSCRIPTION_REVIEW", "Transcription Review"),
                    ("TRANSLATION_EDIT", "Translation Edit"),
                    ("TRANSLATION_REVIEW", "Translation Review"),
                ],
                max_length=35,
            ),
        ),
    ]
