
from django.urls import path
from.views import StackoverflowSearchAPIView

urlpatterns = [
    path("search/",StackoverflowSearchAPIView.as_view(), name="search")
]
