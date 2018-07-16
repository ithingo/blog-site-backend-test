from rest_framework import serializers
from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Category instance to JSON"""

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )


class PostSerializer(serializers.ModelSerializer):
    """Serializer to map the Post instance to JSON"""

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'category',
            'created_at',
            'updated_at',
        )
        read_only_fields = (
            'created_at',
            'updated_at',
        )
