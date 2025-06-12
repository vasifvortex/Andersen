from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    first_name = models.CharField()
    last_name = models.TextField(null=True, blank=True)
    username = models.CharField(unique=True)
    password = models.CharField(validators=[MinLengthValidator(6)])

    def __str__(self):
        return self.username
    

class Task(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    title = models.CharField()
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=Status.choices,default=Status.NEW)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title