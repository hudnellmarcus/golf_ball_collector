# Generated by Django 4.0.5 on 2022-07-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf_ball_app', '0002_alter_attribute_feel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ball',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]