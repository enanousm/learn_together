from django.db import models as m

# Create your models here.
class ramo(m.Model):
    _ramo = m.CharField(max_length=7)

    def __str__(self):
        return self._ramo

class horario(m.Model):
    username = m.CharField(max_length=150)
    rol = m.CharField(max_length=11)
    n_horario = m.CharField(max_length=100)
    estudiar = m.CharField(max_length=7, default='0')

class userdata(m.Model):
    username = m.CharField(max_length=25)
    first_name = m.CharField(max_length=25)
    last_name = m.CharField(max_length=25)
    rol = m.CharField(max_length=11)
    email = m.CharField(max_length=100)
    n_horario = m.CharField(max_length=100)
    estudiar = m.CharField(max_length=7, default='MAT-021')

    def __str__(self):
        return self.username + '------->' + self.rol