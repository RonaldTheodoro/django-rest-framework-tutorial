from rest_framework import generics

from . import models, serializers


class SnippetList(generics.ListCreateAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
