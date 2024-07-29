from django.urls import include, path

import differ.views.admin as v

app_name = "differ"

urlpatterns = [
    path("", v.DiffView.as_view(), name="diff"),
]
