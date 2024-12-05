from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    vin = models.CharField(max_length=17, unique=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Repair(models.Model):
    car = models.ForeignKey(Car, related_name='repairs', on_delete=models.CASCADE)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    repair_date = models.DateTimeField()

    def __str__(self):
        return f"Repair for {self.car}"

class Sale(models.Model):
    car = models.ForeignKey(Car, related_name='sales', on_delete=models.CASCADE)
    sale_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale of {self.car} on {self.sale_date}"
