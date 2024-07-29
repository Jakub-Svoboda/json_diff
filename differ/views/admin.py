from rest_framework import generics, status
from rest_framework.response import Response


class DiffView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        response_data = {}

        return Response(response_data, status=status.HTTP_200_OK)
