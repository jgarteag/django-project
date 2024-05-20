from django.contrib import admin
from .models import Borrows, Modality, Entrys, Causecare, Illnesses, Contact

admin.site.register(Borrows)
admin.site.register(Modality)
admin.site.register(Entrys)
admin.site.register(Causecare)
admin.site.register(Illnesses)
admin.site.register(Contact)