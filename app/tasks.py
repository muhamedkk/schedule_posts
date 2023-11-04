
# from demoapp.models import Widget
# from django.utils import timezone as t
from celery import shared_task ,app
from .models import *

import pytz
from pytz import timezone 
from datetime import datetime

@shared_task
def update_posts_time():

    utc_now = datetime.utcnow()
    utc = pytz.timezone('UTC')
    aware_date = utc.localize(utc_now)
    turkey = timezone('Europe/Istanbul')
    now_turkey = aware_date.astimezone(turkey)
    # current_datetime = t.now()

    print(now_turkey)
    # print(current_datetime)
    print(Post.objects.filter(scheduled_time__lte=now_turkey))
    posts = Post.objects.filter(scheduled_time__lte=now_turkey,is_published = False).update(is_published=True)
    return 'success'
