from django.http import Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Trouble
from .pagination import PageSizePagination
from .serializers import TroubleSerializer, ExtendedTroubleSerializer


class TroubleList(ListCreateAPIView):
    ORDERING_TYPES = ['code', '-code', 'title', 'system']
    DEFAULT_ORDER = 'code'

    MODE_TYPES = ['simple', 'extended']
    DEFAULT_MODE = 'simple'

    pagination_class = PageSizePagination

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        mode_param = request.query_params.get('mode', self.DEFAULT_MODE)
        mode = mode_param if mode_param in self.MODE_TYPES else self.DEFAULT_MODE

        if mode == 'extended':
            serializer = ExtendedTroubleSerializer(page, many=True)
        else:
            serializer = TroubleSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        order_param = self.request.query_params.get('order', self.DEFAULT_ORDER)
        order = order_param if order_param in self.ORDERING_TYPES else self.DEFAULT_ORDER
        return Trouble.objects.order_by(order)


class TroubleDetail(APIView):

    def get(self, request, dtc, format=None):
        trouble = self.get_object(dtc)
        serializer = TroubleSerializer(trouble)
        return Response(serializer.data)

    def get_object(self, code):
        try:
            code = code.upper()
            return Trouble.get_trouble(code)
        except Trouble.DoesNotExist:
            raise Http404
