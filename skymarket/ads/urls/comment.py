from django.urls import path

import ads.views
from rest_framework import routers

urlpatterns = []

router = routers.SimpleRouter()
router.register('comments', ads.views.CommentViewSet)
urlpatterns += router.urls
