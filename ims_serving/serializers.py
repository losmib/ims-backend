from rest_framework import serializers
from ims_serving.models import Operator, Machine, Supplier, ReproRollType, ReproRoll, Product


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ["id", "first_name", "last_name", "date_started"]
        
        
class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ["id", "name", "producer", "role", "date_produced"]
        
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "company_name"]
        
    
class ReproRollTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReproRollType
        fields = ["id", "width", "length", "weight", "paper_type"]
        
        
class ReproRollSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReproRoll
        fields = ["id", "repro_roll_type", "bar_code"]
        
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "batch_bar_code", "produced_by", "produced_on", "repro_material"]