from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonViewSet.as_view()),
    path('products/', views.ProductViewSet.as_view()),
]