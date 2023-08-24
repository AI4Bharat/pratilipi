import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
celery_app = Celery(
    "backend",
    accept_content=["application/json"],
    result_serializer="json",
    task_serializer="json",
    worker_prefetch_multiplier=0,
)
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Celery Queue related settings
celery_app.conf.task_default_queue = "default"
celery_app.conf.task_routes = {"task.tasks.celery_asr_call": {"queue": "asr_tts"}}
celery_app.conf.task_routes = {"task.tasks.celery_tts_call": {"queue": "asr_tts"}}
celery_app.conf.task_routes = {"task.tasks.celery_nmt_call": {"queue": "nmt"}}
# celery_app.conf.task_routes = {"task.tasks.*": {"queue": "asr_tts"}}
celery_app.conf.task_routes = {"transcript.tasks.*": {"queue": "ytt"}}

celery_app.conf.beat_schedule = {
    "Send_mail_to_managers_completed": {
        "task": "send_completed_tasks_mail",
        "schedule": crontab(minute=0, hour="*/6"),  # execute 4 times in a day
    },
    "Send_mail_to_managers_new": {
        "task": "send_new_tasks_mail",
        "schedule": crontab(minute=0, hour=1),  # execute everyday at 1 am
    },
}

celery_app.autodiscover_tasks()
