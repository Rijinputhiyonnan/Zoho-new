# forms.py
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    #attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'text-light', 'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)

# Rijin

from django import forms
from .models import Loan, Payroll

class LoanForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Payroll.objects.all(),
        empty_label="Select an employee"
    )
    loan_amount = forms.DecimalField()
    date_issue = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Issue Date")
    date_expiry = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Expiry Date")
    monthly_cutting_type = forms.ChoiceField(
        choices=[('%', '%'), ('amount', 'Amount')],
        initial='%'
    )

    class Meta:
        model = Loan
        fields = '__all__'

