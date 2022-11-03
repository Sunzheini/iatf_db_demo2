from django import forms


class ProcessForm(forms.Form):
    step_name = forms.CharField(
        label='Step Name', max_length=30,
    )

    responsible = forms.CharField(
        label='Responsible', max_length=30,
    )

    evidence = forms.CharField(
        label='Evidence', max_length=30,
    )
