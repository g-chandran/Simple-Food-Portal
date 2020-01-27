from django.db import models

class Food(models.Model):
    type_choice = (
        ('Veg','Veg'),
        ('Non-Veg', 'Non-Veg')
    )

    food_name = models.CharField(max_length = 200)
    food_type = models.CharField(max_length = 8, choices=type_choice, default='Veg')
    food_pic = models.ImageField(upload_to='food_pics', default='default.jpg')
    food_description = models.TextField()
    order_count = models.IntegerField(default='0')
    food_price = models.IntegerField(default='100')

    def __str__(self):
        return self.food_name
