from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.exceptions import ValidationError
from .serializers import (
    ExpenseSerializer,
    CategorySerializer,
    PaymentSerializer,
    SummaryDaySerializer,
    SummaryMonthSerializer,
)
from .models import Category, Expense, Payment
from django.db.models import F, Sum, Max, Subquery, OuterRef, Window
from django.db.models.functions import RowNumber, TruncDate, TruncMonth
from .pagination import ExpenseListPagination

# Create your views here.


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        category_name = serializer.validated_data["name"]
        name_exists = Category.objects.filter(name=category_name).exists()
        if name_exists:
            raise ValidationError({"name": "Category with this name already exists."})
        serializer.save()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.annotate(
        category_name=F("category__name"), payment_method=F("payment__method")
    ).order_by("-date", "-id")
    serializer_class = ExpenseSerializer
    pagination_class = ExpenseListPagination


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.select_related("category")
    serializer_class = ExpenseSerializer


class SummaryListDay(generics.ListAPIView):
    max_price_subquery = (
        Expense.objects.filter(date=OuterRef("date"))
        .order_by("-price")
        .values("price")[:1]
    )

    # Subquery to rank the rows based on price within each date group
    rank_subquery = (
        Expense.objects.filter(date=OuterRef("date"))
        .annotate(rank=Window(expression=RowNumber(), order_by=F("price").desc()))
        .filter(rank=1)
        .values("item")[:1]
    )

    queryset = (
        Expense.objects.values("date")
        .annotate(
            total=Sum("price"), max_spent=Max("price"), max_item=Subquery(rank_subquery)
        )
        .order_by("-date")
    )
    serializer_class = SummaryDaySerializer


class SummaryListMonth(generics.ListAPIView):
    queryset = (
        Expense.objects.annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total=Sum("price"), max_spent=Max("price"))
        .order_by("month")
    )

    serializer_class = SummaryMonthSerializer

