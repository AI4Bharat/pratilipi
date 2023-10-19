# Generated by Django 4.0.5 on 2022-09-19 05:01

from django.db import migrations, models


# Custom Migrations
def update_human_edited_to_updated_machine_generated(apps, schema_editor):
    """Update human edited translations to updated machine generated"""
    from translation.models import Translation

    Translation.objects.filter(translation_type="he").update(translation_type="umg")


class Migration(migrations.Migration):
    dependencies = [
        ("translation", "0003_rename_target_lang_translation_target_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translation",
            name="translation_type",
            field=models.CharField(
                choices=[
                    ("mg", "Machine Generated"),
                    ("umg", "Updated Machine Generated"),
                    ("mc", "Manually Created"),
                ],
                max_length=3,
                verbose_name="Translation Type",
            ),
        ),
        migrations.RunPython(update_human_edited_to_updated_machine_generated),
    ]
