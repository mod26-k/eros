from django.db import models
from django import forms
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
# from datetime import date
from django.contrib.auth.models import User
# from datetime import datetime


class DateIdeas(models.Model):
    restaurant = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    meal = models.CharField(
        choices = (
            ('Brunch', 'Brunch'), ('Lunch', 'Lunch'), (
        'Dinner', 'Dinner')
            ),
            default = 'Dinner',
        )
    date = models.DateField()
    # time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    def get_absolute_url(self):
        return reverse('dateideas_list', )
    

class Pfp(models.Model):
    url = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    dateideas = models.ManyToManyField(DateIdeas)
    name = models.CharField(max_length = 50)
    pronouns = models.CharField(max_length = 50)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(99)])
    location = models.CharField(
        max_length = 50,
        )
    occupation = models.CharField(
        max_length = 50,
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

    def __str__(self):
        return f"{self.user.username}'s Profile"

