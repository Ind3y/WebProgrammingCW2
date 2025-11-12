from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Tasks


def tasks_api(request):
    tasks = Tasks.objects.all()
    return JsonResponse({
        'tasks': [
            {
                'id': task.id,
                'title': task.title,
                'completed': task.completed
            }
            for task in tasks
        ]
    })


@csrf_exempt
def task_api(request, task_id):
    try:
        task = Tasks.objects.get(id=task_id)
    except Tasks.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data['completed'])
        task.completed = data['completed']
        task.save()



    return JsonResponse({
        'id': task.id,
        'title': task.title,
        'completed': task.completed
    })  