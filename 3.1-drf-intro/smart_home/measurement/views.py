
from rest_framework.response import Response
from .models import Sensor, Measurements
from .serializers import SensorDetailSerializer, MeasurementSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView


class SensView(APIView):
    def get(self, request):
        datas = Sensor.objects.all()
        ser = SensorDetailSerializer(datas, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = SensorDetailSerializer(data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailView(APIView):
    def _get_object(self, pk):
        return Sensor.objects.get(pk=pk)

    def patch(self, request, pk):
        model_object = self._get_object(pk)
        serializer = SensorDetailSerializer(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(status=401, data="wrong parameters")


class SensOneView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer



class MeasurementsMoreView(viewsets.ModelViewSet):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer
