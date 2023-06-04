from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet
from skymarket import settings

# TODO настройка роутов для модели

urlpatterns = []
ads_router = SimpleRouter()

ads_router.register('', AdViewSet)

urlpatterns += ads_router.urls
