from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers
from django.shortcuts import get_object_or_404


@api_view(http_method_names=['GET', 'POST'])
def task_api(request):
    if request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(serializer.errors)

    if request.method == 'GET':
        employees = Task.objects.all()
        serializer = TaskSerializers(employees, many=True)
        return Response(data=serializer.data)


@api_view(http_method_names=['GET', 'PUT', 'PATCH', 'DELETE'])
def task_details_api(request, pk=None):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'GET':
        serializers = TaskSerializers(task)
        return Response(data=serializers.data, status=200)

    if request.method == 'DELETE':
        task.delete()
        return Response(data=None, status=204)

    if request.method == 'PUT':
        serializer = TaskSerializers(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

    if request.method == 'PATCH':
        serializer = TaskSerializers(data=request.data, instance=task, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=205)
        return Response(data=serializer.errors, status=400)




