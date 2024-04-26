from django.urls import path, include
from . import views

urlpatterns = [
    path('categories', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('expenses', views.ExpenseList.as_view()),
    path('expenses/<int:pk>', views.ExpenseDetail.as_view()),
    path('payments', views.PaymentList.as_view()),
    path('summary/day', views.SummaryListDay.as_view()),
    path('summary/month', views.SummaryListMonth.as_view()),
]
