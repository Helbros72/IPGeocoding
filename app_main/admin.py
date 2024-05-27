from django.contrib import admin

from app_main.models import History, Country

#admin.site.register(History)
admin.site.register(Country)

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id','ip','date','country')
    search_fields = ('country',)
    list_filter = ('date',)



