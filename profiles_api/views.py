from rest_framework.views import APIView
from rest_framework.response import Response


class ImageApiView(APIView):
    """ API View For Working With Images """

    def get(self, request, format=None):
        """Returns list of images names"""
        an_apiView = [
            'image1',
            'image2',
            'image3'
        ]
        return Response({'images': an_apiView})
