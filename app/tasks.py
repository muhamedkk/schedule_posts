
# from demoapp.models import Widget
from django.utils import timezone as t
from datetime import timedelta
from celery import shared_task ,app
from .models import *

import pytz
from pytz import timezone 
from datetime import datetime

@shared_task
def update_posts_time():
    current_datetime = t.now() + timedelta(hours=3)
    posts = Post.objects.filter(scheduled_time__lte=current_datetime,is_published = False).update(is_published=True)
    return 'success'
