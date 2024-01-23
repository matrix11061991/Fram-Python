# my_app/urls.py
from django.urls import path
from .views import home, user_login, profile_edit

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]
