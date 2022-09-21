# Generated by Django 4.0.5 on 2022-09-20 07:11

from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model("video", "Video")
    for row in MyModel.objects.all():
        row.video_uuid = uuid.uuid4()
        row.save(update_fields=["video_uuid"])


class Migration(migrations.Migration):

    dependencies = [
        ("video", "0004_add_uuid_field"),
    ]

    operations = [
        migrations.RunPython(gen_uuid),
    ]
