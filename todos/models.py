from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)

    # Class-level attribute to keep track of completed todos
    completed_count = 0

    def __str__(self):
        return self.title

    @classmethod
    def increment_completed_count(cls):
        cls.completed_count += 1
