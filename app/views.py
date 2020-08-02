from django.views import View
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from app.slack_api import *


class SlackView(View):

    def post(self, request, *args, **kwargs):
        data = {"status": 200}
        requests.post(url=request.POST.get('response_url'), json=data)
        command = request.POST.get('command')[1:]
        message = request.POST.get('text')
        user_name = request.POST.get('user_name')
        if command in ALLOWED_COMMANDS:
            number_task = eval(f'{command}("{message}")')
            return JsonResponse({'text': f'{user_name} created new task {number_task}'}, status=200)
        return JsonResponse({'error': f'add the {command} to the list allowed commands'}, status=404)
