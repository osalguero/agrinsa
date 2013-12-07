# encoding: utf-8 --
from django.db import models

# Create your models here.

class area(models.Model):

	codigo_area = models.CharField(max_length = 20, primary_key=True,verbose_name = 'Código de Area')
	nombre_area = models.CharField(max_length = 20)
	descripcion = models.CharField(max_length = 20)

	class Meta:
		db_table = 'area'
		#nombre como se visualiza la tabla en la interfaz grafica
		verbose_name_plural = 'Areas'

	def __unicode__(self):
			return self.nombre_area

class tipo_contrato (models.Model):
 	nombre_contrato = models.CharField (max_length = 20)
  	descripcion = models.CharField (max_length = 20)
  	codigo = models.CharField(max_length = 15, primary_key=True)

  	class Meta:
  		db_table = "tipo_contrato"
  		verbose_name_plural = 'tipos de contrato'

  	def __unicode__(self):
  		return self.descripcion



class empleado(models.Model):
	cedula = models.CharField(max_length=10,primary_key=True)
	nombres = models.CharField(max_length = 25)
	apellidos = models.CharField (max_length = 25)
	direccion = models.TextField()
	telefono = models.CharField(max_length = 12)
	eps = models.CharField(max_length = 20)
	arl	= models.CharField(max_length = 20)
	area = models.ForeignKey('area',null=True,blank=True,db_column='area')
	tipo_contrato = models.ForeignKey('tipo_contrato',null=True,blank=True,db_column='tipo_contrato')
	cargo =models.CharField(max_length = 20)

	class Meta:
		db_table = 'empleado'
		verbose_name_plural = 'empleados'

	def __unicode__(self):
		return self.nombres

class cargo_empleado (models.Model):
	

	codigo_cargo = models.CharField (max_length = 10)
	nombre = models.CharField (max_length = 20)
	descripcion = models.CharField (max_length = 20)
	codigo_area = models.ForeignKey('area',null=True,blank=True,db_column='codigo_area')

	class Meta:
		db_table = 'cargo_empleado'
		verbose_name_plural = 'cargo empleados'

	def __unicode__(self):
		return self.nombre

class horas_extras_acumuladas(models.Model):
	codigo = models.CharField(max_length = 10,primary_key=True,blank=True)
 	cedula = models.CharField(max_length = 15)
 	mes = models.CharField(max_length = 2)
 	ano = models.CharField (max_length = 4)
 	horas_extras_acumulada = models.IntegerField()

 	class Meta:
 		db_table = "horas_extras_acumuladas"
 		verbose_name_plural = 'Horas Extras acumuladas'

 	def __unicode__(self):
 		return self.cedula

  
class horas_trabajadas(models.Model):
	codigo = models.IntegerField()
	cedula = models.CharField (max_length = 10,primary_key = True,blank=True )
 	fecha_hora_ingreso = models.DateField()
 	fecha_hora_salida = models.DateField()
 	turno = models.IntegerField()
 	hora_salida_almuerzo = models.DateField()
 	hora_entrada_almuerzo = models.DateField()

 	class Meta:
 		db_table = "horas_trabajadas"
 		verbose_name_plural = 'horas_trabajadas'

 	def __unicode__(self):
 		return self.cedula
