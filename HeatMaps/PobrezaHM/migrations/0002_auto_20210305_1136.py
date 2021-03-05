# Generated by Django 3.1.4 on 2021-03-05 11:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PobrezaHM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basicdat14',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('numhog', models.BigIntegerField(blank=True, null=True)),
                ('area', models.IntegerField(blank=True, null=True)),
                ('ciudad', models.IntegerField(blank=True, null=True)),
                ('zona', models.IntegerField(blank=True, null=True)),
                ('sector', models.IntegerField(blank=True, null=True)),
                ('vivienda', models.IntegerField(blank=True, null=True)),
                ('hogar', models.IntegerField(blank=True, null=True)),
                ('periodo', models.IntegerField(blank=True, null=True)),
                ('fase', models.IntegerField(blank=True, null=True)),
                ('provin', models.IntegerField(blank=True, null=True)),
                ('regiont', models.IntegerField(blank=True, null=True)),
                ('totper', models.IntegerField(blank=True, null=True)),
                ('fexp', models.FloatField(blank=True, null=True)),
                ('facper', models.FloatField(blank=True, null=True)),
                ('deflac', models.FloatField(blank=True, null=True)),
                ('ajustem2', models.FloatField(blank=True, null=True)),
                ('cn_01', models.FloatField(blank=True, null=True)),
                ('cn_02', models.FloatField(blank=True, null=True)),
                ('cn_03', models.FloatField(blank=True, null=True)),
                ('cn_04', models.FloatField(blank=True, null=True)),
                ('cn_05', models.FloatField(blank=True, null=True)),
                ('cn_06', models.FloatField(blank=True, null=True)),
                ('cn', models.FloatField(blank=True, null=True)),
                ('ca', models.FloatField(blank=True, null=True)),
                ('adjcap', models.FloatField(blank=True, null=True)),
                ('li_2014', models.FloatField(blank=True, null=True)),
                ('engel_t', models.FloatField(blank=True, null=True)),
                ('lp_2014', models.FloatField(blank=True, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('indigent', models.IntegerField(blank=True, null=True)),
                ('pobre', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'basicdat14',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cantonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('nombre_canton', models.CharField(blank=True, max_length=50, null=True)),
                ('no_pobres_num', models.IntegerField(blank=True, null=True)),
                ('pobres_num', models.IntegerField(blank=True, null=True)),
                ('total_num', models.IntegerField(blank=True, null=True)),
                ('no_pobres_porc', models.FloatField(blank=True, null=True)),
                ('pobres_porc', models.FloatField(blank=True, null=True)),
                ('total_porc', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cantonal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cantones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32717)),
                ('dpa_anio', models.CharField(blank=True, max_length=4, null=True)),
                ('dpa_canton', models.CharField(blank=True, max_length=20, null=True)),
                ('dpa_provin', models.CharField(blank=True, max_length=20, null=True)),
                ('dpa_despro', models.CharField(blank=True, max_length=40, null=True)),
                ('dpa_descan', models.CharField(blank=True, max_length=40, null=True)),
                ('regional', models.CharField(blank=True, max_length=10, null=True)),
                ('areakm2', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cantones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('nombre_parroquia', models.CharField(blank=True, max_length=50, null=True)),
                ('no_pobres_num', models.IntegerField(blank=True, null=True)),
                ('pobres_num', models.IntegerField(blank=True, null=True)),
                ('total_num', models.IntegerField(blank=True, null=True)),
                ('no_pobres_porc', models.FloatField(blank=True, null=True)),
                ('pobres_porc', models.FloatField(blank=True, null=True)),
                ('total_porc', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parroquial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parroquias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32717)),
                ('dpa_parroq', models.CharField(blank=True, max_length=20, null=True)),
                ('dpa_despar', models.CharField(blank=True, max_length=40, null=True)),
                ('dpa_valor', models.IntegerField(blank=True, null=True)),
                ('dpa_anio', models.CharField(blank=True, max_length=4, null=True)),
                ('dpa_canton', models.CharField(blank=True, max_length=20, null=True)),
                ('dpa_provin', models.CharField(blank=True, max_length=20, null=True)),
                ('dpa_despro', models.CharField(blank=True, max_length=40, null=True)),
                ('dpa_descan', models.CharField(blank=True, max_length=40, null=True)),
                ('regional', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'parroquias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(blank=True, null=True)),
                ('nombre_provincia', models.CharField(blank=True, max_length=50, null=True)),
                ('no_pobres_num', models.IntegerField(blank=True, null=True)),
                ('pobres_num', models.IntegerField(blank=True, null=True)),
                ('total_num', models.IntegerField(blank=True, null=True)),
                ('no_pobres_porc', models.FloatField(blank=True, null=True)),
                ('pobres_porc', models.FloatField(blank=True, null=True)),
                ('total_porc', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'provincial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=32717)),
                ('dpa_anio', models.CharField(blank=True, max_length=4, null=True)),
                ('dpa_provin', models.CharField(blank=True, max_length=20, null=True)),
                ('dpa_despro', models.CharField(blank=True, max_length=40, null=True)),
                ('regional', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'provincias',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AuthGroup',
        ),
        migrations.DeleteModel(
            name='AuthGroupPermissions',
        ),
        migrations.DeleteModel(
            name='AuthPermission',
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
        migrations.DeleteModel(
            name='AuthUserGroups',
        ),
        migrations.DeleteModel(
            name='AuthUserUserPermissions',
        ),
        migrations.DeleteModel(
            name='DjangoAdminLog',
        ),
        migrations.DeleteModel(
            name='DjangoContentType',
        ),
        migrations.DeleteModel(
            name='DjangoMigrations',
        ),
        migrations.DeleteModel(
            name='DjangoSession',
        ),
        migrations.DeleteModel(
            name='EventosCantones',
        ),
        migrations.DeleteModel(
            name='FuentesAgua',
        ),
        migrations.RemoveField(
            model_name='layer',
            name='topology',
        ),
        migrations.DeleteModel(
            name='TablaPuntos',
        ),
        migrations.DeleteModel(
            name='Layer',
        ),
        migrations.DeleteModel(
            name='Topology',
        ),
    ]
