from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from datetime import date
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    pronouns = models.CharField(max_length = 50)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    location = models.CharField(
        max_length = 50,
        # default = 'Not Disclosed'
        )
    occupation = models.CharField(
        max_length = 50,
        # default = 'Not Disclosed',
        )
    relationship_status = models.CharField(
        choices = (
        ('Single', 'Single'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Open Relationship', 'Open Relationship')
        ),
        default = 'Single',
    )
        
    height_feet = models.CharField(
        choices = (
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8','8'), ('9', '9'),
        ),
        default = '5'
    )
    height_inches = models.CharField(
        choices = (
            ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8','8'), ('9', '9'), ('10', '10'), ('11', '11'),
        ),
        default = '0'
    )
    zodiac_sign = models.CharField(
        choices = (
        ('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces'),
        ),
        null=True,
        blank=True,
    )
    smoke = models.CharField(
        choices = (
            ('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')
        ),
        null=True,
        blank=True,
    )
    drink = models.CharField(
        choices = (
            ('Yes', 'Yes'), ('No', 'No'), ('Occasionally', 'Occasionally')
        ),
        null=True,
        blank=True,
    )
    children = models.CharField(
        choices = (
            ('Yes', 'Yes'), ('No', 'No')
        ),
        null=True,
        blank=True,
    )
    religion = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    dealbreaker = models.TextField(
        null=True, 
        blank=True
    )

    fun_date_idea = models.TextField(
        null=True, 
        blank=True
    )



class DateIdeas(models.Model):
    location = models.CharField(max_length=50)
    meal = models.CharField(
        choices = (
            ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), (
        'Dinner', 'Dinner')
            ),
            default = 'Dinner',
        )
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        null = True
        )
    
    # def __str__(self):
    #     return self.name
    
    # def get_absolute_url(self):
    #     return reverse('date_ideas_details')