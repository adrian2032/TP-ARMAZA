from django.contrib import admin
from .models import *

admin.site.register(Materia)

# Register your models here.
class DocenteAdmin(admin.ModelAdmin):
    list_display = (
        'Nombre',
        'Apellido',
        'materia',
        'Edad',
        'id',
    )
    search_fields =  ('Apellido', 'Nombre')
    list_filter = ('Edad', 'Nombre', 'Apellido')

class NoDocenteAdmin(admin.ModelAdmin):
    list_display = (
        'NDNombre',
        'NDApellido',
        'NDoficina',
        'NDEdad',
        'id',
    )


admin.site.register(DocenteCla, DocenteAdmin)
admin.site.register(NoDocente)
admin.site.register(Oficina)