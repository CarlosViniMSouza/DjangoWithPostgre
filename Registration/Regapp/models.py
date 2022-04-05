from django.db import models


class Client(models.Model):
    Nome = models.CharField(max_length=60)
    Telefone = models.IntegerField()
    Email = models.CharField(max_length=20)
    Senha = models.CharField(max_length=15)


class Car(models.Model):
    Modelo = models.CharField(max_length=10)
    Ano = models.IntegerField()
    Cor = models.CharField(max_length=15)
    Placa = models.CharField(max_length=8)
