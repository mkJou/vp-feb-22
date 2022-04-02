from dataclasses import field
from django.contrib import admin
from .models import *
# Register your models here.

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PersonResource(resources.ModelResource):

    class Meta:
        model = Person
        fields = ('id', 'cedula', 'cargo', 'nombre_tipo_equipo', 'estado_cargo', 'municipio_cargo', 'parroquia_cargo', 'red_name', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'sexo', 'correo', 'tlf_1', 'tlf_2', 'tlf_3')

class PersonAdmin(ImportExportModelAdmin):
    list_filter = ('nombre_tipo_equipo', 'red_name')
    resource_class = PersonResource

admin.site.register(Person, PersonAdmin)

