from rest_framework import serializers
from .models import Foydalanuvchi


class FoydalanuvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foydalanuvchi
        fields = ['id','fio', 'jins', 'birth_date']