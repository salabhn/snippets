from django.urls import path

from .views import *


urlpatterns = [
    path('overview/', overview_api),
    path('snippets/', SnippetView.as_view()),
    path('snippets/<int:pk>/', SnippetView.as_view(), name='snippet-detail'),
    path('tags/', TagView.as_view()),
    path('tags/<int:pk>/', TagView.as_view(), name='tag-detail'),
]

