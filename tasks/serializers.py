from django.utils.timezone import now, datetime

from rest_framework.serializers import ModelSerializer, SerializerMethodField
from datetime import datetime

from .models import Task, IN_PROGRESS, DONE, TODO

class TaskSerializer(ModelSerializer):
    start_time = SerializerMethodField(read_only=True, allow_null=True)
    sum = SerializerMethodField(read_only=True, allow_null=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'start_time', 'sum')

    # def is_valid(self, raise_exception=False):
    #     valid = super().is_valid()
    #     if valid:
    #         if self.validated_data['status'] != 0:
    #             # self.errors['status'] = f'Can not create task with status {self.validated_data["status"]}'
    #             # print(self.errors)
    #             return False
    #     else:
    #         return False
    #
    #     return not bool(self.errors)

    # def get_status(self, task):
    #     return task.status

    def get_start_time(self, task):
        if not hasattr(task, 'timestart'):
            return None
        delta = now() - task.timestart.start_time
        hh = delta.seconds // 3600
        mm = delta.seconds % 3600 // 60
        ss = delta.seconds % 3600 % 60
        return f'{hh}:{mm}:{ss}' if task.get_status_display() == IN_PROGRESS else None

    def get_sum(self, task):
        if not hasattr(task, 'sum'):
            return None
        return task.sum.sum if task.get_status_display() == DONE else None

