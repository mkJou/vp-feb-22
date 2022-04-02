from django.db import models

# Create your models here.
class Person(models.Model):

    TYPE_TEAM = (
        ('Equipo Parroquial de Activistas', 'Equipo Parroquial de Activistas'),
        ('Equipo de Centro de Votación', 'Equipo de Centro de Votación'),
        ('Red Popular', 'Red Popular'),
    )

    estado = models.CharField(max_length=256, default='EDO. ZULIA', null=True)
    municipio = models.CharField(max_length=256, default='MP. MARACAIBO', null=True)
    parroquia = models.CharField(max_length=256, default='PQ. FRANCISCO EUGENIO B', null=True)
    nac = models.CharField(max_length=15, null=True, default='V')
    cedula = models.CharField(max_length=256, default='', null=True)
    cargo = models.CharField(max_length=256, default='', null=True)
    nombre_tipo_equipo = models.CharField(max_length=256, default='', null=True, choices=TYPE_TEAM)
    estado_cargo = models.CharField(max_length=256, default='', null=True)
    municipio_cargo = models.CharField(max_length=256, default='', null=True)
    parroquia_cargo = models.CharField(max_length=256, default='', null=True)
    red_name = models.CharField(max_length=256, default='', null=True)

    nombre_1 = models.CharField(max_length=256, default='', null=True)
    nombre_2 = models.CharField(max_length=256, default='', null=True)

    apellido_1 = models.CharField(max_length=256, default='', null=True)
    apellido_2 = models.CharField(max_length=256, default='', null=True)

    sexo = models.CharField(max_length=256, default='', null=True)
    correo = models.CharField(max_length=256, default='', null=True)
    
    tlf_1 = models.CharField(max_length=256, default='', null=True)
    tlf_2 = models.CharField(max_length=256, default='', null=True)
    tlf_3 = models.CharField(max_length=256, default='', null=True)

    observaciones = models.TextField(default='', max_length=256, name='Observaciones')
    
    class Meta:
        verbose_name = "Activista"
        verbose_name_plural = 'Activistas'

    def __str__(self):

        cd = f'{self.nac}-{self.cedula} {self.nombre_1} {self.nombre_2} {self.apellido_1} {self.apellido_2}'
        return cd
