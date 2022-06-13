from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from party.filters import GroupFilterSet
from party.models import Invite, Group
from party.serializers import InviteModelSerializer, GroupModelSerializer


class GroupViewSet(GenericViewSet, ListModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = GroupModelSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = GroupFilterSet

    def get_queryset(self):
        return Group.objects.filter(users=self.request.user, is_active=True)

    @action(['GET'], False)
    def all(self, request, *args, **kwargs):
        qs = Group.objects.filter(is_active=True)
        return self.serializer_class(qs, many=True)


class InviteViewSet(GenericViewSet, ListModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = InviteModelSerializer

    def get_queryset(self):
        user = self.request.user
        return Invite.objects.filter(receiver=user, is_active=True)

    @action(['GET'], False)
    def sent_invites(self, request, *args, **kwargs):
        user = self.request.user
        qs = Invite.objects.filter(sender=user)
        return self.serializer_class(qs, many=True)
