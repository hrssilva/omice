#!/usr/bin/env python3
from json import loads
from rdflib import Graph
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def sparql_query(g, sparql_query_str: str):
    query_result = g.query(sparql_query_str)
    query_dict = loads(query_result.serialize(encoding="utf-8", format="json"))
    return query_dict

if __name__ == "__main__":
    arger = ArgumentParser(description="A simple script to query a graph locally with SPARQL", formatter_class=ArgumentDefaultsHelpFormatter)
    arger.add_argument("model", help="File to read and query over")
    arger.add_argument("-f", "--file", action="store_true", help="Treat the query argument as a file path to the query")
    arger.add_argument("query", help="SPARQL query to run over model")
    args = arger.parse_args()
    parsed = vars(args)
    query = parsed['query']
    if parsed['file']:
        with open(query, "r") as file:
            query = file.read()
    g = Graph()
    g.parse(parsed['model'])
    print(sparql_query(g, query))
