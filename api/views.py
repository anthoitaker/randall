from django.http import Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Trouble
from .serializers import TroubleSerializer


class TroubleList(ListCreateAPIView):
    queryset = Trouble.objects.all()
    serializer_class = TroubleSerializer


class TroubleDetail(APIView):

    def get(self, request, dtc, format=None):
        trouble = self.get_object(dtc)
        serializer = TroubleSerializer(trouble)
        return Response(serializer.data)

    def get_object(self, code):
        try:
            code = code.upper()
            return Trouble.objects.get(code=code)
        except Trouble.DoesNotExist:
            raise Http404
