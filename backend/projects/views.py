from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from .models import Project
from .serializers import ProjectSerializer, ProjectListSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Project instances.

    Provides CRUD operations:
    - GET /api/projects/ - List all projects
    - POST /api/projects/ - Create a new project
    - GET /api/projects/{id}/ - Retrieve a specific project
    - PUT /api/projects/{id}/ - Update a project
    - PATCH /api/projects/{id}/ - Partial update a project
    - DELETE /api/projects/{id}/ - Delete a project
    """
    queryset = Project.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'technologies', 'project_type']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']

    def get_serializer_class(self):
        """
        Use lightweight serializer for list view.
        """
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer
