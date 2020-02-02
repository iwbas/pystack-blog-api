from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from .models import Page, Video, Audio, Text
from .serializers import PageSerializer, PageDetailsSerializer

from .mixins import MyPaginationMixin

class PageList(APIView, MyPaginationMixin):
    queryset = Page.objects.all()
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 

    def get(self, request):
        # pages = Page.objects.all()
        pages = self.paginate_queryset(self.queryset)
        if pages is not None:
            serializer = PageSerializer(pages, many=True, context={"request":request}) 
            return self.get_paginated_response(serializer.data)
        # return Response({"pages": serializer.data, "id": Page.objects.first().id})

class PageDetail(APIView):
    def get(self, request, pk):
        page = get_object_or_404(Page.objects.all(), pk=pk)
        page_serializer = PageDetailsSerializer(page, context={"request":request})

        return Response({"page": page_serializer.data})