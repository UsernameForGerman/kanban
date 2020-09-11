from rest_framework.serializers import ModelSerializer, SerializerMethodField
from datetime import datetime

from .models import Task, IN_PROGRESS, DONE

class TaskSerializer(ModelSerializer):
    start_time = SerializerMethodField(allow_null=True)
    sum = SerializerMethodField(allow_null=True)

    class Meta:
        model = Task
        fields = ('name', 'status', 'start_time', 'sum')

    def is_valid(self, raise_exception=False):
        valid = super().is_valid()
        if valid:
            if self.start_time is not None:
                self.errors['start_time'] = 'Can not set start time'
                return False
            if self.sum is not None:
                self.errors['sum'] = 'Can not set sum'
                return False
        else:
            return False

        return not bool(self.errors)


    def get_start_time(self, task):
        delta = datetime.now() - task.timestart.start_time
        hh = delta.seconds // 3600
        mm = delta.seconds % 3600 // 60
        ss = delta.seconds % 3600
        return f'{hh}:{mm}:{ss}' if task.status == IN_PROGRESS else ''

    def get_sum(self, task):
        return task.sum.sum if task.status == DONE else ''

