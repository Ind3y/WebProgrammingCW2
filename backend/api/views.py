from django.shortcuts import render
from django.http import JsonResponse

from .models import to_Do


def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })

def toDo_api_view(request):
    toDo = to_Do.objects.all()
    return JsonResponse({
        'toDos': list(toDo.values())
    })
