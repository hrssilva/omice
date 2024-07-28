#!/usr/bin/env python3
from rdflib import Graph, compare
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from rdflib.extras.external_graph_libs import rdflib_to_networkx_multidigraph
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    arger = ArgumentParser(description="A simple script to plot the difference between two graphs", formatter_class=ArgumentDefaultsHelpFormatter)
    arger.add_argument("A", help="File to read containing graph A")
    arger.add_argument("B", help="File to read containing graph B")
    args = arger.parse_args()
    parsed = vars(args)
    A = Graph()
    A.parse(parsed['A'])
    B = Graph()
    B.parse(parsed['B'])
    both, first, second = compare.graph_diff(A, B)
    G1 = rdflib_to_networkx_multidigraph(first, lambda s, p ,o: {'p': p})
    G2 = rdflib_to_networkx_multidigraph(second, lambda s, p ,o: {'p': p})
    pos1 = nx.spring_layout(G1, scale=1.25)
    edge_labels1 = nx.get_edge_attributes(G1, 'p')
    print(edge_labels1)
    nx.draw(G1, pos1, node_color='red', node_size=1000, with_labels=True)
    nx.draw_networkx_edge_labels(G1, pos1, edge_labels=edge_labels1)
    plt.show()

    pos2 = nx.spring_layout(G2, scale=1.25)
    edge_labels2 = nx.get_edge_attributes(G2, 'p')
    print(edge_labels2)
    nx.draw(G2, pos2, node_color='green', node_size=1000, with_labels=True)
    nx.draw_networkx_edge_labels(G2, pos2, edge_labels=edge_labels2)
    plt.show()
