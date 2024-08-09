#!/usr/bin/env python3
from rdflib import Graph, compare
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt
import itertools as it

if __name__ == "__main__":
    arger = ArgumentParser(description="A simple script to plot the difference between two graphs", formatter_class=ArgumentDefaultsHelpFormatter)
    arger.add_argument("A", help="File to read containing graph A")
    arger.add_argument("B", help="File to read containing graph B")
    args = arger.parse_args()
    parsed = vars(args)
    #connectionstyle = f"arc3, rad = 0.3"
    connectionstyle = [f"arc3,rad={r}" for r in it.accumulate([0.15] * 4)]   
    A = Graph()
    A.parse(parsed['A'])
    B = Graph()
    B.parse(parsed['B'])
    both, first, second = compare.graph_diff(A, B)
    G1 = rdflib_to_networkx_multidigraph(first, lambda s, p ,o: {'p': p})
    G2 = rdflib_to_networkx_multidigraph(second, lambda s, p ,o: {'p': p})
    pos1 = nx.spring_layout(G1)
    edge_labels1 = {}
    for key, value in nx.get_edge_attributes(G1, 'p').items():
        edge_labels1[key] = (value.rpartition('#')[-1].rpartition('/')[-1] or value.rpartition('#')[-1])
    node_labels1 = {}
    for key, value in G1.nodes().items():
        node_labels1[key] = (str(key).rpartition('#')[-1].rpartition('/')[-1] or str(key).rpartition('#')[-1])
    print(f"Drawing graph\n\t{G1}" )
    nx.draw(G1, pos1, node_color='red', node_shape="o", node_size=2000, labels=node_labels1, with_labels=True, connectionstyle=connectionstyle, bbox=dict(facecolor="red", edgecolor='black', boxstyle='round,pad=0.3'), arrowsize=20, margins=[0.2, 0.3])
    nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels1, connectionstyle=connectionstyle)
    plt.show()

    pos2 = nx.spring_layout(G2)
    edge_labels2 = {}
    for key, value in nx.get_edge_attributes(G2, 'p').items():
        edge_labels2[key] = (value.rpartition('#')[-1].rpartition('/')[-1] or value.rpartition('#')[-1])
    node_labels2 = {}
    for key, value in G2.nodes().items():
        node_labels2[key] = (str(key).rpartition('#')[-1].rpartition('/')[-1] or str(key).rpartition('#')[-1])
        print(key, node_labels2[key])
    print(f"Drawing graph\n\t{G2}" )
    nx.draw(G2, pos2, node_color='green', node_shape="o", node_size=2000, labels=node_labels2, with_labels=True, connectionstyle=connectionstyle, bbox=dict(facecolor="green", edgecolor='black', boxstyle='round,pad=0.3'), arrowsize=20, margins=[0.2, 0.3])
    nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels2, connectionstyle=connectionstyle)
    plt.show()
