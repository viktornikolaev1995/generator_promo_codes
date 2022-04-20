from django.urls import path
from .views import GroupListCreateAPIView

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view(), name='retrieve_create_groups')
]
