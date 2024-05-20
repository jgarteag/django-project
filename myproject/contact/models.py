from django.db import models
from patients.models import Person

# Create your models here.
class Borrows(models.Model):
    """
    Clase que representa los prestadores de salud.
    """
    code_borrow = models.CharField(max_length=12, primary_key=True, verbose_name = 'Código prestadores')
    name_borrow = models.CharField(max_length=200, verbose_name = 'Nombre del prestador', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'borrows'

    def __str__(self):
        return f'{self.code_borrow} - {self.name_borrow}'
    
class Modality(models.Model):
    """
    Clase que representa la modalidad de atención de un paciente.
    """
    id_typemod = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la modalidad')
    description_modality = models.CharField(max_length=100, verbose_name = 'Descripción de la modalidad', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'modality'

    def __str__(self):
        return f'{self.id_typemod} - {self.description_modality}'
    
class Entrys(models.Model):
    """
    Clase que representa la entrada de un paciente a un centro de salud.
    """
    id_type_entrys = models.CharField(primary_key=True, max_length=2, verbose_name = 'Código de la entrada')
    entrys_names = models.CharField(max_length=200, verbose_name = 'Nombre de la entrada', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'entrys'

    def __str__(self):
        return f'{self.id_type_entrys} - {self.entrys_names}'
    
class Causecare(models.Model):
    """
    Clase que representa la causa de atención de un paciente.
    """
    id_care = models.CharField(max_length=2, primary_key=True, verbose_name = 'Código de la causa de atención')
    type_care = models.CharField(max_length=50, verbose_name = 'Tipo de atención', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'causecare'

    def __str__(self):
        return f'{self.id_care} - {self.type_care}'
    
class Illnesses(models.Model):
    """
    Clase que representa las enfermedades de un paciente.
    """
    cod_4 = models.CharField(max_length=4, primary_key=True, verbose_name = 'Código de la enfermedad')
    des_illness = models.CharField(max_length=400, verbose_name = 'Descripción de la enfermedad', unique = True, null = False)

    class Meta:
        managed = False
        db_table = 'illnesses'

    def __str__(self):
        return f'{self.cod_4} - {self.des_illness}'

class Contact(models.Model):
    """
    Clase que representa el contacto de una persona con un servicio de salud.
    """
    GRP_SERVICES = [
        ('01', 'Consulta Externa'),
        ('02', 'Apoyo Diagnostico y Complementacion Terapeutica'), 
        ('03', 'Internacion'),
        ('04', 'Quirurgico'),
        ('05', 'Atencion Inmediata'),
    ]

    ENV_ATT = [
        ('01', 'Hogar'),
        ('02', 'Comunitario'),
        ('03', 'Escolar'),
        ('04', 'Laboral'),
        ('05', 'Institucional'),
    ]

    TRIAGE = [
        ('01', 'TRIAGE I'),
        ('02', 'TRIAGE II'),
        ('03', 'TRIAGE III'),
        ('04', 'TRIAGE IV'),
        ('05', 'TRIAGE V'),
    ]

    TYPES = [
        ('01', 'Impresión Diagnóstica'),
        ('02', 'Confirmado Nuevo'),
        ('03', 'Confirmado Repetido')
    ]

    id_contact = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True, related_name='id_contact')
    cod_borr = models.ForeignKey(Borrows, on_delete=models.PROTECT, verbose_name='Código del prestador', null=True, blank=True)
    date_start_attention = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de inicio de atención') #automatico
    modality_of_realization_it = models.ForeignKey(Modality, on_delete=models.PROTECT, verbose_name='Modalidad de realización de la atención', null=True, blank=True)
    it_groups = models.CharField('Grupo de servicios', max_length=2, choices = GRP_SERVICES, default = '01')
    env_attention = models.CharField('Entorno de atención', max_length=2, choices = ENV_ATT, default = '01')
    way_of_entry = models.ForeignKey(Entrys, on_delete=models.PROTECT, verbose_name='Vía de ingreso')
    cause_of_care = models.ForeignKey(Causecare, on_delete=models.PROTECT, verbose_name='Causa de atención')
    date_triage = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de triage') #automatico
    classification_triage = models.CharField('Clasificación de triage', max_length=2, choices = TRIAGE, default = '01')
    diagnosis_of_admission = models.ForeignKey(Illnesses, on_delete=models.PROTECT, verbose_name='Diagnóstico de ingreso')
    type_of_diagnosis = models.CharField('Tipo de diagnóstico', max_length=2, choices = TYPES, default = '01')

    class Meta:
        db_table = 'contact'
        verbose_name = 'Contacto con el servicio de salud'
        verbose_name_plural = 'Contacts'
        constraints = [
            models.UniqueConstraint(fields=['id_contact', 'date_start_attention'], name='UQ_ID_CONTACT_DATE_ATTENTION')
        ]

    def __str__(self):
        return f'{self.id_contact} - {self.date_start_attention}'.strip()