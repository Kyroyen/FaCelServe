import os
from dotenv import load_dotenv
from celery import Celery

load_dotenv()

BROKER_URI = os.environ.get("BROKER_URI")
BACKEND_URI = os.environ.get("BACKEND_URI")

app = Celery(
    "celery_app",
    broker = BROKER_URI,
    backend = BACKEND_URI,
    include = ["celery_task_app.tasks"]
)

app.conf.update(
    task_serializer="pickle",
    result_serializer="json",
    accept_content=["json", "pickle"]
)

