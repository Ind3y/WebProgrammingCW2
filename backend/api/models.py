from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Steps(models.Model):
    task = models.ForeignKey(Tasks, related_name='steps', on_delete=models.CASCADE)
    decription = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)