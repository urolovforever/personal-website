from rest_framework import serializers
from .models import Profile, Project


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model with all fields.
    Returns absolute URLs for profile_image and cv_file.
    """
    profile_image = serializers.SerializerMethodField()
    cv_file = serializers.SerializerMethodField()

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

    def get_profile_image(self, obj):
        """Return absolute URL for profile image"""
        if obj.profile_image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.profile_image.url)
            return obj.profile_image.url
        return None

    def get_cv_file(self, obj):
        """Return absolute URL for CV file"""
        if obj.cv_file:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.cv_file.url)
            return obj.cv_file.url
        return None


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model with all fields.
    Returns absolute URL for image.
    """
    image = serializers.SerializerMethodField()

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

    def get_image(self, obj):
        """Return absolute URL for project image"""
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class ProjectListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for project list view.
    Returns absolute URL for image.
    """
    image = serializers.SerializerMethodField()

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

    def get_image(self, obj):
        """Return absolute URL for project image"""
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
