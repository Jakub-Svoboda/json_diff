from django.urls import include, path
from rest_framework.routers import DefaultRouter

import differ.views.admin as v

app_name = "search-admin"

router = DefaultRouter(trailing_slash=False)
router.register("", v.DiffView, basename="diff")

urlpatterns = [
    path("/", include(router.urls)),
]
