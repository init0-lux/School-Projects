#!/usr/bin/python3

import osmnx as ox
import taxicab as tc
import matplotlib.pyplot as plt

def create_graph(location, distance, transport_mode, location_type="address"):
    if location_type == "address":
        G = ox.graph_from_address(location, dist=distance, network_type=transport_mode)
    return G

def get_coordinates_from_user(ax):
    print("Click on two points on the map to set the origin and destination.")
    coordinates = plt.ginput(2)
    orig = coordinates[0]
    dest = coordinates[1]
    ax.scatter(orig[0], orig[1], color='lime', marker='.', s=1000, label='orig')
    ax.scatter(dest[0], dest[1], color='blue', marker='.', s=1000, label='dest')
    plt.legend()
    plt.show()
    return orig, dest

def main():
    G = create_graph("New York", 450, 'drive')

    fig, ax = tc.plot.plot_graph(G, figsize=(40, 40))

    while True:
        orig, dest = get_coordinates_from_user(ax)

        route = tc.distance.shortest_path(G, orig, dest)

        fig, ax = tc.plot.plot_graph_route(G, route, figsize=(40, 40), show=False, close=False)

if __name__ == "__main__":
    main()

