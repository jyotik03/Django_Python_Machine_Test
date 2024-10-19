# models.py
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_clients', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_projects')
    def __str__(self):
        return self.project_name
