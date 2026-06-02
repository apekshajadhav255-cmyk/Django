from django.db import models

# Create your models here.
class TaskModel(models.Model):#consist of task to be done
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)

#Once the task has been performed before delete it from TaskModel i need to store it in another model CompleteModel

class CompleteModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)

class TrashModel(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)