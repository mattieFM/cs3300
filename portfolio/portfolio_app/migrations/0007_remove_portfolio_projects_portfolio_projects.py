# Generated by Django 4.2 on 2024-03-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_alter_portfolio_projects_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='projects',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='projects',
            field=models.ManyToManyField(related_name='studentProjects', to='portfolio_app.project'),
        ),
    ]
