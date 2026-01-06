from django import forms
from .models import Student,Guardian

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'address', 'classroom']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'classroom': forms.Select(attrs={'class': 'form-control'}), 
        }
class GuardianForm(forms.ModelForm):
    class Meta:
        model=Guardian
        fields=['name','phone','relation']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'relation': forms.TextInput(attrs={'class': 'form-control'}),
        }
