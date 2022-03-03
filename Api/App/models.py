from django.db import models
from datetime import date


# Create your models here.

class Foydalanuvchi(models.Model):
    fio=models.CharField('FIO',max_length=100)
    jins=models.CharField('Jinsi',max_length=20)
    birth_date=models.DateField(null=True)
    yaratildi=models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
    def __str__(self):
        return self.fio


class Kitob(models.Model):
    nomi = models.CharField('Nomi', max_length=100)
    muallif = models.ForeignKey(Foydalanuvchi,on_delete=models.CASCADE,related_name='foydalanuvchilar')

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
    def __str__(self):
        return self.nomi

