# Generated by Django 3.2.8 on 2024-05-19 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrows',
            fields=[
                ('code_borrow', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Código prestadores')),
                ('name_borrow', models.CharField(max_length=200, unique=True, verbose_name='Nombre del prestador')),
            ],
            options={
                'db_table': 'borrows',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Causecare',
            fields=[
                ('id_care', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Código de la causa de atención')),
                ('type_care', models.CharField(max_length=50, unique=True, verbose_name='Tipo de atención')),
            ],
            options={
                'db_table': 'causecare',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entrys',
            fields=[
                ('id_type_entrys', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Código de la entrada')),
                ('entrys_names', models.CharField(max_length=200, unique=True, verbose_name='Nombre de la entrada')),
            ],
            options={
                'db_table': 'entrys',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Illnesses',
            fields=[
                ('cod_4', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Código de la enfermedad')),
                ('des_illness', models.CharField(max_length=400, unique=True, verbose_name='Descripción de la enfermedad')),
            ],
            options={
                'db_table': 'illnesses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('id_typemod', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='Código de la modalidad')),
                ('description_modality', models.CharField(max_length=100, unique=True, verbose_name='Descripción de la modalidad')),
            ],
            options={
                'db_table': 'modality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='id_contact', serialize=False, to='patients.person')),
                ('date_start_attention', models.DateTimeField(auto_now=True, verbose_name='Fecha de inicio de atención')),
                ('it_groups', models.CharField(choices=[('01', 'Consulta Externa'), ('02', 'Apoyo Diagnostico y Complementacion Terapeutica'), ('03', 'Internacion'), ('04', 'Quirurgico'), ('05', 'Atencion Inmediata')], default='01', max_length=2, verbose_name='Grupo de servicios')),
                ('env_attention', models.CharField(choices=[('01', 'Hogar'), ('02', 'Comunitario'), ('03', 'Escolar'), ('04', 'Laboral'), ('05', 'Institucional')], default='01', max_length=2, verbose_name='Entorno de atención')),
                ('date_triage', models.DateTimeField(auto_now=True, verbose_name='Fecha de triage')),
                ('classification_triage', models.CharField(choices=[('01', 'TRIAGE I'), ('02', 'TRIAGE II'), ('03', 'TRIAGE III'), ('04', 'TRIAGE IV'), ('05', 'TRIAGE V')], default='01', max_length=2, verbose_name='Clasificación de triage')),
                ('type_of_diagnosis', models.CharField(choices=[('01', 'Impresión Diagnóstica'), ('02', 'Confirmado Nuevo'), ('03', 'Confirmado Repetido')], default='01', max_length=2, verbose_name='Tipo de diagnóstico')),
                ('cause_of_care', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contact.causecare', verbose_name='Causa de atención')),
                ('cod_borr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contact.borrows', verbose_name='Código del prestador')),
                ('diagnosis_of_admission', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contact.illnesses', verbose_name='Diagnóstico de ingreso')),
                ('modality_of_realization_it', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='contact.modality', verbose_name='Modalidad de realización de la atención')),
                ('way_of_entry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contact.entrys', verbose_name='Vía de ingreso')),
            ],
            options={
                'verbose_name': 'Contacto con el servicio de salud',
                'verbose_name_plural': 'Contacts',
                'db_table': 'contact',
            },
        ),
        migrations.AddConstraint(
            model_name='contact',
            constraint=models.UniqueConstraint(fields=('id_contact', 'date_start_attention'), name='UQ_ID_CONTACT_DATE_ATTENTION'),
        ),
    ]
