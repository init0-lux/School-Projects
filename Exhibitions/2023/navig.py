#! /usr/bin/python3

import osmnx as ox
import taxicab as tc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from time import sleep
from hashlib import md5

def hashfunc(orig,  dest,  id = "Car 1",  rc = "JH01BB3922"):
    orig = md5(str(orig).encode('utf-8')).hexdigest()
    dest = md5(str(dest).encode('utf-8')).hexdigest()
    id = md5(id.encode('utf-8')).hexdigest()
    rc = md5(rc.encode('utf-8')).hexdigest()


    with open("blockchain",  'a') as f:
        strs = orig +  "| " +  dest +  " | " +  id +  " | " +  rc  + " |\n"
        f.write(strs)

def create_g(loc, dist, trans_mode, loc_type="address"):
    if loc_type == "address":
        G= ox.graph_from_address(loc, dist = dist, network_type=trans_mode)
    
    return G

G = create_g("New york", 450, 'drive')
#ox.plot_graph(G)

fig, ax = ox.plot_graph(ox.project_graph(G, "EPSG:4326"), show=False, close = False, figsize=(40, 40))
plt.title('New York City', fontweight ="bold") 

while True:
    try: 
        loc = plt.ginput(2, show_clicks=True, timeout= -1)

        #orig = (40.713611, -74.006774)
        #dest = (40.710574, -74.007416)
        orig = (loc[0][1], loc[0][0])
        dest = (loc[1][1], loc[1][0])
        print("orig:", orig)
        print("dest:", dest)
        hashfunc(orig, dest)

        route = tc.distance.shortest_path(G, orig, dest)
        fig, ax = tc.plot.plot_graph_route(G, route, figsize=(40, 40), show=False, close = False, route_color="green", route_linewidth=4)
        
        a=plt.scatter(orig[1], orig[0], color='cyan', marker='.', s=500, label='orig')
        b=plt.scatter(dest[1], dest[0], color='orange', marker='.', s=500, label='dest')
        #fig = plt.scatter_mapbox(df, lon= “X_from”, lat=”Y_from”, zoom=13, width=1000, height=800, animation_frame=”index”,mapbox_style=”dark”)

        plt.legend()
        plt.ginput(1, timeout=-1)
        
        a.remove()
        b.remove()


    except KeyboardInterrupt:
        print("Quitting...")
        quit()
