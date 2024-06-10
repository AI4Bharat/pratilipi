# Generated by Django 4.1.5 on 2023-09-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("translation", "0015_alter_translation_target_language")]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="translation_type",
            field=models.CharField(
                choices=[
                    ("MACHINE_GENERATED", "Machine Generated"),
                    ("MANUALLY_CREATED", "Manually Created"),
                    ("ORIGINAL_SOURCE", "Original Source"),
                ],
                max_length=35,
                verbose_name="Translation Type",
            ),
        )
    ]
