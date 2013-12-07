from django.contrib import admin
from models import area, horas_trabajadas
from models import empleado
from django.conf.urls.static import static

class areaAdminModels ( admin.ModelAdmin ):
	list_display = ('codigo_area','nombre_area','descripcion' )
	search_fields = ('codigo_area','nombre_area','descripcion',)
	list_filter =('nombre_area',)

class cargo_empleadoAdminmodels ( admin.ModelAdmin):
	list_display = ('codigo_cargo','nombre','descripcion','codigo_area')
	search_fields = ('codigo_cargo','nombre','descripcion','codigo_area')	
	list_filter = ('codigo_cargo')

class empleadoAdminmodels (admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido','direccion','telefono','eps','arl','area','tipo_contrato','cargo')
	search_fields = ('cedula','nombre','apellido','direccion','telefono','eps','arl','area','tipo_contrato','cargo')
	list_filter = ('cedula')

class tipo_contratoAdminmodels (admin.ModelAdmin):
	list_display = ('nombre_contrato','descripcion','codigo')
	search_fields = ('nombre_contrato','descripcion','codigo')
	list_filter = ('codigo')

class horas_extras_acumuladasAdminmodels (admin.ModelAdmin):
	list_display = ('codigo', 'cedula','mes','ano', 'horas_extras_acumuladas')
	search_fields = ('codigo', 'cedula','mes','ano', 'horas_extras_acumuladas')	
	list_filter = ('codigo')

class horas_trabajadasAdminmodels (admin.ModelAdmin):
	list_display = ('codigo', 'cedula', 'fecha_hora_ingreso','fecha_hora_salida','turno','hora_salida_almuerzo','hora_entrada_almuerzo')
	search_fields = ('codigo', 'cedula', 'fecha_hora_ingreso','fecha_hora_salida','turno','hora_salida_almuerzo','hora_entrada_almuerzo')
	list_filter = ('cedula')
	
				
	
admin.site.register(area, areaAdminModels)
admin.site.register(horas_trabajadas)


admin.site.register(empleado)
from models import cargo_empleado
admin.site.register(cargo_empleado)
from models import horas_extras_acumuladas
admin.site.register(horas_extras_acumuladas)
from models import tipo_contrato
admin.site.register(tipo_contrato)


