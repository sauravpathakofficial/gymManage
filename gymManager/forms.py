from django.forms import ModelForm
from django import forms 
from .models import GymMembership,GymMember

class createMembership(ModelForm):
    membership=forms.CharField()
    instructor = forms.CharField()
    time=forms.CharField()
    capacity = forms.IntegerField()
    class Meta:
        model=GymMembership
        fields=['membership','instructor','time','capacity']


class createMember(ModelForm):
    name = forms.CharField()
    email= forms.EmailField()
    phone=forms.IntegerField()
    membership = forms.ModelChoiceField(queryset=GymMembership.objects.all(), widget=forms.Select, required=False)
    class Meta:
        model=GymMember
        fields=['name','email','phone','membership']
        
