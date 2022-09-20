from django.db import models
import uuid 

class Video(models.Model):
    """
    Model for the Video object.
    """

    video_uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        verbose_name="Video UUID",
        primary_key=False, 
    )
    name = models.CharField(max_length=255, verbose_name="Video Name")
    url = models.URLField(unique=True, verbose_name="Video URL", db_index=True)
    duration = models.DurationField(verbose_name="Video Duration")
    subtitles = models.JSONField(verbose_name="Subtitles", null=True, blank=True)

    def __str__(self):
        return str(self.video_uuid) + " : " + self.name
