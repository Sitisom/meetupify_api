from rest_framework.serializers import ModelSerializer

from party.models import Invite, Group


class GroupModelSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class InviteModelSerializer(ModelSerializer):
    class Meta:
        model = Invite
        fields = '__all__'
