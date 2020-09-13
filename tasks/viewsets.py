from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

class TasksViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=self.request.data)
        if serializer.is_valid():
            task = get_object_or_404(Task, id=self.kwargs['id'])
            serializer.update(task, serializer.validated_data)
            return Response(serializer.validated_data, HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



