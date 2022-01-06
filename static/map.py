coordination = [33.89102317066826, -5.568059749925812]
mapping = folium.Map(location=coordination, zoom_start= 80 ,tiles = 'Stamen Terrain')


def color_config(ELEV):
    if ELEV < 1000:
        return 'green'
    elif 1000 < ELEV < 3000:
        return 'orange'
    else:
        return 'red'

info_I = pd.read_csv('Volcanoes.txt')
lat = info_I['LAT']
lon = info_I['LON']
elev = info_I['ELEV']
name = info_I['NAME']



v_map = folium.FeatureGroup('Volcanoes Location in USA')

for lt ,ln ,ev ,nm in zip(lat ,lon ,elev ,name):
    v_map.add_child(folium.Marker(location= [lt ,ln] , popup= str(nm)+': '+str(ev)+'m ' , icon=folium.Icon(color=color_config(ev))))
    
    

mil_map = folium.FeatureGroup('Mil words')


mil_map.add_child(folium.GeoJson(data=open('world.json' ,'r' ,encoding='utf-8-sig').read() ,
                               style_function = lambda x: {'fillColor' : 'green' if x['properties']['POP2005'] < 1000000 
                       else 'orange' if 1000000 <= x['properties']['POP2005'] < 10000000 
                      else 'red'})) 

m_loc = folium.FeatureGroup('MY LOCATION')


m_loc.add_child(folium.Marker(zoom_start= 80, location= coordination ,popup= '' ,icon=folium.Icon(color='green')))

mapping.add_child(m_loc)
mapping.add_child(v_map)
mapping.add_child(mil_map)
mapping.add_child(folium.LayerControl())
mapping.save('Map v.II.html')