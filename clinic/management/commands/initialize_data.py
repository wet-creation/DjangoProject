from django.core.management.base import BaseCommand
from clinic.models import Doctor, Patient, Stay
from datetime import date

class Command(BaseCommand):
    help = 'Initialize the database with initial clinic data'

    def handle(self, *args, **kwargs):
        # Insert Doctors
        doctors = [
            {"last_name": "Smith", "first_name": "John", "middle_name": "Edward", "specialization": "ent", "experience_years": 10},
            {"last_name": "Doe", "first_name": "Jane", "middle_name": "Marie", "specialization": "therapist", "experience_years": 7},
            {"last_name": "Brown", "first_name": "Michael", "middle_name": "James", "specialization": "surgeon", "experience_years": 15},
            {"last_name": "Johnson", "first_name": "Emily", "middle_name": "Louise", "specialization": "therapist", "experience_years": 5},
        ]
        for doc in doctors:
            Doctor.objects.get_or_create(**doc)

        # Insert Patients
        patients = [
            {"last_name": "Anderson", "first_name": "Alice", "middle_name": "Patricia", "address": "123 Main St", "phone_number": "1234567890", "birth_year": 2001, "category": "child"},
            {"last_name": "White", "first_name": "Chris", "middle_name": "Thomas", "address": "456 Elm St", "phone_number": "2345678901", "birth_year": 1995, "category": "adult"},
            {"last_name": "Davis", "first_name": "Sophia", "middle_name": "Maria", "address": "789 Oak St", "phone_number": "3456789012", "birth_year": 1988, "category": "adult"},
            {"last_name": "Harris", "first_name": "James", "middle_name": "Charles", "address": "101 Pine St", "phone_number": "4567890123", "birth_year": 2010, "category": "child"},
            {"last_name": "Martin", "first_name": "Olivia", "middle_name": "Grace", "address": "102 Maple St", "phone_number": "5678901234", "birth_year": 2003, "category": "child"},
            {"last_name": "Clark", "first_name": "William", "middle_name": "Anthony", "address": "103 Cedar St", "phone_number": "6789012345", "birth_year": 1992, "category": "adult"},
            {"last_name": "Lewis", "first_name": "Ava", "middle_name": "Elizabeth", "address": "104 Birch St", "phone_number": "7890123456", "birth_year": 1985, "category": "adult"},
            {"last_name": "Walker", "first_name": "Noah", "middle_name": "Alexander", "address": "105 Spruce St", "phone_number": "8901234567", "birth_year": 2012, "category": "child"},
            {"last_name": "Young", "first_name": "Emma", "middle_name": "Charlotte", "address": "106 Redwood St", "phone_number": "9012345678", "birth_year": 1999, "category": "adult"},
        ]
        for pat in patients:
            Patient.objects.get_or_create(**pat)

        # Insert Stays
        stays = [
            {"patient_id": 1, "admission_date": date(2023, 9, 15), "stay_days": 5, "daily_cost": 100.00, "discount_percent": 0.10, "doctor_id": 1},
            {"patient_id": 2, "admission_date": date(2023, 9, 16), "stay_days": 3, "daily_cost": 80.00, "discount_percent": 0.00, "doctor_id": 2},
            {"patient_id": 3, "admission_date": date(2023, 9, 17), "stay_days": 7, "daily_cost": 90.00, "discount_percent": 0.15, "doctor_id": 3},
            {"patient_id": 4, "admission_date": date(2023, 9, 18), "stay_days": 4, "daily_cost": 85.00, "discount_percent": 0.05, "doctor_id": 2},
            {"patient_id": 5, "admission_date": date(2023, 9, 19), "stay_days": 6, "daily_cost": 75.00, "discount_percent": 0.20, "doctor_id": 1},
            {"patient_id": 6, "admission_date": date(2023, 9, 20), "stay_days": 2, "daily_cost": 110.00, "discount_percent": 0.00, "doctor_id": 3},
            {"patient_id": 7, "admission_date": date(2023, 9, 21), "stay_days": 3, "daily_cost": 95.00, "discount_percent": 0.00, "doctor_id": 1},
            {"patient_id": 8, "admission_date": date(2023, 9, 22), "stay_days": 5, "daily_cost": 120.00, "discount_percent": 0.10, "doctor_id": 2},
            {"patient_id": 9, "admission_date": date(2023, 9, 23), "stay_days": 4, "daily_cost": 130.00, "discount_percent": 0.05, "doctor_id": 3},
            {"patient_id": 1, "admission_date": date(2023, 9, 24), "stay_days": 3, "daily_cost": 115.00, "discount_percent": 0.00, "doctor_id": 1},
            {"patient_id": 2, "admission_date": date(2023, 9, 25), "stay_days": 2, "daily_cost": 125.00, "discount_percent": 0.00, "doctor_id": 3},
            {"patient_id": 3, "admission_date": date(2023, 9, 26), "stay_days": 5, "daily_cost": 85.00, "discount_percent": 0.10, "doctor_id": 2},
            {"patient_id": 4, "admission_date": date(2023, 9, 27), "stay_days": 7, "daily_cost": 90.00, "discount_percent": 0.15, "doctor_id": 1},
            {"patient_id": 5, "admission_date": date(2023, 9, 28), "stay_days": 4, "daily_cost": 100.00, "discount_percent": 0.20, "doctor_id": 3},
            {"patient_id": 6, "admission_date": date(2023, 9, 29), "stay_days": 6, "daily_cost": 105.00, "discount_percent": 0.05, "doctor_id": 2},
            {"patient_id": 7, "admission_date": date(2023, 9, 30), "stay_days": 2, "daily_cost": 95.00, "discount_percent": 0.00, "doctor_id": 1},
            {"patient_id": 8, "admission_date": date(2023, 10, 1), "stay_days": 3, "daily_cost": 80.00, "discount_percent": 0.00, "doctor_id": 3},
        ]
        for stay in stays:
            Stay.objects.get_or_create(**stay)

        self.stdout.write(self.style.SUCCESS('Successfully initialized the clinic database with sample data'))
