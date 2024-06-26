# Generated by Django 3.2.16 on 2023-06-09 12:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0014_alter_video_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("hi", "Hindi"),
                    ("as", "Assamese"),
                    ("bn", "Bengali"),
                    ("gu", "Gujarati"),
                    ("kn", "Kannada"),
                    ("ml", "Malayalam"),
                    ("mr", "Marathi"),
                    ("or", "Oriya"),
                    ("pa", "Punjabi"),
                    ("ta", "Tamil"),
                    ("te", "Telugu"),
                ],
                max_length=4,
                verbose_name="Target Language",
            ),
        ),
    ]
