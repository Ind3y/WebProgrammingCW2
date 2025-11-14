from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Tasks, Steps


def tasks_api(request):
    tasks = Tasks.objects.all()
    steps = Steps.objects.all()
    return JsonResponse({
        'tasks': [
            {
                'id': task.id,
                'title': task.title,
                'due_date': task.due_date,
                'completed': task.completed,
                'notes':task.notes
            }
            for task in tasks
        ],
        'steps': [
            {
                'id': step.id,
                'task_id': step.task.id,
                'description': step.description,
                'completed': step.completed
            }
            for step in steps
        ],
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
    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.completed = data['completed']
        task.save()
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'due_date': task.due_date,
            'completed': task.completed}) 

    return JsonResponse({
        'id': task.id,
        'title': task.title,
        'due_date': task.due_date,
        'completed': task.completed
    })  

@csrf_exempt
def create_task_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '')
        due_date = data.get('due_date', None)

        task = Tasks.objects.create(title=title, due_date=due_date)

    return JsonResponse({
        'id': task.id,
        'title': task.title,
        'due_date': task.due_date,
        'completed': task.completed
    })
    
@csrf_exempt
def update_task_api(request, task_id):
    try:
        task = Tasks.objects.get(id=task_id)
    except Tasks.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        task.title = data.get('title', task.title)
        due_date = data.get('due_date', task.due_date)
        if due_date == '':
            task.due_date = None
        else:
            task.due_date = due_date

        note = data.get('note', None)
        if note == '':
            task.notes = None
        else:
            task.notes = note
        

        task.completed = data.get('completed', task.completed)
        task.save()
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'due_date': task.due_date,
            'completed': task.completed,
            'notes': task.notes
        })

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def create_step_api(request, task_id):
    try:
        task = Tasks.objects.get(id=task_id)
    except Tasks.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'POST':
        data = json.loads(request.body)
        description = data.get('description', '')

        step = Steps.objects.create(task=task, description=description)

    return JsonResponse({
        'id': step.id,
        'task_id': step.task.id,
        'description': step.description,
        'completed': step.completed
    })

@csrf_exempt
def step_api(request, step_id):
    try:
        step = Steps.objects.get(id=step_id)
    except Steps.DoesNotExist:
        return JsonResponse({'error': 'Step not found'}, status=404)

    if request.method == 'DELETE':
        step.delete()
        return JsonResponse({'message': 'Step deleted successfully'})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        step.completed = data.get('completed', step.completed)
        step.save()
        return JsonResponse({
            'id': step.id,
            'task_id': step.task.id,
            'description': step.description,
            'completed': step.completed
        })
    return JsonResponse({'message': 'Invalid request method'}, status=400)  

        
