# Generated by Django 2.2.5 on 2020-01-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('food_type', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], default='Veg', max_length=8)),
                ('food_pic', models.ImageField(default='default.jpg', upload_to='food_pics')),
                ('food_description', models.TextField()),
                ('order_count', models.IntegerField(default='0')),
                ('food_price', models.IntegerField(default='100')),
            ],
        ),
    ]
