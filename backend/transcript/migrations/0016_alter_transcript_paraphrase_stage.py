# Generated by Django 4.1.5 on 2024-07-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0015_transcript_paraphrase_stage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='paraphrase_stage',
            field=models.BooleanField(blank=True, default=False, help_text='Indicates whether transcription is in paraphrasing stage', null=True, verbose_name='Paraphrasing Stage'),
        ),
    ]
