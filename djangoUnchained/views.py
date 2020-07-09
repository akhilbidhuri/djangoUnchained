from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse


def error_page(request, exception):
    return JsonResponse({'error': 'Not Found'}, status=404)