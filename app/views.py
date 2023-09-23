from django.contrib.auth.models import User
from rest_framework import permissions, generics
from .serializers import UserSerializer, ProductSerializer, LessonSerializer
from .models import Product, Lesson

# Create your views here.
class LessonViewSet(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        lessons = Lesson.objects.filter(product__owners=user)
        return lessons
    

class ProductViewSet(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        products = Product.objects.all()
        return products
