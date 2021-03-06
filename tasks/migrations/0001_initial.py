# Generated by Django 3.1.1 on 2020-09-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name of the task')),
                ('status', models.CharField(choices=[(0, 'To Do'), (1, 'In Progress'), (2, 'Done')], max_length=16, verbose_name='Status of the task')),
            ],
        ),
        migrations.CreateModel(
            name='Sum',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tasks.task')),
                ('sum', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TimeStart',
            fields=[
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tasks.task')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
