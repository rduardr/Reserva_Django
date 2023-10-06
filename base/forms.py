from django import forms
from django.core.validators import RegexValidator


class ReservaForm(forms.Form):
    nome_do_pet = forms.CharField()
    telefone = forms.CharField(
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="O campo deve conter 11 dígitos sem espaço (incluindo o DDD).",
                code="invalid_phone",
            )
        ]
    )
    dia_do_banho = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "ex: 01/01"}),
        required=True,
    )
    observacoes = forms.CharField(widget=forms.Textarea)
