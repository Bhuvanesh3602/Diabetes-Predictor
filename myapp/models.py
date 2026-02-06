from django.db import models

class Prediction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.FloatField()
    outcome = models.IntegerField()
    risk_level = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        ordering = ['-timestamp']
        db_table = 'diabetes_predictions'
    
    def __str__(self):
        return f"Prediction {self.id} - {self.timestamp}"
