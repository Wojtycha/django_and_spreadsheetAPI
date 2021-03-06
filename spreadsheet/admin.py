from django.contrib import admin
from .models import DaneArkusza, Faktura
from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import url
from django.http import HttpResponseRedirect


@staff_member_required
def getData(request):
    DaneArkusza.getDataFromSheet()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

class AdmSite(admin.ModelAdmin):

    def get_urls(self):
        urls = super(AdmSite, self).get_urls()
        my_urls = [
            url(r"^getData/$", getData)
        ]
        return my_urls + urls
    list_display = ['id', 'Imie', 'Nazwisko', 'Email', 'Numer_telefonu', 'Adres']
    change_list_template = "admin/changelist.html"
    search_fields = ['id', 'Imie', 'Nazwisko']

admin.site.register(DaneArkusza, AdmSite)
admin.site.register(Faktura)