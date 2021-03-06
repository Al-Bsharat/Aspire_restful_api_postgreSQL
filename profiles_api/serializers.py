from rest_framework import serializers
from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return new user."""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    user_email = serializers.ReadOnlyField(source='user_profile.email')

    class Meta:
        model = models.ProfileFeedItem
        fields = ['id', 'user_email', 'status_text', 'created_on']
        extra_kwargs = {
            'created_on': {'read_only': True}
        }


class ImagesSerializer(serializers.Serializer):
    """Serializer for ImageApiView"""

    image_name = serializers.CharField(max_length=20)
