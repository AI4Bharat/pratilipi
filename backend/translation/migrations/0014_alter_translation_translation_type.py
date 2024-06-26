# Generated by Django 3.2.16 on 2023-05-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translation", "0013_alter_translation_translation_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="translation_type",
            field=models.CharField(
                choices=[
                    ("MACHINE_GENERATED", "Machine Generated"),
                    ("MANUALLY_CREATED", "Manually Created"),
                ],
                max_length=35,
                verbose_name="Translation Type",
            ),
        ),
    ]
