from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Countries(models.Model):
    """
    Clase que representa los países.
    segun ISO 3166-1 alpha-3
    """
    alfa_3 = models.CharField(max_length=3, primary_key=True, verbose_name = 'Código de tres letras del país')
    name_country = models.CharField(max_length=200, verbose_name = 'Nombre del país', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return f'{self.alfa_3} - {self.name_country}'
    
class Typesdocs(models.Model):
    """
    Clase que representa el tipo de documento de identificación de una persona.
    """
    id_typedoc = models.CharField(verbose_name = 'Código del tipo de documento', max_length=2, primary_key=True)
    doc_type = models.CharField(verbose_name = 'Descripción', max_length=100, unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'typesdocs'

    def __str__(self):
        return f'{self.id_typedoc} - {self.doc_type}'
    
class Occupations(models.Model):
    """
    Clase que representa la ocupación de una persona.
    """
    code_occ = models.CharField(max_length=4, primary_key=True, verbose_name = 'Código de la ocupación')
    name_occ = models.CharField(max_length=200, verbose_name = 'Nombre de la ocupación', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'occupations'

    def __str__(self):
        return f'{self.code_occ} - {self.name_occ}'
    
class Disability(models.Model):
    """
    Clase que representa la discapacidad de una persona.
    """
    id_dis = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la discapacidad')
    name_dis = models.CharField(max_length=50, verbose_name = 'Nombre de la discapacidad', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'disability'

    def __str__(self):
        return f'{self.id_dis} - {self.name_dis}'
    
class Municipalities(models.Model):
    """
    Clase que representa los municipios de un departamento.
    """
    departament = models.CharField(max_length=200, verbose_name='Departamento', null = False)
    code_dep = models.CharField(primary_key=True, max_length=5, verbose_name='Código del municipio', null = False)
    name_dep = models.CharField(max_length=200, verbose_name='Nombre del municipio', null = False)
    type_mnc = models.CharField(max_length=200, verbose_name='Tipo de municipio', null = False)

    class Meta:
        managed = False
        db_table = 'municipalities'

    def __str__(self):
        return f'{self.code_dep} - {self.name_dep}'
    
class Ethnicity(models.Model):
    """
    Clase que representa la etnia de una persona.
    """
    id_et = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la etnia')
    name_ethn = models.CharField(max_length=200, verbose_name = 'Nombre de la etnia', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'ethnicity'

    def __str__(self):
        return f'{self.id_et} - {self.name_ethn}'
    
class Eps(models.Model):
    """
    Clase que representa la EPS de una persona.
    """
    code_eps = models.CharField(max_length=6, primary_key=True, verbose_name = 'Código de la EPS')
    name_eps = models.CharField(max_length=200, verbose_name = 'Nombre de la EPS', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'eps'

    def __str__(self):
        return f'{self.code_eps} - {self.name_eps}'


class Person(models.Model):
    """
    Clase que representa a una persona.
    """
    SEX_BIO = [
        ('01', 'Hombre'),
        ('02', 'Mujer'),
        ('03', 'Indeterminado intersexual'),
    ]

    GEN_ID = [
        ('01', 'Masculino'),
        ('02', 'Femenino'),
        ('03', 'Transgenero'),
        ('04', 'Neutro'),
        ('05', 'No lo declara')
    ]

    OPOSSITION = [
        ('01', 'Si'),
        ('02', 'No')
    ]

    ZONE = [
        ('01', 'Urbana'),
        ('02', 'Rural')
    ]

    id_history = models.AutoField(primary_key=True, verbose_name = 'Código de historia clínica')
    country_origin = models.ForeignKey(Countries, on_delete = models.PROTECT, verbose_name = 'País de origen', related_name='origin_country')
    doc_type = models.ForeignKey(Typesdocs, on_delete = models.PROTECT, verbose_name = 'Tipo de documento')
    number_doc = models.CharField(max_length=20, blank=False, null=False, validators=[RegexValidator(regex='^[0-9]*$', message='Solo se permiten números')], verbose_name = 'Número de documento persona')
    last_name = models.CharField(max_length=60, blank=False, null=False, verbose_name = 'Primer apellido')
    surname = models.CharField(max_length=60, blank=False, null=False, verbose_name = 'Segundo apellido')
    first_name = models.CharField(max_length=60, blank=False, null=False, verbose_name = 'Primer nombre')
    middle_name = models.CharField(max_length=60, null=True, blank=True, verbose_name = 'Segundo nombre', default = '')
    date_born = models.DateTimeField(blank=False, null=False, verbose_name = 'Fecha de nacimiento')
    biologic_sex = models.CharField(max_length=2, choices = SEX_BIO, default = '01', verbose_name = 'Sexo biológico')
    gender_identity = models.CharField(max_length=2, choices = GEN_ID, default = '01', verbose_name = 'Identidad de género')
    occupation_care = models.ForeignKey(Occupations, on_delete=models.PROTECT, verbose_name='Ocupación')
    opossition_donation = models.CharField(max_length=2, choices = OPOSSITION, default = '01', verbose_name = 'Oposición legal de donación')
    date_opossition = models.DateField(auto_now=True, verbose_name = 'Fecha de oposición a la donación') #automatico
    antiquated_will_document = models.CharField(max_length=2, blank=False, null=False, choices = OPOSSITION, default = '01')
    date_suscrip_ant_will_doc = models.DateField(auto_now=True, verbose_name='Fecha de suscripción del documento de voluntad anticipada') #automatico

    category_disability = models.ForeignKey(Disability, on_delete=models.PROTECT, verbose_name='Categoría de discapacidad')
    habitual_residence = models.ForeignKey(Countries, on_delete=models.PROTECT, verbose_name= 'País de residencia habitual', related_name='residence_country')
    municipality_of_hab_res = models.ForeignKey(Municipalities, on_delete=models.PROTECT, verbose_name='Municipio de residencia habitual')
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.PROTECT, verbose_name='Etnia')
    territorial_zone = models.CharField(max_length=2, choices = ZONE, default = '01', verbose_name='Zona de residencia')
    eps = models.ForeignKey(Eps, on_delete=models.PROTECT, verbose_name='EPS')

    class Meta:
        db_table = 'person'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        constraints = [
            models.UniqueConstraint(fields=['doc_type', 'number_doc'], name='UQ_DOCUMENT_TYPE_IDENTITY_CARD')
        ]