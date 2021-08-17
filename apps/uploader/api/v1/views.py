from rest_framework import viewsets, parsers

from .serializers import DropBoxSerializer

from ...models import DropBox


class DropBoxViewset(viewsets.ModelViewSet): 
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']