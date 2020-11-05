from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.reverse import reverse
from rest_framework import mixins, generics

from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def overview_api(request):
    snippets = Snippet.objects.all()

    response = {'count': snippets.count(), 'snippets': [reverse('snippet-detail', args=[x.id], request=request) for x in snippets]}
    return Response(response)


class SnippetView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]


class TagView(generics.ListAPIView, generics.RetrieveAPIView):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

