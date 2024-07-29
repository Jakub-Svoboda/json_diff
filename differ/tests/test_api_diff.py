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
