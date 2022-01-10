from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='add_task'),
    path('<int:pk>/', views.TasksListView.as_view(), name='view_task'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete/', views.TasksListView.as_view(), name='delete_task'),
]