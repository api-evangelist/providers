---
aid: eclipse-rdf4j
name: Eclipse RDF4J
description: Eclipse RDF4J is a powerful open-source Java framework for processing and handling RDF data. It supports creating, parsing, scalable storage, reasoning, and querying with RDF and Linked Data, and ships with an HTTP server (RDF4J Server) and a web-based Workbench. The framework offers an easy-to-use Java API and SPARQL 1.1 support, and integrates with leading RDF database solutions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/eclipse-rdf4j/refs/heads/main/apis.yml
tags:
  - Eclipse Foundation
  - Java
  - Linked Data
  - Open Source
  - RDF
  - Semantic Web
  - SPARQL
  - Triple Store
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: eclipse-rdf4j:rdf4j-server-rest-api
    name: RDF4J Server REST API
    description: REST API exposed by the Eclipse RDF4J Server for managing repositories, executing SPARQL queries and updates, working with statements, namespaces, contexts, and transactions, and importing/exporting RDF in standard serialization formats.
    humanURL: https://rdf4j.org/documentation/reference/rest-api/
    baseURL: http://localhost:8080/rdf4j-server
    tags:
      - RDF
      - Repository
      - REST
      - SPARQL
      - Transactions
    properties:
      - type: Documentation
        url: https://rdf4j.org/documentation/reference/rest-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/eclipse-rdf4j/main/openapi/rdf4j-server-rest-api-openapi.yml
      - type: GettingStarted
        url: https://rdf4j.org/documentation/programming/getting-started/
      - type: Repository
        url: https://github.com/eclipse/rdf4j
common:
  - type: Getting Started
    url: https://rdf4j.org/documentation/programming/getting-started/
  - type: Documentation
    url: https://rdf4j.org/documentation/
  - type: Tutorials
    url: https://rdf4j.org/documentation/tutorials/
  - type: Change Log
    url: https://rdf4j.org/release-notes/
  - type: Issues
    url: https://github.com/eclipse/rdf4j/issues
  - type: Support
    url: https://github.com/eclipse/rdf4j/discussions
  - type: GitHub Organization
    url: https://github.com/eclipse/rdf4j
  - type: License
    url: https://github.com/eclipse/rdf4j/blob/main/LICENSE.md
maintainers:
  - FN: Eclipse Foundation
    email: rdf4j-dev@eclipse.org
---
