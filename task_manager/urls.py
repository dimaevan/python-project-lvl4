from django.contrib import admin
from django.urls import path, include
from task_manager import views
import dotenv
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='main_page'),
    path('statuses/', include('statuses.urls')),

    path('users/', views.UsersDetailView.as_view(), name='users'),
    path('users/<int:pk>/update/', views.update_user, name='update_user'),
    path('users/<int:pk>/delete/', views.delete_user, name='delete_user'),
    path('users/create', views.RegisterView.as_view(), name='registration'),

    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
]

dotenv.load_dotenv('local.env')
if os.environ.get('GUNICORN_STATIC'):
    urlpatterns += staticfiles_urlpatterns()
