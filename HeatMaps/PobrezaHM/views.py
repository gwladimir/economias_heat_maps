from django.shortcuts import render, HttpResponse
from django.db import connection
import folium


# Create your views here.
def dictfetchall(cursor): 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

def home(request):
    
    return render(request, "PobrezaHM/base.html")

def mapa(request):

    cursor = connection.cursor()
    #cursor.execute("select dpa_provin, dpa_despro from provincias where dpa_provin != '90' order by dpa_despro;")
    cursor.execute("SELECT dpa_despro, ST_X(ST_CENTROID(geom)) as x , ST_Y(ST_CENTROID(geom)) as y FROM limites.provincias where dpa_provin != '90' order by dpa_despro;")
    r = dictfetchall(cursor)
    
    #Mapa
    primero = r[0]
    locacion = [primero['x'], primero['y']]
    print(locacion)

    m = folium.Map(
        Location = locacion,
        tiles = 'Stamen Toner',
        zoom_start = 100
    )

    #marcador
    folium.Marker(
        locacion,
        tooltip='Clic aquí',
        popup=primero['dpa_despro']

    ).add_to(m)

    m = m._repr_html_()

    context = {
        'provin': r,
        'mapa': m
    }

    return render(request, "PobrezaHM/mapa.html",context)