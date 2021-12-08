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
]

dotenv.load_dotenv('local.env')
if os.environ.get('GUNICORN_STATIC'):
    urlpatterns += staticfiles_urlpatterns()
