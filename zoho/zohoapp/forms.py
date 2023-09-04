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
from django.core.validators import MinValueValidator, MaxValueValidator


class LoanForm(forms.ModelForm):
    employee = forms.ModelChoiceField(
        queryset=Payroll.objects.all(),
        empty_label="Select an employee"
    )
    loan_amount = forms.DecimalField()
    loan_issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    loan_expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    payment_method = forms.ChoiceField(
        choices=[('percentage', 'Percentage Wise'), ('amount', 'Amount Wise')],
        initial='percentage'
    )

    # Define these fields based on the selected payment method
    monthly_cutting_percentage = forms.DecimalField(
        label="Monthly Cutting Percentage (%)",
        required=False,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )
    monthly_cutting_amount = forms.DecimalField(
        label="Monthly Cutting Amount (INR)",
        required=False,
    )

    class Meta:
        model = Loan
        fields = '__all__'


