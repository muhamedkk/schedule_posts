from django.shortcuts import render ,get_object_or_404
from .models import *

def authorization(view_func):
    def wrapper(request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['pk'])
        author_of_post = post.author.id
        if  request.user.is_anonymous or request.user.id != author_of_post:
            return render(request, 'error_response_pages/403.html')
        response = view_func(request,*args, **kwargs)
        return response
    return wrapper