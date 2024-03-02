# Generated by Django 4.2 on 2024-03-02 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_remove_project_studentportfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='studentReference',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.student'),
        ),
        migrations.AddField(
            model_name='project',
            name='studentReference',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.student'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='projects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='studentProjects', to='portfolio_app.project'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentPortfolio',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio_app.portfolio'),
        ),
    ]