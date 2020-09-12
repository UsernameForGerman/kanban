from django.urls import reverse, resolve

import pytest

from tasks.models import Task

class TestListDetailTaskUrls:

    @pytest.fixture
    def task(self):
        return Task(id=1, name='test', status=1)

    def test_detail_task_url(self, task: Task):
        assert(
            reverse("tasks:task-detail", kwargs={"id": task.id}) == f"/api/v1/tasks/{task.id}/"
        )
        assert resolve(f"/api/v1/tasks/{task.id}/").view_name == "tasks:task-detail"

    def test_list_task_url(self):
        assert reverse("tasks:task-list") == "/api/v1/tasks/"
        assert resolve("/api/v1/tasks/").view_name == "tasks:task-list"

