from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from task_manager import views
import dotenv
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main_page.html'), name='main_page'),

    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),

    path('users/', views.UsersDetailView.as_view(), name='users'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='update_user'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete_user'),
    path('users/create/', views.UserSignUpView.as_view(), name='registration'),

    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
]

dotenv.load_dotenv('.env')
if os.environ.get('GUNICORN_STATIC'):
    urlpatterns += staticfiles_urlpatterns()
