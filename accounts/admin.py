from django.contrib import admin
from accounts.models import Profesor, Asesoria,Curso,Cita

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Asesoria)
admin.site.register(Cita)
