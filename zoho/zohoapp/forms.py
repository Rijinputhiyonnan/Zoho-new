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
    loan_issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    loan_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    payment_method = forms.ChoiceField(
        choices=[('percentage_wise', 'Percentage Wise'), ('amount_wise', 'Amount Wise')],
        initial='percentage_wise'
    )
    cutting_value = forms.DecimalField()

    class Meta:
        model = Loan
        fields = '__all__'


