# Generated by Django 4.1.5 on 2024-05-16 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transcript', '0015_alter_transcript_language'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0017_alter_task_status'),
        ('video', '0019_alter_video_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationVoiceover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translation_voiceover_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Translation Voiceover UUID')),
                ('translation_type', models.CharField(choices=[('MACHINE_GENERATED', 'Machine Generated'), ('MANUALLY_CREATED', 'Manually Created')], max_length=35, verbose_name='Translation Type')),
                ('voiceover_type', models.CharField(choices=[('MACHINE_GENERATED', 'Machine Generated'), ('MANUALLY_CREATED', 'Manually Created')], max_length=35, verbose_name='Voiceover Type')),
                ('translation_status', models.CharField(choices=[('SELECT_SOURCE', 'Selected Source'), ('EDITOR_ASSIGNED', 'Editor Assigned'), ('EDIT_INPROGRESS', 'Edit In Progress'), ('EDIT_COMPLETE', 'Edit Complete'), ('REVIEWER_ASSIGNED', 'Reviewer Assigned'), ('REVIEW_INPROGRESS', 'Review In Progress'), ('REVIEW_COMPLETE', 'Review Complete')], default=None, max_length=35, verbose_name='Status')),
                ('voiceover_status', models.CharField(choices=[('SELECT_SOURCE', 'Selected Source'), ('EDITOR_ASSIGNED', 'Editor Assigned'), ('EDIT_INPROGRESS', 'Edit In Progress'), ('EDIT_COMPLETE', 'Edit Complete'), ('REVIEWER_ASSIGNED', 'Reviewer Assigned'), ('REVIEW_INPROGRESS', 'Review In Progress'), ('REVIEW_COMPLETE', 'Review Complete')], default=None, max_length=35, verbose_name='Status')),
                ('translation_payload', models.JSONField(null=True, verbose_name='Translation Payload')),
                ('voiceover_payload', models.JSONField(null=True, verbose_name='Voiceover Payload')),
                ('target_language', models.CharField(choices=[('en', 'English'), ('hi', 'Hindi'), ('as', 'Assamese'), ('bn', 'Bengali'), ('brx', 'Bodo'), ('doi', 'Dogri'), ('gu', 'Gujarati'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('gom', 'Konkani'), ('mai', 'Maithili'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('mni', 'Manipuri'), ('ne', 'Nepali'), ('or', 'Oriya'), ('pa', 'Punjabi'), ('sa', 'Sanskrit'), ('sat', 'Santali'), ('sd', 'Sindhi'), ('ta', 'Tamil'), ('te', 'Telugu'), ('ur', 'Urdu'), ('en', 'English'), ('hi', 'Hindi'), ('as', 'Assamese'), ('bn', 'Bengali'), ('brx', 'Bodo'), ('doi', 'Dogri'), ('gu', 'Gujarati'), ('kn', 'Kannada'), ('ks', 'Kashmiri'), ('gom', 'Konkani'), ('mai', 'Maithili'), ('ml', 'Malayalam'), ('mr', 'Marathi'), ('mni', 'Manipuri'), ('ne', 'Nepali'), ('or', 'Oriya'), ('pa', 'Punjabi'), ('sa', 'Sanskrit'), ('sat', 'Santali'), ('sd', 'Sindhi'), ('si', 'Sinhala'), ('ta', 'Tamil'), ('te', 'Telugu'), ('ur', 'Urdu')], max_length=4, verbose_name='Target Language')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('voiceover_azure_url', models.URLField(blank=True, default=None, null=True, verbose_name='Azure URL')),
                ('voiceover_azure_url_audio', models.URLField(blank=True, default=None, null=True, verbose_name='Azure Audio URL')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_voiceovers', to='task.task', verbose_name='Task')),
                ('transcript', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translation_voiceovers', to='transcript.transcript', verbose_name='Transcript')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Speaker/Translator')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_voiceovers', to='video.video', verbose_name='Video')),
            ],
        ),
    ]
