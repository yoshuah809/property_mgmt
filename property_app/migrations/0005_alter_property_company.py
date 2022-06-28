# Generated by Django 4.0.4 on 2022-06-27 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0004_alter_company_options_property_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='property', to='property_app.company'),
        ),
    ]