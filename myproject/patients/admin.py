from django.contrib import admin

# Register your models here.
from .models import Countries, Typesdocs, Occupations, Disability, Municipalities, Ethnicity, Eps, Person

admin.site.register(Countries)  
admin.site.register(Typesdocs)
admin.site.register(Occupations)
admin.site.register(Disability)
admin.site.register(Municipalities)
admin.site.register(Ethnicity)
admin.site.register(Eps)
admin.site.register(Person)