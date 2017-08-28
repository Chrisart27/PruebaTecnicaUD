from django.db import models


class Politic(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del partido')

    def __str__(self):
        return self.name


class UserSelection(models.Model):
    fk_politic = models.ForeignKey(Politic, verbose_name='Partido Politico')
    candidates = models.ManyToManyField('Candidate', verbose_name='Candidatos')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at.strftime('%d/%m/%y %H:%M:%S')


class Candidate(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre del candidato')

    def __str__(self):
        return self.name
