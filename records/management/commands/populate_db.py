from django.core.management.base import BaseCommand
from records.models import Patient, Drug, Treatment
from datetime import date
import random

class Command(BaseCommand):
    help = 'Populate the database with mock data'

    def handle(self, *args, **kwargs):
        self.create_patients()
        self.create_drugs()
        self.create_treatments()

    def create_patients(self):
        Patient.objects.all().delete()
        patients = [
            {"first_name": "John", "last_name": "Doe", "date_of_birth": date(1980, 5, 14)},
            {"first_name": "Jane", "last_name": "Doe", "date_of_birth": date(1990, 7, 23)},
            {"first_name": "Jim", "last_name": "Beam", "date_of_birth": date(1975, 8, 30)},
            {"first_name": "Jack", "last_name": "Daniels", "date_of_birth": date(1985, 2, 20)},
            {"first_name": "Johnny", "last_name": "Walker", "date_of_birth": date(1992, 3, 25)},
        ]
        for patient_data in patients:
            Patient.objects.create(**patient_data)
        self.stdout.write(self.style.SUCCESS('Successfully created patients'))

    def create_drugs(self):
        Drug.objects.all().delete()
        drugs = [
            {"name": "Aspirin", "description": "Pain reliever and fever reducer"},
            {"name": "Ibuprofen", "description": "Nonsteroidal anti-inflammatory drug"},
            {"name": "Paracetamol", "description": "Analgesic and antipyretic"},
            {"name": "Amoxicillin", "description": "Antibiotic for bacterial infections"},
            {"name": "Lisinopril", "description": "Medication for high blood pressure"},
        ]
        for drug_data in drugs:
            Drug.objects.create(**drug_data)
        self.stdout.write(self.style.SUCCESS('Successfully created drugs'))

    def create_treatments(self):
        Treatment.objects.all().delete()
        patients = list(Patient.objects.all())
        drugs = list(Drug.objects.all())
        treatments = [
            {"patient": random.choice(patients), "drug": random.choice(drugs), "start_date": date(2024, 1, 1), "end_date": date(2024, 1, 10), "dosage": "1 tablet daily"},
            {"patient": random.choice(patients), "drug": random.choice(drugs), "start_date": date(2024, 2, 1), "end_date": date(2024, 2, 10), "dosage": "2 tablets daily"},
            {"patient": random.choice(patients), "drug": random.choice(drugs), "start_date": date(2024, 3, 1), "end_date": date(2024, 3, 10), "dosage": "1 tablet twice daily"},
            {"patient": random.choice(patients), "drug": random.choice(drugs), "start_date": date(2024, 4, 1), "end_date": date(2024, 4, 10), "dosage": "3 tablets daily"},
            {"patient": random.choice(patients), "drug": random.choice(drugs), "start_date": date(2024, 5, 1), "end_date": date(2024, 5, 10), "dosage": "1 tablet every 8 hours"},
        ]
        for treatment_data in treatments:
            Treatment.objects.create(**treatment_data)
        self.stdout.write(self.style.SUCCESS('Successfully created treatments'))
