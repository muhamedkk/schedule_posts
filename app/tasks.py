
# from demoapp.models import Widget
from django.utils import timezone
from celery import shared_task ,app
from .models import *
from datetime import datetime

@shared_task
def update_posts_time():
    current_datetime = timezone.now()
    posts = Post.objects.filter(scheduled_time__lte=current_datetime,is_published = False).update(is_published=True)
