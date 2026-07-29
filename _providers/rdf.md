---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 9
common:
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-schema/rdf-triple.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-schema/rdf-graph.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-schema/rdf-dataset.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-structure/rdf-triple-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-structure/rdf-graph-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/json-ld/rdf-context.jsonld
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/examples/rdf-triple-example.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/examples/rdf-graph-example.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/vocabulary/rdf-vocabulary.yml
- group: docs
  title: ''
  type: Specification
  url: https://www.w3.org/TR/rdf11-concepts/
- group: docs
  title: ''
  type: Specification
  url: https://www.w3.org/TR/rdf12-concepts/
- group: docs
  title: ''
  type: Specification
  url: https://www.w3.org/TR/sparql11-query/
- group: docs
  title: ''
  type: Specification
  url: https://www.w3.org/TR/json-ld11/
- group: docs
  title: ''
  type: Documentation
  url: https://www.w3.org/groups/wg/rdf-star/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/w3c/rdf-star-wg
created: '2025-01-01'
description: The Resource Description Framework (RDF) is a W3C standard for representing information about resources on the web. RDF is the foundation for linked data and the semantic web, providing a graph-based data model where statements are expressed as subject-predicate-object triples. It enables interoperability between systems by using IRIs to identify resources and relationships, supporting multiple serialization formats including RDF/XML, Turtle, N-Triples, N-Quads, TriG, and JSON-LD. RDF 1.1 is a W3C Recommendation (2014). RDF 1.2 is a Candidate Recommendation (2026) adding triple terms (RDF-star) and directional language-tagged strings.
examples:
- key_count: 1
  name: Rdf Graph Example
  slug: rdf-graph-example
- key_count: 4
  name: Rdf Triple Example
  slug: rdf-triple-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rdf.png
json_schemas:
- name: RDF Dataset
  property_count: 2
  slug: rdf-dataset
- name: RDF Graph
  property_count: 0
  slug: rdf-graph
- name: RDF Triple
  property_count: 3
  slug: rdf-triple
json_structures:
- name: Rdf Graph Structure
  property_count: 0
  slug: rdf-graph-structure
- name: Rdf Triple Structure
  property_count: 0
  slug: rdf-triple-structure
jsonld:
- class_count: 0
  name: Rdf Context
  property_count: 30
  slug: rdf-context
layout: provider
modified: '2026-05-02'
name: RDF
nav: Providers
network: true
overview: 'RDF is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include JSON-LD, Knowledge Graph, Linked Data, Ontology, and RDF.


  The RDF catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RDF''s developer surface includes code examples, documentation, GitHub presence, and 12 more developer resources.'
random_paper: 0
rules:
- name: RDF API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: rdf-jsonschema-spectral-rules
score:
  band: emerging
  composite: 18.9
  delta: -4.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 12.9
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 23.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rdf/refs/heads/main/screenshots/rdf-2026-06-20T192625.png
slug: rdf
tags:
- JSON-LD
- Knowledge Graph
- Linked Data
- Ontology
- RDF
- Semantic Web
- SPARQL
- W3C
---
