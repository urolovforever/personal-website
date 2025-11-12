from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model with all fields.
    """
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'image',
            'github_link',
            'live_link',
            'technologies',
            'project_type',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for project list view.
    """
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'image',
            'github_link',
            'live_link',
            'technologies',
            'project_type',
            'created_at'
        ]
