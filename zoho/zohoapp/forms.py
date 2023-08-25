# forms.py
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=100)
    #attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'text-light', 'multiple': True}))
    message = forms.CharField(widget=forms.Textarea)

# Rijin

from django import forms
from .models import Loan, Employee

class LoanForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        empty_label="Select an employee"
    )
    loan_amount = forms.DecimalField()
    loan_issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    loan_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    monthly_cutting_type = forms.ChoiceField(
        choices=[('%', '%'), ('amount', 'Amount')],
        initial='%'
    )

    class Meta:
        model = Loan
        fields = '__all__'
