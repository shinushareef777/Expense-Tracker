from rest_framework import serializers
from .models import Expense, Category, Payment

class ExpenseSerializer(serializers.ModelSerializer):
	category_name = serializers.CharField(source='category.name', read_only=True)
	payment_method = serializers.CharField(source='payment.method', read_only=True)

	class Meta:
		model = Expense
		fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = '__all__'

class SummaryDaySerializer(serializers.ModelSerializer):
	total = serializers.DecimalField(max_digits=6, decimal_places=2)
	max_spent = serializers.DecimalField(max_digits=6, decimal_places=2)
	max_item = serializers.CharField()

	class Meta:
		model = Expense
		fields = ['date', 'total', 'max_spent', 'max_item']

class SummaryMonthSerializer(serializers.Serializer):
	month = serializers.DateField()
	total = serializers.FloatField()
	max_spent = serializers.FloatField()
	


