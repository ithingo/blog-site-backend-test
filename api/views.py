from rest_framework import generics


from .serializers import CategorySerializer, PostSerializer
from .models import Category, Post


class CategoryCreateView(generics.ListAPIView):
    """This class defines a create behavior for categories list"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """Save category data when creating a new category"""
        serializer.save()


class PostCreateView(generics.ListAPIView):
    """This class defines a create behavior for posts list"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Save post data when creating a new post"""
        serializer.save()
