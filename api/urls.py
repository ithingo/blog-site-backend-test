from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views


urlpatterns = [
    path('categorylist', views.CategoryCreateView.as_view(), name='create-category'),
    path('postlist', views.PostCreateView.as_view(), name='create-post')
]


urlpatterns = format_suffix_patterns(urlpatterns)