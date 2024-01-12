# Generated by Django 5.0 on 2023-12-17 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0009_alter_customuser_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_date', models.DateField(verbose_name='pickdate')),
                ('pick_time', models.TimeField(verbose_name='picktime')),
                ('category', models.CharField(choices=[('NFL', 'NFL'), ('NBA', 'NBA'), ('NCAAF', 'NCAAF'), ('NCAAM', 'NCAAM'), ('UFC', 'UFC')], default='NFL', max_length=5)),
                ('pick', models.CharField(max_length=200)),
            ],
        ),
    ]
