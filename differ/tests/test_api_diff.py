from rest_framework import status

from differ.tests.BaseApiTestCase import BaseAPITestCase


class TestApiDiff(BaseAPITestCase):

    def test_diff_response_code(self):
        data = {
            "left_text": "hello",
            "right_text": "world"
        }
        res = self.client.post("/api-admin/v1/diff/", data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_diff_validity(self):
        data = {
            "left_text": '{"abc": 1}',
            "right_text": '"word"word'
        }
        res = self.client.post("/api-admin/v1/diff/", data, "json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["validity"]["left"], True)
        self.assertEqual(res.data["validity"]["right"], False)
