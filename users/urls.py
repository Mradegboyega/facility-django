from django.urls import path
from . import views

urlpatterns = [
    path('user_home/', views.index, name='user_home'),
    path('greet/', views.greet, name='greet_user')
]