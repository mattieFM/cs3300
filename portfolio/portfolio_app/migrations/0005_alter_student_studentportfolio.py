# Generated by Django 4.2 on 2024-03-19 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0004_project_studentportfolio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentPortfolio',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio_app.portfolio'),
        ),
    ]