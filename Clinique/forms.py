from django import forms
from django.contrib.auth.models import User
from . import models



class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['profile_pic','address','mobile','specialite','status','Htravail','Occu']


class Doctorxy(forms.ModelForm):
    class Meta:
        model=models.Doctor       
        fields=['profile_pic','address','mobile','specialite','status','x','y','Htravail','Occu']



#for teacher related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }


class PatientForm(forms.ModelForm):
     class Meta:
        model=models.Patient
        fields=['address','mobile','status','profile_pic']


    

class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Docteur Nom et specialite", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Nom", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['symptoms','status']




class PatientAppointmentEnligneForm(forms.ModelForm):
   # Drspecialite=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True).order_by().values_list('specialite').distinct(),empty_label="Specialite", to_field_name="user_id")
   # idDec=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True).distinct(),empty_label="Specialite", to_field_name="user_id")
    #idDec=forms.ModelChoiceField(queryset=models.Doctor.objects.filter(status=True).values_list('specialite').order_by('specialite').distinct(),empty_label="Specialite", to_field_name="user_id")


    #Drspecialite=forms.ModelChoiceField(queryset=models.Doctoro.bjects.raw('SELECT specialite FROM Doctor;'),empty_label="Specialite", to_field_name="user_id")
    #Person.objects.raw('SELECT id, first_name, last_name, birth_date FROM myapp_person')
    class Meta:
        model=models.Doctor
        fields=['specialite']



class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label=" Docteur Nom et specialite", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['symptoms','status']


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


