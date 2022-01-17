from django.urls import path
from statuses.views import StatusesListView, StatusUpdateView, StatusCreateView, StatusDeleteView

urlpatterns = [
    path('', StatusesListView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create_status'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='update_status'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete_status'),
]
