# Generated by Django 4.0.4 on 2022-06-27 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property_app', '0003_company_property_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AddField(
            model_name='property',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Property', to='property_app.company'),
            preserve_default=False,
        ),
    ]
