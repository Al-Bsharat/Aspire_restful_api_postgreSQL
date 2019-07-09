from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = permissions.UpdateOwnProfile


class ImageApiView(APIView):
    """ API View For Working With Images """
    serializer_class = serializers.ImagesSerializer

    an_api_view = [
        'image1',
        'image2',
        'image3'
    ]

    def get(self, request, format=None):
        """Returns list of images names"""
        return Response({'images': self.an_api_view})

    def post(self, request):
        """Add New Image Name"""
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        img_name = serializer.validated_data['image_name']
        serializer.save()

        self.an_api_view.append(img_name)
        return Response(
            {'message': f'Image {img_name}, was added.'},
            status=status.HTTP_201_CREATED
        )

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'method': 'Put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        img_name = serializer.validated_data['image_name']
        self.an_api_view.remove(img_name)
        return Response({'message': f'{img_name} Deleted successfully'})


class ImageViewSet(viewsets.ViewSet):
    """ ViewSet For Working With Images """

    serializer_class = serializers.ImagesSerializer

    an_api_view = [
        'image1',
        'image2',
        'image3'
    ]

    def list(self, request):
        """Return all images stored on server"""
        return Response({'images': self.an_api_view})

    def create(self, request):
        """Create new image"""
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        img_name = serializer.validated_data['image_name']
        self.an_api_view.append(img_name)
        return Response({'message': f'Image {img_name} created.'})

    def retrieve(self, request, pk=None):
        """Handle getting object by its ID"""
        if pk and self.an_api_view[pk]:
            pk = int(pk)
            return Response({'image': self.an_api_view[pk]})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'message': 'Update (PUT)'})

    def partial_update(self, request, pk=None):
        """Handle update part of an object"""
        return Response({'message': 'Partial Update (PATCH)'})

    def destroy(self, request, pk=None):
        """Handle remove an object"""
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        img_name = serializer.validated_data['image_name']
        self.an_api_view.remove(img_name)
        return Response({'message': f'{img_name} Destroyed'})
