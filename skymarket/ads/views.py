from django.http import JsonResponse
from django.views.generic import UpdateView
from rest_framework import pagination, viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ads.models import Ad, Comment
# from ads.permissions import IsOwner, IsStaff
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permissions = {
        'retrieve': [IsAuthenticated],
        # 'update': [IsAuthenticated, IsOwner | IsStaff],
        # 'partial_update': [IsAuthenticated, IsOwner | IsStaff],
        # 'destroy': [IsAuthenticated, IsOwner | IsStaff]
    }
    default_permission = [AllowAny]

    # def get_permissions(self):
    #     return [permission() for permission in self.permissions.get(self.action, self.default_permission)]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        user = request.data
        self.queryset = self.queryset.filter(author_id=user['id'])
        return super().list(request, *args, **kwargs)


class AdUploadImageView(UpdateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
            "pk": self.object.pk,
            "title": self.object.title,
            "author": self.object.author.username,
            "description": self.object.description,
            "price": self.object.price,
            "created_at": self.object.created_at,
            "image": self.object.image.url,
        })


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad = self.kwargs.get("ad_pk")
        serializer.save(ad=ad)

    def get_queryset(self):
        pass
