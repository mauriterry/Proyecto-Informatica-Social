from django.contrib import admin
from .models import Paciente
from .models import Docente
from .models import Usuario
from .models import HistorialPaciente


# Register your models here.
admin.site.register(Paciente)
admin.site.register(Docente)
admin.site.register(Usuario)
admin.site.register(HistorialPaciente)