# Generated by Django 5.0 on 2023-12-11 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0008_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
    ]
