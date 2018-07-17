from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import CategorySerializer, PostSerializer
from .models import Category, Post


class CategoryListView(APIView):
    """This class defines a behavior for categories list"""

    def __get_all_objects(self):
        try:
            return Category.objects.all()
        except Category.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        categories = self.__get_all_objects()
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(categories_serializer.data)

    def post(self, request, format=None):
        categories_serializer = CategorySerializer(data=request.data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return Response(categories_serializer.data, status=status.HTTP_201_CREATED)
        return Response(categories_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        categories = self.__get_all_objects()
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryDetailsView(APIView):
    """This class defines a behavior for category item"""
    def __get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.__get_object(pk)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)

    def post(self, request, pk, format=None):
        category = self.__get_object(pk)
        category_serializer = CategorySerializer(category, data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data)
        return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.__get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCreateView(APIView):
    """This class defines a create behavior for posts list"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Save post data when creating a new post"""
        serializer.save()
