from django.db import models
import os

class Tasks(models.Model):
    class Meta:
        db_table = 'tasks'

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True)
    module = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    st_date = models.DateField(("Starting Date"),blank=True)
    ed_date = models.DateField(("Ending Date"),blank=True)
    status = models.CharField(max_length=100, blank=True)