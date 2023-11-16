from django.db import models


MACHINE_ROLE_CHOICES = [
    ("C", "paper cutting"),
    ("PO", "printing only"),
    ("PC", "printing and cutting"),
    ("PA", "packaging"),
    # Roll hammer
]


PAPER_TYPES = [
    ("T", "thermo"),
]

# Create your models here.
class Operator(models.Model):
    first_name = models.CharField(max_length=32, blank=True, default='')
    last_name = models.CharField(max_length=32, blank=True, default='')
    date_started = models.DateTimeField()
    
    
class Machine(models.Model):
    name = models.CharField(max_length=32, blank=True, default='')
    producer = models.CharField(max_length=32, blank=True, default='')  # TODO Change to fkey 
    role = models.CharField(choices=MACHINE_ROLE_CHOICES, max_length=2)
    date_produced = models.DateTimeField()
    
    
class Supplier(models.Model):
    company_name = models.CharField(max_length=32, blank=True, default='')
    # TODO Contact info, type of supply, ...
    
    
class ReproRollType(models.Model):
    width = models.FloatField()  # in mm
    length = models.FloatField()  # in m
    weight = models.FloatField()  # in g
    paper_type = models.CharField(choices=PAPER_TYPES, max_length=1)
    
    
class ReproRoll(models.Model):
    repro_roll_type = models.ForeignKey(ReproRollType, on_delete=models.PROTECT)
    bar_code = models.CharField(max_length=256, blank=True, default='') # TODO Determine 'batch'
    
    
class Product(models.Model):
    batch_bar_code = models.CharField(max_length=256, blank=True, default='') # TODO Determine 'batch'
    produced_by = models.ForeignKey(Operator, on_delete=models.PROTECT)
    produced_on = models.ForeignKey(Machine, on_delete=models.PROTECT)
    repro_material = models.ForeignKey(ReproRoll, on_delete=models.PROTECT)

