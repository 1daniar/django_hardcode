from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product, Lesson


class ProductSerializer(serializers.ModelSerializer):
    owners = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    lesson_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['owners', 'lesson_list']

class LessonSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Lesson
        fields = ['product', 'name', 'link', 'seconds', 'user_seconds', 'is_seen']

class UserSerializer(serializers.ModelSerializer):
    product_list = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'product_list']