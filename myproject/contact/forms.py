from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """
    Formulario para el registro de un contacto con los servicios de salud
    """
    class Meta:
        model = Contact
        fields = [
            'cod_borr', 'modality_of_realization_it',  'it_groups', 'env_attention',
            'way_of_entry', 'cause_of_care', 'classification_triage', 'diagnosis_of_admission',
            'type_of_diagnosis'
        ]
        labels = {
            'cod_borr': 'Código del prestador ',
            'modality_of_realization_it': 'Modalidad de realización de la TI en salud',
            'it_groups': 'Grupos de servicios de TI en salud',
            'env_attention': 'Entorno de atención',
            'way_of_entry': 'Vía de ingreso',
            'cause_of_care': 'Causa de la atención',
            'classification_triage': 'Clasificación de triage',
            'diagnosis_of_admission': 'Diagnóstico de ingreso',
            'type_of_diagnosis': 'Tipo de diagnóstico'
        }
        widgets = {
            'cod_borr': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'modality_of_realization_it': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'it_groups': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'env_attention': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'way_of_entry': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cause_of_care': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'classification_triage': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'diagnosis_of_admission': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'type_of_diagnosis': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }