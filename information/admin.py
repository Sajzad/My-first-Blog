from django.contrib import admin
from information.models import Divisions, Districts

class DistrictAdmin(admin.ModelAdmin):
	list_display= ('name','division','visited','population_density')
class divisionAdmin(admin.ModelAdmin):
	list_display= ('name', 'population','area')

admin.site.register(Divisions, divisionAdmin)
admin.site.register(Districts,DistrictAdmin)
#admin.site.register(DistrictAdmin)

# Register your models here.
