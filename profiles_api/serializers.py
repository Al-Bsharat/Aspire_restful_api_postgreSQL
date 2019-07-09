from rest_framework import serializers


class ImagesSerializer(serializers.Serializer):
    """Serializer for ImageApiView"""

    image_name = serializers.CharField(max_length=20)
