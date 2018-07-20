from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailsView.as_view()),
    path('posts', views.PostListView.as_view()),
    path('posts/<int:pk>', views.PostDetailsView.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)