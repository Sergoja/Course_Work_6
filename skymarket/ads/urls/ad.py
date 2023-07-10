from django.urls import path, include
from rest_framework.routers import SimpleRouter

import ads
from ads.views import AdUploadImageView, AdViewSet
from rest_framework import routers

router = SimpleRouter()
router.register('ads', AdViewSet, basename="ads")

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/upload_image/', ads.views.AdUploadImageView.as_view()),
    path('<int:pk>/', include('ads.urls.comment'))
]

