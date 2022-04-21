from django.urls import path
from .views import GroupListCreateAPIView, GroupPartialUpdateAPIView, GroupDestroyAPIView

urlpatterns = [
    path('create-retrieve-groups/', GroupListCreateAPIView.as_view(), name='retrieve_create_groups'),
    path('partial-update-groups/', GroupPartialUpdateAPIView.as_view(), name='partial_update_groups'),
    path('delete-groups/', GroupDestroyAPIView.as_view(), name='delete_groups')
]