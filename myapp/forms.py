from django import forms


class StudentForm(forms.Form):
    name=forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class':'name','id':'name'}))
    age=forms.IntegerField(min_value=20,max_value=45,widget=forms.NumberInput(attrs={'class':'age'}))