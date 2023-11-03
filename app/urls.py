from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [    
               
    # Home Page
    path('' , views.index,name='index'),
    
    # profile
    path('profile' , views.profile,name='profile'),
    
    # Authentication
    path('authentication/login' , views._login,name='login'),
    path('authentication/signup' , views.signup,name='signup'),
    path('authentication/_logout' , views._logout,name='_logout'),
    
    # Post Delete And Edit
    path('post/edit/<int:pk>/' , views.edit_post,name='edit_post'),
    path('post/delete/<int:pk>/' , views.delete_post,name='delete_post'),
    
    
    
    ]
 