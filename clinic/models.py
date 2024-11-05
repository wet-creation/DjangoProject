from django.db import models


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('ent', 'ENT'),
        ('therapist', 'Therapist'),
        ('surgeon', 'Surgeon'),
    ]

    doctor_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    experience_years = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    CATEGORY_CHOICES = [
        ('child', 'Child'),
        ('adult', 'Adult'),
    ]

    patient_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_year = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Stay(models.Model):
    stay_id = models.AutoField(primary_key=True)
    admission_date = models.DateField()
    stay_days = models.IntegerField()
    daily_cost = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=3, decimal_places=2)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"Stay ID: {self.stay_id} for {self.patient.first_name}"
