from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        fields = ['full_name', 'email', 'age','interest']
        exclude = ['last_update']
        model = Student

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 120:
            raise forms.ValidationError("You may be too old for this class")
        return age
