from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from datetime import date
# from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    pronouns = models.CharField(max_length = 50)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    height_feet = models.CharField(
        max_length = 1,
        choices = (
            ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8','8'), ('9', '9'),
        ),
        default = '5'
    )
    height_inches = models.CharField(
        max_length = 2,
        choices = (
            ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8','8'), ('9', '9'), ('10', '10'), ('11', '11'),
        ),
        default = '0'
    )
    zodiac_sign = models.CharField(
        max_length = 11,
        choices = (
        ('Aries', 'Aries'), ('Taurus', 'Taurus'), ('Gemini', 'Gemini'), ('Cancer', 'Cancer'), ('Leo', 'Leo'), ('Virgo', 'Virgo'), ('Libra', 'Libra'), ('Scorpio', 'Scorpio'), ('Sagittarius', 'Sagittarius'), ('Capricorn', 'Capricorn'), ('Aquarius', 'Aquarius'), ('Pisces', 'Pisces'),
        ),
        default = 'Aries',
    )

class DateIdeas(models.Model):
    location = models.CharField()
    meal = models.CharField(
        choices = (
            ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), (
        'Dinner', 'Dinner')
            ),
            default = 'Dinner',
        )
    # date = models.DateField('Date:')
    # time = models.DateTimeField('Time:')
    
    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return reverse('date_ideas_details')