from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from differ.JsonValidator import is_valid_json


class DiffView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        left_text = data.get("left_text", "")
        right_text = data.get("right_text", "")

        response_data = {
            "validity": {
                "left": is_valid_json(left_text),
                "right": is_valid_json(right_text)
            },
            "left_text": left_text,
            "right_text": right_text
        }


        return Response(response_data, status=status.HTTP_200_OK)
