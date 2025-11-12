from rest_framework import viewsets, filters
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer, ProjectListSerializer


class ProfileView(RetrieveAPIView):
    """
    API endpoint to retrieve profile information.
    GET /api/profile/ - Retrieve the profile
    """
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        """
        Get the single profile instance
        """
        try:
            profile = Profile.objects.first()
            if profile:
                serializer = self.serializer_class(profile, context={'request': request})
                return Response(serializer.data)
            else:
                # Return default data if no profile exists
                return Response({
                    'name': 'Nizomjon Urolov',
                    'title': 'Junior Web Developer | Cybersecurity Enthusiast',
                    'bio': 'Passionate about building clean, responsive, and user-friendly websites.',
                    'email': 'nizomjonurolov24@gmail.com',
                    'phone': '+998 95-039-36-69',
                    'location': 'Pilla street, 78, Tashkent',
                    'github_url': 'https://github.com/urolovforever',
                    'linkedin_url': 'https://www.linkedin.com/in/nizomjonurolov',
                    'telegram_url': 'https://t.me/urolovnizomjon',
                    'profile_image': None,
                    'cv_file': None
                })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
