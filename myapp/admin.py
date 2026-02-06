from django.contrib import admin
from .models import Prediction

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'glucose', 'bmi', 'age', 'outcome', 'risk_level']
    list_filter = ['outcome', 'risk_level', 'timestamp']
    search_fields = ['id']
    ordering = ['-timestamp']
