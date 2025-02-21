from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration_api_view),
    path('login/', views.authorization_api_view),
    path('confirm/', views.confirm_user_api_view),
]