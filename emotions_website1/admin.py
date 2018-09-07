from django.contrib import admin
from emotions_website1.models import Country,VisitorQuery

class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ['name', 'code']
    search_fields  = ['name', 'code']
    ordering = ['name']
    readonly_fields = ['name', 'code','alpha2',
                    'region',
                    'subregion',
                    'intermregion']
    actions = []
class VisitorAdmin(admin.ModelAdmin):
    model = VisitorQuery
    list_display = ['created','keywords','name','get_country_name','processed']
    ordering = ['-created']
    search_fields = ['keywords','name','country__name','processed']
    actions = ['do_process']

    def get_country_name(self, obj):
        return obj.country.name if obj.country_id is not None else ''
    get_country_name.admin_order_field  = 'country'
    get_country_name.short_description = 'Country Name'


    def do_process(self, request, objects):
        for obj in objects:
            self.do_process_query(obj)
        return
    do_process.short_description = 'Do process'

    def do_process_query(self, obj):
        return True


admin.site.register(Country, CountryAdmin)
admin.site.register(VisitorQuery, VisitorAdmin)