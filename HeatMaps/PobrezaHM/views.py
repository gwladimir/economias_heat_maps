from django.shortcuts import render, HttpResponse
from django.db import connection
import folium
from PobrezaHM.models import Provincias
import geopandas as gpd
import pandas as pd

# Create your views here.
def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def mapa(request):

    cursor = connection.cursor()
    cursor1 = connection.cursor()
    #cursor.execute("select dpa_provin, dpa_despro from provincias where dpa_provin != '90' order by dpa_despro;")
    #cursor.execute("SELECT dpa_despro, st_x(st_transform(st_centroid(geom),4326)) as x , st_y(st_transform(st_centroid(geom),4326)) as y FROM limites.provincias where dpa_provin != '90' order by dpa_despro;")
    #cursor.execute("SELECT dpa_despro, st_x(st_transform(st_centroid(geom),4326)) as x , st_y(st_transform(st_centroid(geom),4326)) as y FROM limites.provincias where dpa_despro = 'PICHINCHA';")
    
    #Select para mapa de puntos
    cursor.execute("SELECT p.dpa_despro, st_x(st_transform(st_centroid(p.geom),4326)) as x ,st_y(st_transform(st_centroid(p.geom),4326)) as y, c.pobres_porc FROM limites.provincias p, censo10.provincial c where p.dpa_provin != '90' and p.dpa_despro = c.nombre_provincia order by p.dpa_despro;")
    #Select de pobreza provincial
    cursor1.execute("select st_transform(geom,4326), dpa_anio,dpa_provin,dpa_despro,regional from limites.provincias;")
    

    r = dictfetchall(cursor)
    r1 = dictfetchall(cursor1)

    #df = pd.DataFrame(list(r1))
    
    
    #mapa del mundo
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    print(world.head())


    #Mapa
    primero = r[0]
    locacion = [primero['y'], primero['x']]

    m = folium.Map(
        Location = locacion,
        tiles = 'Stamen Toner',
        zoom_start = 100
    )

    #marcador
    color = ''
    for i in r:
        if i['pobres_porc'] <= 0.3:
            color = 'green'
        elif i['pobres_porc'] > 0.3 and i['pobres_porc'] <= 0.4:
            color = 'yellow'
        elif i['pobres_porc'] > 0.4 and i['pobres_porc'] <= 0.6:
            color= 'blue'
        else:
            color = 'red'
        folium.Marker(
        (i['y'],i['x']),
        tooltip='Clic para ver',
        popup="Provincia: " + i['dpa_despro'] + " Pobreza: " + str(i['pobres_porc']) + "%",
        icon=folium.Icon(color)
        ).add_to(m)

    m = m._repr_html_()

    context = {
        'provin': r,
        'mapa': m
    }

    return render(request, "PobrezaHM/mapa.html",context)