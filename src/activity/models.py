from email.policy import default
from uuid import uuid4

from django.db import models
from django.db.models.fields import UUIDField

class Activity(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    user = models.UUIDField(db_index=True, null=False)
    project = models.UUIDField(db_index=True, null=False)
    rule = models.UUIDField(db_index=True, null=True)
    payment = models.UUIDField(db_index=True, null=True)
    project_name = models.CharField(max_length=60, null=True, default=None)
    rule_name = models.CharField(max_length=60, null=True, default=None)
    amount = models.DecimalField(max_digits=12, decimal_places=2, default=None, null=True)
    title = models.CharField(max_length=200, null=True, default=None)
    message = models.CharField(max_length=300, null=True, default=None)
    footer = models.CharField(max_length=200, null=True, default=None)
    rule_icon = models.CharField(max_length=60, null=True, default=None)
    created_at = models.DateTimeField(auto_now=True)
    # indica el tipo de actividad
    ACTIVITY_TYPE_CHOICES = [
        ('E', 'Event'),
        ('S', 'Saving'),
    ]
    activity_type = models.CharField(default=None, null=True, max_length=1, choices=ACTIVITY_TYPE_CHOICES)

    class Meta:

        managed = True
        db_table = 'activities'
