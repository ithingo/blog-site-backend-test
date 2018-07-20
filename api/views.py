from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404


from .serializers import CategorySerializer, PostSerializer
from .models import Category, Post


class CategoryListView(APIView):
    """This class defines a behavior for categories list"""

    def __get_all_objects(self):
        return get_list_or_404(Category)

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
        return get_object_or_404(Category, id=pk)

    def get(self, request, pk, format=None):
        category = self.__get_object(pk)
        category_serializer = CategorySerializer(category)
        return Response(category_serializer.data)

    def put(self, request, pk, format=None):
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


class PostListView(APIView):
    """This class defines a behavior for posts list"""

    def __get_all_objects(self):
        return get_list_or_404(Post)

    def get(self, request, format=None):
        posts = self.__get_all_objects()
        posts_serializer = PostSerializer(posts, many=True)
        return Response(posts_serializer.data)

    def post(self, request, format=None):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        posts = self.__get_all_objects()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostDetailsView(APIView):
    """This class defines a behavior for post item"""
    def __get_object(self, pk):
        return get_object_or_404(Category, id=pk)

    def get(self, request, pk, format=None):
        post = self.__get_object(pk)
        post_serializer = PostSerializer(post)
        return Response(post_serializer.data)

    def put(self, request, pk, format=None):
        post = self.__get_object(pk)
        post_serializer = PostSerializer(post, data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.__get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
