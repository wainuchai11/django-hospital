from django import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Drug(models.Model):
    name = models.  CharField(max_length=100)
    designation = models.TextField()

    def _str_(self):
        return self.name
    
class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    dosage = models.CharField(max_length=100)

    def __str__(self):
        return f"Treatment of {self.patient} with {self.drug}"
