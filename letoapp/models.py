from django.db import models as m

# Create your models here.
class ramo(m.Model):
    _ramo = m.CharField(max_length=7)

    def __str__(self):
        return self._ramo

class horario(m.Model):
    username = m.CharField(max_length=150)
    n_horario = m.CharField(max_length=100)
    rol = m.CharField(max_length=11)

    def __str__(self):
        return self.username + '------->' + self.rol + '------->' + self.n_horario 
