# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer, CreateProjectSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the user who created the client
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def add_project(self, request, pk=None):
        client = get_object_or_404(Client, pk=pk)
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save(client=client)
            project.users.set(serializer.validated_data['users'])
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def assigned_projects(self, request):
        user = request.user
        projects = user.projects.all()  # Projects assigned to the logged-in user
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
