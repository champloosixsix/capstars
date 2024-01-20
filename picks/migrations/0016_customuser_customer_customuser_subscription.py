# Generated by Django 5.0 on 2024-01-13 02:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0012_2_8'),
        ('picks', '0015_alter_picks_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='customer',
            field=models.ForeignKey(blank=True, help_text="The user's Stripe Customer object, if it exists", null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.customer'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscription',
            field=models.ForeignKey(blank=True, help_text="The user's Stripe Subscription object, if it exists", null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.subscription'),
        ),
    ]