from django.db import models
from ordered_model.models import OrderedModel


class Task(OrderedModel):
    STATUS = (
        ('in progress', 'In Progress'),
        ('finished', 'Finished')
    )
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
