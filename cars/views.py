from rest_framework import viewsets
from .models import Car, Repair, Sale
from .serializers import CarSerializer, RepairSerializer, SaleSerializer # type: ignore
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Auto Center API!")

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
