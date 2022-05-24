from rest_framework import serializers

from core.models import User


class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', 'phone')


class UserSerializer(serializers.ModelSerializer):
    friends = FriendsSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
