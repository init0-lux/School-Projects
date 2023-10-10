#! /usr/bin/python3

import osmnx as ox
import taxicab as tc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from time import sleep

def create_g(loc, dist, trans_mode, loc_type="address"):
    if loc_type == "address":
        G= ox.graph_from_address(loc, dist = dist, network_type=trans_mode)
    
    return G

G = create_g("New york", 450, 'drive')
ox.plot_graph(G)

"""
orig = (39.08710, -84.31050)
dest = (39.08800, -84.32000)

route = tc.distance.shortest_path(G, orig, dest)

fig, ax = tc.plot.plot_graph_route(
    G, route, figsize=(10,10), show=False, close=False)


ax.scatter(orig[1], orig[0],
    color='lime', marker='x', s=100, label='orig-point')

ax.scatter(dest[1], dest[0],
    color='red', marker='x', s=100, label='dest-point')

plt.legend()
plt.show()

fig, ax = ox.plot_graph(ox.project_graph(G), show=False, close = False, figsize=(40, 40))
plt.title('New York City', fontweight ="bold") 

while True:
    try: 
        loc = plt.ginput(2, show_clicks=True, timeout= -1)

       # orig = ax.transData.inverted().transform(loc[0])
       # dest = ax.transData.inverted().transform(loc[1])


        #orig = (40.713611, -74.006774)
        #dest = (40.710574, -74.007416)
        orig = (loc[0][1], loc[0][0])
        dest = (loc[1][1], loc[1][0])
        print("orig:", orig)
        print("dest:", dest)
        
        route = tc.distance.shortest_path(G, orig, dest)

        fig, ax = tc.plot.plot_graph_route(G, route, figsize=(40, 40), show=False, close = False)
        a=plt.scatter(orig[1], orig[0], color='lime', marker='.', s=500, label='orig')
        b=plt.scatter(dest[1], dest[0], color='blue', marker='.', s=500, label='dest')
        plt.legend()
        plt.ginput(1, timeout=-1)
        a.remove()
        b.remove()

    except KeyboardInterrupt:
        print("Quitting...")
        quit()
"""
