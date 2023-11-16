from django.shortcuts import render
from rest_framework import viewsets
from ims_serving.models import Operator, Machine, Supplier, ReproRollType, ReproRoll, Product
from ims_serving.serializers import OperatorSerializer, MachineSerializer, SupplierSerializer, \
    ReproRollTypeSerializer, ReproRollSerializer, ProductSerializer


class OperatorViewSet(viewsets.ModelViewSet):
    query_set = Operator.objects.all()
    serializer = OperatorSerializer
    
    
class MachineViewSet(viewsets.ModelViewSet):
    query_set = Machine.objects.all()
    serializer = MachineSerializer
    
    
class SupplierViewSet(viewsets.ModelViewSet):
    query_set = Supplier.objects.all()
    serializer = SupplierSerializer
    
    
class ReproRollTypeViewSet(viewsets.ModelViewSet):
    query_set = ReproRollType.objects.all()
    serializer = ReproRollTypeSerializer
    

class ReproRollViewSet(viewsets.ModelViewSet):
    query_set = ReproRoll.objects.all()
    serializer = ReproRollSerializer
        
        
class ProductViewSet(viewsets.ModelViewSet):
    query_set = Product.objects.all()
    serializer = ProductSerializer