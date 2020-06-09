from django.urls import path
from .views import Login, Register, CreatePost, Dashboard

app_name = 'user'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('create/', CreatePost.as_view(), name='create_post'),
]