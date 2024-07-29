from deepdiff import DeepDiff
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):
    def assertJsonDeepEqual(self, first, second, **kwargs):
        diff = DeepDiff(second, first, **kwargs)
        if diff:
            raise AssertionError(diff)
