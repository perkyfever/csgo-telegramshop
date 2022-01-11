# Generated by Django 4.0.1 on 2022-01-11 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopmanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='feedback_rate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='feedback_text',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='purchased',
            field=models.IntegerField(default=0),
        ),
    ]