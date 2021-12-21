from django.contrib import admin
from django.urls import path
from . import views
import dotenv
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='main_page'),
    path('users/', views.users, name='users'),
    path('users/create', views.registration, name='registration'),
    path('users/<int:pk>/update/', views.update_user, name='update_user'),
    path('users/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

dotenv.load_dotenv('local.env')
if os.environ.get('GUNICORN_STATIC'):
    urlpatterns += staticfiles_urlpatterns()
