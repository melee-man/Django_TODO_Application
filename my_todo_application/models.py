from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.status_name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    task_name = models.CharField(max_length = 100)
    task_status = models.ForeignKey(Status, on_delete = models.CASCADE)
    due_date =  models.DateField()

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):
        return reverse('user_dashboard')

