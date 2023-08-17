from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', BlogView)


urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path('post/add/', BlogCreateView.as_view(), name="add"),
    path("post/delete/<int:pk>/", BlogDeleteView.as_view(), name="delete"),
    path("post/edit/<int:pk>/", BlogUpdateView.as_view(), name="edit"),
    path("post/one/", some, name="one"),
    path("api/", include(router.urls), name="api")
]