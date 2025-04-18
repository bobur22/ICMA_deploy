from django import forms
from .models import *
from .validators import validate_email, PhoneValidator, validate_f_name, validate_date


class PassportForm(forms.ModelForm):
    class Meta:
        model = Passport
        fields = ('p_fname', 'p_code', 'p_email', 'given_date')
        widgets = {
            'p_fname': forms.TextInput(
                attrs={
                    # 'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter', 'id': 'formGroupExampleInput',
                    'placeholder': 'Full Name',
                    'name': "f_name"}),
            'p_email': forms.EmailInput(
                attrs={
                    # 'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                    'id': 'formGroupExampleInput2',
                    'placeholder': 'Email',
                    'name': "email"}),
            'p_code': forms.TextInput(
                attrs={
                    # 'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                    'id': 'formGroupExampleInput3',
                    'placeholder': 'Phone Number',
                    'name': "code"}),
            'given_date': forms.DateInput(
                attrs={
                    # 'class': 'form-control py-3 ps-4 font_fv font_style_b fw-lighter',
                    'id': 'formGroupExampleInput8',
                    'placeholder': 'Berilgan sana',
                    'name': "date"}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
