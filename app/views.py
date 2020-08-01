from django.views import View
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from app.slack import *


# TODO: тестовый класс, удалить в конце
class ConnectionView(View):

    def post(self, request, *args, **kwargs):
        a = 123
        return Response(status=status.HTTP_200_OK)

    def get(self, request):
        a = 123
        return Response(status=status.HTTP_200_OK)


class SlackView(View):

    def post(self, request, *args, **kwargs):
        data = {"status": 200}
        requests.post(url=request.POST.get('response_url'), json=data)
        command = request.POST.get('command')[1:]
        message = request.POST.get('text')
        user_name = request.POST.get('user_name')
        eval(f'{command}("{message}")')
        return JsonResponse({'text': f'{user_name} created new task'}, status=200)
