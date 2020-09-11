from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from datetime import timedelta, datetime

from .models import TimeStart, Task, Sum, IN_PROGRESS, DONE, SALARY_PER_HOUR

@receiver(post_save, sender=Task)
def create_timestamp_for_inprogress(sender, instance, **kwargs):
    if instance.status == IN_PROGRESS:
        TimeStart.objects.create(task=instance)
    return

@receiver(post_save, sender=Task)
def create_sum_for_done(sender, instance, **kwargs):
    if instance.status == DONE:
        delta = datetime.now() - instance.timestart.start_time
        Sum.objects.create(sum=SALARY_PER_HOUR*(delta.seconds // 3600))
    return

@receiver(post_save, sender=Task)
def delete_timestamp_for_done(sender, instance, **kwargs):
    if instance.status == DONE:
        instance.timestamp.delete()
    return