---
aid: rdf
name: RDF
description: The Resource Description Framework (RDF) is a W3C standard for representing information about resources on the web. RDF is the foundation for linked data and the semantic web, providing a graph-based data model where statements are expressed as subject-predicate-object triples. It enables interoperability between systems by using IRIs to identify resources and relationships, supporting multiple serialization formats including RDF/XML, Turtle, N-Triples, N-Quads, TriG, and JSON-LD. RDF 1.1 is a W3C Recommendation (2014). RDF 1.2 is a Candidate Recommendation (2026) adding triple terms (RDF-star) and directional language-tagged strings.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/apis.yml
tags:
  - JSON-LD
  - Knowledge Graph
  - Linked Data
  - Ontology
  - RDF
  - Semantic Web
  - SPARQL
  - W3C
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis: []
common:
  - type: JSONSchema
    name: RDF Triple Schema
    description: JSON Schema for an RDF triple (subject, predicate, object).
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-schema/rdf-triple.json
  - type: JSONSchema
    name: RDF Graph Schema
    description: JSON Schema for an RDF graph in the RDF/JSON serialization format.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-schema/rdf-graph.json
  - type: JSONSchema
    name: RDF Dataset Schema
    description: JSON Schema for an RDF dataset (default graph plus named graphs).
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-schema/rdf-dataset.json
  - type: JSONStructure
    name: RDF Triple Structure
    description: Field-level structure documentation for the RDF triple object.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-structure/rdf-triple-structure.json
  - type: JSONStructure
    name: RDF Graph Structure
    description: Field-level structure documentation for the RDF graph serialization.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-structure/rdf-graph-structure.json
  - type: JSONLDContext
    name: RDF JSON-LD Context
    description: JSON-LD context defining core RDF, RDFS, OWL, and related vocabularies.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-ld/rdf-context.jsonld
  - type: Example
    name: RDF Triple Example
    description: Example RDF triple about Tim Berners-Lee using foaf:name.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/examples/rdf-triple-example.json
  - type: Example
    name: RDF Graph Example
    description: Example RDF graph in RDF/JSON serialization about Tim Berners-Lee.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/examples/rdf-graph-example.json
  - type: Vocabulary
    name: RDF Vocabulary
    description: Normative vocabulary for RDF concepts, serialization formats, and related standards.
    url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/vocabulary/rdf-vocabulary.yml
  - type: Specification
    name: RDF 1.1 Concepts and Abstract Syntax
    description: W3C Recommendation defining the RDF data model.
    url: https://www.w3.org/TR/rdf11-concepts/
  - type: Specification
    name: RDF 1.2 Concepts and Abstract Data Model
    description: W3C Candidate Recommendation (2026) introducing triple terms and directional language-tagged strings.
    url: https://www.w3.org/TR/rdf12-concepts/
  - type: Specification
    name: SPARQL 1.1 Query Language
    description: W3C Recommendation for querying RDF data.
    url: https://www.w3.org/TR/sparql11-query/
  - type: Specification
    name: JSON-LD 1.1
    description: W3C Recommendation for JSON-based RDF serialization.
    url: https://www.w3.org/TR/json-ld11/
  - type: Documentation
    name: W3C RDF Working Group
    description: W3C working group developing RDF and SPARQL specifications.
    url: https://www.w3.org/groups/wg/rdf-star/
  - type: GitHub
    name: W3C RDF Working Group GitHub
    description: GitHub organization for the W3C RDF and SPARQL specifications.
    url: https://github.com/w3c/rdf-star-wg
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
