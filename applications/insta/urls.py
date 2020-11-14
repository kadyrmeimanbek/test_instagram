from django.urls import path
from .views import (index, get_all_posts, get_details, create_app_form, success_message, new_application_form)

urlpatterns = [
    path('', index, ),
    path('application-form/create/', create_app_form, name='app_form'),
    path('application-form/success/', success_message, name='success_msg'),
    path('posts/', get_all_posts, name='posts'),
    path('posts/<int:id>/', get_details, name='post_detail'),
    path('new-app-form/', new_application_form, name='new_form')
]