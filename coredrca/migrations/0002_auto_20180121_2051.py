# Generated by Django 2.0.1 on 2018-01-21 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coredrca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, to='coredrca.Disciplina'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='d_requisito',
            field=models.ManyToManyField(blank=True, to='coredrca.Disciplina'),
        ),
    ]