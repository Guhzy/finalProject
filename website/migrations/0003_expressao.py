# Generated by Django 3.2.2 on 2021-05-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_maquina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expressao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('regex', models.CharField(max_length=100)),
            ],
        ),
    ]
