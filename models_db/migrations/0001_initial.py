# Generated by Django 4.1.4 on 2022-12-25 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Origen_Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=500)),
                ('direccion', models.CharField(max_length=500)),
                ('cantidad_reproducciones', models.PositiveIntegerField(default=0)),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='models_db.estado_video')),
                ('id_origen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='models_db.origen_video')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
