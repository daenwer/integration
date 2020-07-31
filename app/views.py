from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework import status


class ConnectionView(View):
    def post(self, request, *args, **kwargs):
        a = 123
        return Response({'logs': a}, status=status.HTTP_200_OK)

    def get(self, request):
        a = 123
        return Response({'logs': a}, status=status.HTTP_200_OK)
