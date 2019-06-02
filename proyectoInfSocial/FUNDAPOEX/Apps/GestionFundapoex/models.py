from django.db import models

# Create your models here.

class Paciente (models.Model): 
	Nombre1 = models.CharField(max_length = 60, blank = False, null=False)
	Nombre2 = models.CharField(max_length = 60, blank = True, null=True)
	Apellido1 = models.CharField(max_length = 60, blank = False, null=True)
	Apellido2 = models.CharField(max_length = 60, blank = True, null=False)
	FechaIngreso = models.DateField()
	Estados = (('A','Activo'), ('N','NoActivo'))
	EstadoActivacion = models.CharField(max_length=1, choices=Estados, default = 'N') 

	def __str__(self):
		return self.Nombre1


class Docente(models.Model): 
	Nombre1 = models.CharField(max_length = 60, blank = False, null=False)
	Nombre2 = models.CharField(max_length = 60, blank = True, null=True)
	Apellido1 = models.CharField(max_length = 60, blank = False, null=False)
	Apellido2 = models.CharField(max_length = 60, blank = True, null=True)
	FechaIngreso = models.DateField()

	def __str__(self):
		return self.Nombre1
	


class Usuario(models.Model):
	NombreUsuario = models.CharField(max_length = 60, blank = False, null=False) 
	Contraseña =models.CharField(max_length = 60, blank = False, null=False)
	Email = models.EmailField()
	idDocete = models.ForeignKey(Docente, blank = False, null=False, on_delete = models.CASCADE)
	idPaciente = models.ForeignKey(Paciente, blank = False, null=False,on_delete = models.CASCADE)

	def __str__(self):
		return self.NombreUsuario

class HistorialPaciente(models.Model):
	FechaHistorialPaciente = models.DateField()
	HistorialPaciente = models.CharField(max_length = 1000,blank = False, null=False) 
	HistorialPaciente = models.CharField(max_length = 1000, blank = False, null=False)
	IdentificacionPaciente = models.ForeignKey(Paciente, blank=True, null= True,on_delete = models.CASCADE) 

	def __str__(self):
		return self.HistorialPaciente



