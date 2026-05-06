---
aid: apache-jena
name: Apache Jena
description: Apache Jena is a Java framework for building Semantic Web and Linked Data applications. It provides APIs for RDF, SPARQL, OWL, and a triplestore database (TDB2) along with the Fuseki SPARQL server with a REST API for querying and managing RDF datasets.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Java
  - Linked Data
  - OWL
  - Ontology
  - Open Source
  - RDF
  - Semantic Web
  - SPARQL
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-jena/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-jena:fuseki-sparql-api
    name: Apache Jena Fuseki SPARQL API
    description: Jena Fuseki provides a SPARQL server with REST API endpoints for SPARQL 1.1 Query, SPARQL 1.1 Update, and the SPARQL Graph Store HTTP Protocol. It supports dataset management, authentication, and monitoring.
    humanURL: https://jena.apache.org/documentation/fuseki2/
    tags:
      - Fuseki
      - RDF
      - REST
      - SPARQL
    properties:
      - type: Documentation
        url: https://jena.apache.org/documentation/fuseki2/
      - type: OpenAPI
        url: openapi/apache-jena-fuseki-sparql-api.yaml
  - aid: apache-jena:java-api
    name: Apache Jena Java API
    description: The Jena Java API provides programmatic access to RDF model creation, SPARQL query execution, OWL reasoning, and TDB2 triplestore management for building Semantic Web applications.
    humanURL: https://jena.apache.org/documentation/
    tags:
      - Java
      - OWL
      - RDF
      - SDK
    properties:
      - type: Documentation
        url: https://jena.apache.org/documentation/
      - type: GettingStarted
        url: https://jena.apache.org/tutorials/
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/jena
  - type: Documentation
    url: https://jena.apache.org/documentation/
  - type: GettingStarted
    url: https://jena.apache.org/tutorials/
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://jena.apache.org/about_jena/releases.html
  - type: SpectralRules
    url: rules/apache-jena-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-jena-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/sparql-data-management.yaml
  - type: Features
    data:
      - name: SPARQL Query and Update
        description: Full SPARQL 1.1 query and update protocol support via Fuseki REST API.
      - name: RDF Model API
        description: Java API for creating, reading, and manipulating RDF graphs.
      - name: OWL Reasoning
        description: OWL and RDFS inference via Jena's rule-based and OWL reasoners.
      - name: TDB2 Triplestore
        description: Native high-performance RDF triplestore for persistent graph storage.
      - name: Graph Store Protocol
        description: SPARQL Graph Store HTTP Protocol for named graph management.
      - name: Multiple RDF Formats
        description: Support for Turtle, JSON-LD, N-Triples, RDF/XML, and TriG serialization.
      - name: Ontology API
        description: High-level API for working with OWL and RDFS ontologies.
  - type: UseCases
    data:
      - name: Knowledge Graph Management
        description: Build and query knowledge graphs using RDF and SPARQL.
      - name: Linked Data Publishing
        description: Publish Linked Data endpoints with Fuseki SPARQL server.
      - name: Semantic Search
        description: Enable semantic search over structured RDF datasets.
      - name: Data Integration
        description: Integrate heterogeneous data sources using RDF as a common data model.
  - type: Integrations
    data:
      - name: Apache Solr
        description: Integrate full-text search with SPARQL queries via Solr text index.
      - name: Elasticsearch
        description: Full-text search integration for Fuseki text search capabilities.
      - name: Spring Framework
        description: Spring integration for Jena RDF operations in enterprise Java apps.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
