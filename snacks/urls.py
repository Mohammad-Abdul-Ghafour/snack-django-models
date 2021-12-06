from django.urls import path
from .views import SnackDetailView , SnackListView

urlpatterns = [
    path('',SnackListView.as_view(), name='snackList'),
    path('<int:pk>',SnackDetailView.as_view(),name='snackDetail')
]