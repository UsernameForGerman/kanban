from rest_framework.serializers import ModelSerializer, SerializerMethodField
from datetime import datetime

from .models import Task, IN_PROGRESS, DONE, TODO

class TaskSerializer(ModelSerializer):
    start_time = SerializerMethodField(read_only=True, allow_null=True)
    sum = SerializerMethodField(read_only=True, allow_null=True)

    class Meta:
        model = Task
        fields = ('name', 'status', 'start_time', 'sum')

    # TODO: fix to return text of the error
    # TODO: fix to pass updates of the status
    def is_valid(self, raise_exception=False):
        valid = super().is_valid()
        if valid:
            if self.validated_data['status'] != 0:
                # self.errors['status'] = f'Can not create task with status {self.validated_data["status"]}'
                # print(self.errors)
                return False
        else:
            return False

        return not bool(self.errors)

    # def get_status(self, task):
    #     return task.status

    def get_start_time(self, task):
        if not hasattr(task, 'timestart'):
            return None
        delta = datetime.now() - task.timestart.start_time
        hh = delta.seconds // 3600
        mm = delta.seconds % 3600 // 60
        ss = delta.seconds % 3600
        return f'{hh}:{mm}:{ss}' if task.status == IN_PROGRESS else ''

    def get_sum(self, task):
        if not hasattr(task, 'sum'):
            return None
        return task.sum.sum if task.status == DONE else ''

