from django.urls import include, path
from rest_framework import routers

from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, UserUploadImageView

users_router = SimpleRouter()

users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path('<int:pk>/upload_image/', UserUploadImageView.as_view())
]
