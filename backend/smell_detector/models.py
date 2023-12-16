from django.db import models

class Smell(models.Model):
    name = models.CharField()
    category = models.CharField()
    fix = models.TextField()
    line_number = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} smell at line number {self.line_number}"
