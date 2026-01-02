from django.db import models
from .enums import Category
from django.core.exceptions import ValidationError
from django.db.models import Q, F
from django.utils import timezone
import datetime

valid_categories = [choice[0] for choice in Category.choices]

class Announcement(models.Model):
    content = models.CharField()
    category = models.CharField(choices=Category.choices)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'Content: {self.content}; Category: {self.category}'
    
    def is_active(self):
        return timezone.now() < self.end_date

    def clean(self): # Python-level validation
        if self.category not in valid_categories:
            raise ValidationError(f'"{self.category}" is not a valid category')
        
        if self.start_date > self.end_date or self.start_date < timezone.now():
            raise ValidationError('Date is invalid')
        
        return super().clean()
    
    def save(self):
        self.full_clean()
        return super().save()
    
    class Meta: # Database-level validation
        constraints = [
            models.CheckConstraint(
                condition=Q(category__in=valid_categories),
                name='category_validation'
            ),
            models.CheckConstraint(
                condition=(Q(start_date__lt=F('end_date')) & Q(start_date__gte=timezone.now())),
                name='date_validation'
            ),
        ]
        
    
