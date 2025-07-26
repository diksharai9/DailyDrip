from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'PATCH':
        try:
            task = Task.objects.get(id=task_id)
            data = json.loads(request.body)
            task.completed = data.get("completed", task.completed)
            task.save()
            return JsonResponse({"id": task.id, "completed": task.completed})
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)
    return JsonResponse({"error": "Invalid request"}, status=400)