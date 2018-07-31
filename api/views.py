from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import System, Trouble
from .factories import TroubleSerializerFactory
from .pagination import PageSizePagination
from .serializers import SystemSerializer
from .shortcuts import get_trouble_or_404


class TroubleList(ListCreateAPIView):
    ORDERING_TYPES = ['code', '-code', 'title', 'system']
    DEFAULT_ORDER = 'code'

    pagination_class = PageSizePagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        mode = request.query_params.get('mode')
        trouble_serializer_factory = TroubleSerializerFactory(mode)
        serializer = trouble_serializer_factory.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        order_param = self.request.query_params.get('order', self.DEFAULT_ORDER)
        order = order_param if order_param in self.ORDERING_TYPES else self.DEFAULT_ORDER
        return Trouble.objects.order_by(order)


class TroubleDetail(APIView):

    def get(self, request, dtc):
        code = dtc.upper()
        trouble = get_trouble_or_404(code=code)
        mode = request.query_params.get('mode')
        trouble_serializer_factory = TroubleSerializerFactory(mode)
        serializer = trouble_serializer_factory.get_serializer(trouble)
        return Response(serializer.data)


class SystemList(ListCreateAPIView):
    ORDERING_TYPES = ['name', '-name']
    DEFAULT_ORDER = 'name'

    pagination_class = PageSizePagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = SystemSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        order_param = self.request.query_params.get('order', self.DEFAULT_ORDER)
        order = order_param if order_param in self.ORDERING_TYPES else self.DEFAULT_ORDER
        return System.objects.order_by(order)


class SymptomList(ListCreateAPIView):

    def list(self, request, dtc):
        code = dtc.upper()
        trouble = get_trouble_or_404(code=code)
        symptoms = trouble.list_symptoms()
        return Response(symptoms)


class CauseList(ListCreateAPIView):

    def list(self, request, dtc):
        code = dtc.upper()
        trouble = get_trouble_or_404(code=code)
        causes = trouble.list_causes()
        return Response(causes)


class SolutionList(ListCreateAPIView):

    def list(self, request, dtc):
        code = dtc.upper()
        trouble = get_trouble_or_404(code=code)
        solutions = trouble.list_solutions()
        return Response(solutions)
