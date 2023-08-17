from django.urls import path, include
from .views import *
urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path('post/add/', BlogCreateView.as_view(), name="add"),
    path("post/delete/<int:pk>/", BlogDeleteView.as_view(), name="delete"),
    path("post/edit/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
]