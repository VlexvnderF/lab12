from django.contrib import admin

from prestamos.models import Libro, Prestamo, Usuario

# Register your models here.


admin.site.register(Prestamo)
admin.site.register(Libro)
admin.site.register(Usuario)