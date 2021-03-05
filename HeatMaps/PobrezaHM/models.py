# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models

class Cantones(models.Model):
    geom = models.MultiPolygonField(srid=32717, blank=True, null=True)
    dpa_anio = models.CharField(max_length=4, blank=True, null=True)
    dpa_canton = models.CharField(max_length=20, blank=True, null=True)
    dpa_provin = models.CharField(max_length=20, blank=True, null=True)
    dpa_despro = models.CharField(max_length=40, blank=True, null=True)
    dpa_descan = models.CharField(max_length=40, blank=True, null=True)
    regional = models.CharField(max_length=10, blank=True, null=True)
    areakm2 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"id: {self.dpa_canton} - Canton: {self.dpa_descan}"

    class Meta:
        managed = False
        db_table = 'cantones'



class Parroquias(models.Model):
    geom = models.MultiPolygonField(srid=32717, blank=True, null=True)
    dpa_parroq = models.CharField(max_length=20, blank=True, null=True)
    dpa_despar = models.CharField(max_length=40, blank=True, null=True)
    dpa_valor = models.IntegerField(blank=True, null=True)
    dpa_anio = models.CharField(max_length=4, blank=True, null=True)
    dpa_canton = models.CharField(max_length=20, blank=True, null=True)
    dpa_provin = models.CharField(max_length=20, blank=True, null=True)
    dpa_despro = models.CharField(max_length=40, blank=True, null=True)
    dpa_descan = models.CharField(max_length=40, blank=True, null=True)
    regional = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"id: {self.dpa_parroq} - Parroquia: {self.dpa_despar}"

    class Meta:
        managed = False
        db_table = 'parroquias'


class Provincias(models.Model):
    geom = models.MultiPolygonField(srid=32717, blank=True, null=True)
    dpa_anio = models.CharField(max_length=4, blank=True, null=True)
    dpa_provin = models.CharField(max_length=20, blank=True, null=True)
    dpa_despro = models.CharField(max_length=40, blank=True, null=True)
    regional = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"id: {self.dpa_provin} - Provincia: {self.dpa_despro}"

    class Meta:
        managed = False
        db_table = 'provincias'


class Basicdat14(models.Model):
    id = models.IntegerField(primary_key=True)
    numhog = models.BigIntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    ciudad = models.IntegerField(blank=True, null=True)
    zona = models.IntegerField(blank=True, null=True)
    sector = models.IntegerField(blank=True, null=True)
    vivienda = models.IntegerField(blank=True, null=True)
    hogar = models.IntegerField(blank=True, null=True)
    periodo = models.IntegerField(blank=True, null=True)
    fase = models.IntegerField(blank=True, null=True)
    provin = models.IntegerField(blank=True, null=True)
    regiont = models.IntegerField(blank=True, null=True)
    totper = models.IntegerField(blank=True, null=True)
    fexp = models.FloatField(blank=True, null=True)
    facper = models.FloatField(blank=True, null=True)
    deflac = models.FloatField(blank=True, null=True)
    ajustem2 = models.FloatField(blank=True, null=True)
    cn_01 = models.FloatField(blank=True, null=True)
    cn_02 = models.FloatField(blank=True, null=True)
    cn_03 = models.FloatField(blank=True, null=True)
    cn_04 = models.FloatField(blank=True, null=True)
    cn_05 = models.FloatField(blank=True, null=True)
    cn_06 = models.FloatField(blank=True, null=True)
    cn = models.FloatField(blank=True, null=True)
    ca = models.FloatField(blank=True, null=True)
    adjcap = models.FloatField(blank=True, null=True)
    li_2014 = models.FloatField(blank=True, null=True)
    engel_t = models.FloatField(blank=True, null=True)
    lp_2014 = models.FloatField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    indigent = models.IntegerField(blank=True, null=True)
    pobre = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basicdat14'


class Cantonal(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_canton = models.CharField(max_length=50, blank=True, null=True)
    no_pobres_num = models.IntegerField(blank=True, null=True)
    pobres_num = models.IntegerField(blank=True, null=True)
    total_num = models.IntegerField(blank=True, null=True)
    no_pobres_porc = models.FloatField(blank=True, null=True)
    pobres_porc = models.FloatField(blank=True, null=True)
    total_porc = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Cantón: {self.nombre_canton}"

    class Meta:
        managed = False
        db_table = 'cantonal'


class Parroquial(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_parroquia = models.CharField(max_length=50, blank=True, null=True)
    no_pobres_num = models.IntegerField(blank=True, null=True)
    pobres_num = models.IntegerField(blank=True, null=True)
    total_num = models.IntegerField(blank=True, null=True)
    no_pobres_porc = models.FloatField(blank=True, null=True)
    pobres_porc = models.FloatField(blank=True, null=True)
    total_porc = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Parroquia: {self.nombre_parroquia}"

    class Meta:
        managed = False
        db_table = 'parroquial'


class Provincial(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre_provincia = models.CharField(max_length=50, blank=True, null=True)
    no_pobres_num = models.IntegerField(blank=True, null=True)
    pobres_num = models.IntegerField(blank=True, null=True)
    total_num = models.IntegerField(blank=True, null=True)
    no_pobres_porc = models.FloatField(blank=True, null=True)
    pobres_porc = models.FloatField(blank=True, null=True)
    total_porc = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Provincia: {self.nombre_provincia}"

    class Meta:
        managed = False
        db_table = 'provincial'
