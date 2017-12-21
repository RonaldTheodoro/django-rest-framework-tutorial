from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import permissions as custom_permissions
from . import models, serializers


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly,
    )

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
