# Generated by Django 3.2.16 on 2023-03-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0010_alter_task_task_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("SELECTED_SOURCE", "Selected Source"),
                    ("INPROGRESS", "In Progress"),
                    ("POST_PROGRESS", "Post Progress"),
                    ("COMPLETE", "Complete"),
                ],
                default=None,
                max_length=35,
                verbose_name="Task Status",
            ),
        ),
    ]
