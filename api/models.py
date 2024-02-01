from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.name}"

class Payment(models.Model):
	method = models.CharField(max_length=50)

	def __str__(self) -> str:
		return f"{self.method}"

class Expense(models.Model):
	item = models.CharField(max_length=50)
	price = models.FloatField()
	date  = models.DateField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f"{self.item} -> {self.price}"