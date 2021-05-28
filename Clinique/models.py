from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
from json import dumps
import datetime

specialites=[('pediatrie','pediatrie'),
('Ophtalmologie','Ophtalmologie'),
('Urologie','Urologie'),
('Psychiatrie','Psychiatrie'),
('Endocrinologie','Endocrinologie'),
('Gastro Entérologie','Gastro Entérologie'),
('Dermatologie','Dermatologie'),
('Neurologie','Neurologie'),
('Cardiologie','Cardiologie'),
('ORL','ORL'),
('medecin-general','medecin-general'),
('Rhumatologie ','Rhumatologie ')
]


class Pharmacie(models.Model):
  longitude = models.FloatField(default=0)
  latitude = models.FloatField(default=0)

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    specialite = models.CharField(max_length=50,choices=specialites,default='medecin-general')
    status = models.BooleanField(default=False)
    x=models.FloatField(null=True)
    y=models.FloatField(null=True)
    Htravail= models.PositiveIntegerField(default=4)
    Occu = models.TimeField(default=datetime.time(8))

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.specialite)
        #return self.specialite

symtomes=[('fievre chez les enfants,la diarrhée,les vomissements...','fievre chez les enfants,la diarrhée,les vomissements..'),
('deficite respiratoire','deficite respiratoire'),
('Douleur oculaire violente et subite,Baisse brutale de la vision d\'un œil ou de l\'autre...','Baisse brutale de la vision d\'un œil ou de l\'autre'),
('Anurie,Anérection,Anéjaculation,Azoospermie...','Anurie,Anérection,Anéjaculation,Azoospermie...'),
('Hyperactivité,Agitation...','Hyperactivité,Agitation...'),('perte ou prise de poids inexpliquée, fatigue, douleurs, troubles de l’humeur... ','perte ou prise de poids inexpliquée, fatigue, douleurs, troubles de l’humeur... '),('les vomissements,la perte d\'appétit,la diarrhée...','les vomissements,la perte d\'appétit,la diarrhée...'),
('Bouton sur le corp,Eruption Cutannee,Rash cutanee...','Bouton sur le corp,Eruption Cutannee,Rash cutanee...'),
('Douleur dorsale,Tremblements...','Douleur dorsale,Tremblements...'),
('Palpitations ,Sensation de vertige...','Palpitations ,Sensation de vertige...'),
('rhume,bouchon de cérumen,angine...','rhume,bouchon de cérumen,angine...'),
('mal de dos, rhumatismes, arthrose, fibromylagie...','mal de dos, rhumatismes, arthrose, fibromylagie...'),
('Fièvre,maux de tete...','Fièvre,maux de tete...')

]

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    appointmentDate=models.DateField(auto_now=True)

    symptoms = models.CharField(max_length=100,choices=symtomes,default='Fièvre,maux de tete...',null=False)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    releaseDate=models.DateField(null=False)    
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)
