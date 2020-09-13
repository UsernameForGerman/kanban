import pytest
from django.urls import reverse

from rest_framework.test import APIRequestFactory

from tasks.viewsets import TasksViewSet
from tasks.models import Task, TODO, IN_PROGRESS, DONE
from tasks.serializers import TaskSerializer

@pytest.fixture
def task():
    return Task.objects.create(name='test')

class TestTasksViewSet:

    factory = APIRequestFactory()

    @pytest.mark.django_db
    def test_retrieve_task(self, task: Task):
        path = reverse('tasks:task-detail', kwargs={'id': task.id})
        request = self.factory.get(path)
        response = TasksViewSet.as_view({'get': 'retrieve'})(request, id=task.id)

        assert response.status_code == 200
        assert response.data == TaskSerializer(task).data

    @pytest.mark.django_db
    def test_list_tasks(self):
        path = reverse('tasks:task-list')
        request = self.factory.get(path)
        response = TasksViewSet.as_view({'get': 'list'})(request)

        assert response.status_code == 200

    @pytest.mark.django_db
    @pytest.mark.parametrize('name, status, response_status', [
        ('name', TODO, 201),
        ('name', IN_PROGRESS, 201),
        ('name', DONE, 201),
        ('name', None, 201),
        ('name' * 10 ** 3, TODO, 400),
        (None, DONE, 400),
    ])
    def test_success_create_task(self, name: str, status: str, response_status: int):
        path = reverse('tasks:task-list')

        data = dict()
        if name:
            data['name'] = name
        if status:
            data['status'] = status

        request = self.factory.post(path, data=data)
        response = TasksViewSet.as_view({'post': 'create'})(request)

        assert response.status_code == response_status

    @pytest.mark.django_db
    @pytest.mark.parametrize('field, value', [
        ('status', TODO),
        ('status', IN_PROGRESS),
        ('status', DONE),
    ])
    def test_success_update_task(self, task: Task, field: str, value: str):
        path = reverse('tasks:task-detail', kwargs={'id': task.id})
        request = self.factory.put(path, data={
            'id': task.id,
            'name': task.name,
            field: value,
        })
        response = TasksViewSet.as_view({'put': 'update'})(request, id=task.id)

        assert response.status_code == 200

    @pytest.mark.django_db
    @pytest.mark.parametrize('field, value', [
        ('name', 'name'*10**3),
    ])
    def test_failed_update_task(self, task: Task, field: str, value: str):
        path = reverse('tasks:task-detail', kwargs={'id': task.id})
        request = self.factory.put(path, data={
            'id': task.id,
            field: value,
        })
        response = TasksViewSet.as_view({'put': 'update'})(request, id=task.id)

        assert response.status_code == 400
