from django.db import models


class Result(models.Model):
    input = models.TextField(verbose_name='Cadena de entrada')
    first = models.CharField(verbose_name='Primer Caracter', max_length=1, null=True, blank=True)
    first_count = models.IntegerField(verbose_name='Número de veces del primero', null=True, blank=True)
    second = models.CharField(verbose_name='Segundo Caracter', max_length=1, null=True, blank=True)
    second_count = models.IntegerField(verbose_name='Número de veces del segundo', null=True, blank=True)
    third = models.CharField(verbose_name='Tercer Caracter', max_length=1, null=True, blank=True)
    third_count = models.IntegerField(verbose_name='Número de veces del tercero', null=True, blank=True)
    success = models.BooleanField(verbose_name='¿Satisfactoria?')
    error_msg = models.CharField(max_length=100, verbose_name='Mensaje de error', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ejecución')
    pdf = models.FileField(verbose_name='PDF generado', upload_to='pdf')
    xml = models.FileField(verbose_name='XML generado', upload_to='xml')

    def __str__(self):
        end = 'satisfactoria' if self.success else 'error'
        return self.created_at.strftime('%d/%m/%y %H:%M:%S') + ' ' + end
