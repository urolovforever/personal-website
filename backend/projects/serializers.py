from rest_framework import serializers
from .models import Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model with all fields.
    """
    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'title',
            'bio',
            'profile_image',
            'email',
            'phone',
            'location',
            'github_url',
            'linkedin_url',
            'telegram_url',
            'cv_file',
            'updated_at'
        ]
        read_only_fields = ['id', 'updated_at']


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
