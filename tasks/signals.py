from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.timezone import now, datetime

from datetime import timedelta, datetime

from .models import TimeStart, Task, Sum, IN_PROGRESS, DONE, SALARY_PER_HOUR

@receiver(post_save, sender=Task)
def create_timestamp_for_inprogress(sender, instance, **kwargs):
    if instance.get_status_display() == IN_PROGRESS:
        if not hasattr(instance, 'timestart'):
            TimeStart.objects.create(task=instance)
    return

@receiver(post_save, sender=Task)
def create_sum_for_done(sender, instance, **kwargs):
    if instance.get_status_display() == DONE:
        if hasattr(instance, 'timestart'):
            delta = now() - instance.timestart.start_time
        else:
            delta = timedelta(0)

        if not hasattr(instance, 'sum'):
            Sum.objects.create(task=instance, sum=SALARY_PER_HOUR / 3600 * delta.seconds)
    return

@receiver(post_save, sender=Task)
def delete_timestamp_for_done(sender, instance, **kwargs):
    if instance.get_status_display() == DONE and hasattr(instance, 'timestamp'):
        instance.timestamp.delete()
    return