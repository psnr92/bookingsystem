# Generated by Django 3.0.9 on 2020-08-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('A', 'A-Gebäude'), ('B', 'B-Gebäude'), ('C', 'C-Gebäude'), ('D', 'D-Gebäude'), ('E', 'E-Gebäude')], default='A', max_length=1),
            preserve_default=False,
        ),
    ]
