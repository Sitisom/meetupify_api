from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from core.models import User
from core.serializers import UserSerializer


class UserViewSet(GenericViewSet, ListModelMixin):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all(is_active=True)

    @action(['POST'], detail=True, url_path='add-friend')
    def add_friend(self, *args, **kwargs):
        user = self.request.user
        obj = self.get_object()
        user.friends.add(obj)