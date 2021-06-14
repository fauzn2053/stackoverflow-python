from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import  AllowAny
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .throtling import UserDayThrottle, UserMinThrottle
from .pagination import get_paginated_data

# Create your views here.

BASE_URL="http://127.0.0.1:8000"

# .................................................................................
# Stackoverflow API Views
# .................................................................................

class StackoverflowSearchAPIView(APIView): 
    """
    API View for Banner listing
    """
    permission_classes = (AllowAny,)
    throttle_classes = [
          UserMinThrottle,
          UserDayThrottle
     ]

    @method_decorator(cache_page(60*5))
    def get(self, request, format=None):
        q=request.GET['q']
        page = request.GET.get("page","")
        request_data =f"https://api.stackexchange.com/2.2/search?key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow&order=desc&sort=activity&intitle={q}&page={page}&filter=default"
        response = requests.get(request_data)
        result=get_paginated_data(response.json().get("items"), f"{BASE_URL}/api/v1/search/?q={q}", request)

        return Response({
                    "status": True,
                    "code" : status.HTTP_200_OK,
                    "message" : "Detail fetched successfully",
                    "data": result,
                    }, status=status.HTTP_200_OK)
