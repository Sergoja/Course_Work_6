from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserUploadImageView(UpdateView):
    model = User
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "email": self.object.email,
            "role": self.object.role,
            "image": self.object.image.url,
        })


