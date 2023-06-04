from django.urls import include, path
from rest_framework import routers

from rest_framework.routers import SimpleRouter

from users.views import UserViewSet, UserUploadImageView

urlpatterns = [
    path('<int:pk>/upload_image/', UserUploadImageView.as_view())
]

router = routers.SimpleRouter()
router.register('', UserViewSet)
urlpatterns += router.urls

