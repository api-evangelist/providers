---
name: SPARQL
description: SPARQL (SPARQL Protocol and RDF Query Language) is a W3C Recommendation that provides a standardized query language for retrieving and manipulating data stored in Resource Description Framework (RDF) format. It includes a protocol for submitting queries and updates over HTTP, a JSON results format for SELECT and ASK queries, and a Graph Store HTTP Protocol for managing RDF graphs.
url: https://www.w3.org/TR/sparql11-overview/
tags:
  - Linked Data
  - Query Language
  - RDF
  - Semantic Web
  - SPARQL
  - W3C
created: '2025'
modified: '2026-03-16'
apis:
  - name: SPARQL Protocol API
    description: Standard SPARQL 1.1 Protocol HTTP endpoints for executing queries and updates against RDF datasets, plus the Graph Store HTTP Protocol for direct management of named graphs and the default graph, as defined by the W3C Recommendation.
    humanURL: https://www.w3.org/TR/sparql11-protocol/
    baseURL: https://dbpedia.org/sparql
    version: '1.1'
    tags:
      - Graph Store
      - Query
      - RDF
      - SPARQL
      - Update
    properties:
      - type: x-openapi
        url: openapi.yml
      - type: x-json-schema
        url: json-schema.json
      - type: x-json-ld-context
        url: json-ld-context.jsonld
      - type: x-documentation
        url: https://www.w3.org/TR/sparql11-overview/
      - type: x-specification
        url: https://www.w3.org/TR/sparql11-protocol/
      - type: x-specification
        url: https://www.w3.org/TR/sparql11-query/
      - type: x-specification
        url: https://www.w3.org/TR/sparql11-results-json/
    contact:
      - type: x-website
        url: https://www.w3.org/
      - type: x-github
        url: https://github.com/w3c/sparql-query
common: []
---
