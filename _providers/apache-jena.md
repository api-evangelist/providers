---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Apache Jena Agentic Access
  operation_count: 11
  slug: apache-jena-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- description: The Jena Java API provides programmatic access to RDF model creation, SPARQL query execution, OWL reasoning, and TDB2 triplestore management for building Semantic Web applications.
  name: Apache Jena Java API
  slug: java-api
- baseURL: http://localhost:3030
  baseurl_source: spec
  description: Dataset administration
  name: Apache Jena Dataset Management API
  slug: apache-jena-dataset-management-api
- baseURL: http://localhost:3030
  baseurl_source: spec
  description: SPARQL Graph Store HTTP Protocol operations
  name: Apache Jena Graph Store Protocol API
  slug: apache-jena-graph-store-protocol-api
- baseURL: http://localhost:3030
  baseurl_source: spec
  description: SPARQL 1.1 Query operations
  name: Apache Jena SPARQL Query API
  slug: apache-jena-sparql-query-api
- baseURL: http://localhost:3030
  baseurl_source: spec
  description: SPARQL 1.1 Update operations
  name: Apache Jena SPARQL Update API
  slug: apache-jena-sparql-update-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Jena Fuseki SPARQL Dataset Management API
  slug: open-apache-jena-dataset-management-api
- collection_type: open
  name: Apache Jena Fuseki SPARQL Dataset Management Graph Store Protocol API
  slug: open-apache-jena-graph-store-protocol-api
- collection_type: open
  name: Apache Jena Fuseki SPARQL Dataset Management SPARQL Query API
  slug: open-apache-jena-sparql-query-api
- collection_type: open
  name: Apache Jena Fuseki SPARQL Dataset Management SPARQL Update API
  slug: open-apache-jena-sparql-update-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/jena/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/jena/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/jena/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/jena/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-jena-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-jena-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-jena-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/jena
- group: docs
  title: ''
  type: Documentation
  url: https://jena.apache.org/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://jena.apache.org/tutorials/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: design
  title: ''
  type: Versioning
  url: https://jena.apache.org/about_jena/releases.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-jena-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-jena-vocabulary.yaml
created: '2026-03-16'
description: Apache Jena is a Java framework for building Semantic Web and Linked Data applications. It provides APIs for RDF, SPARQL, OWL, and a triplestore database (TDB2) along with the Fuseki SPARQL server with a REST API for querying and managing RDF datasets.
examples:
- key_count: 0
  name: Fuseki Sparql Api Binding Example
  slug: fuseki-sparql-api-binding-example
- key_count: 3
  name: Fuseki Sparql Api Dataset Example
  slug: fuseki-sparql-api-dataset-example
- key_count: 1
  name: Fuseki Sparql Api Dataset List Example
  slug: fuseki-sparql-api-dataset-list-example
- key_count: 2
  name: Fuseki Sparql Api Dataset Request Example
  slug: fuseki-sparql-api-dataset-request-example
- key_count: 4
  name: Fuseki Sparql Api Rdf Term Example
  slug: fuseki-sparql-api-rdf-term-example
- key_count: 3
  name: Fuseki Sparql Api Sparql Results Example
  slug: fuseki-sparql-api-sparql-results-example
features:
- description: Full SPARQL 1.1 query and update protocol support via Fuseki REST API.
  name: SPARQL Query and Update
- description: Java API for creating, reading, and manipulating RDF graphs.
  name: RDF Model API
- description: OWL and RDFS inference via Jena's rule-based and OWL reasoners.
  name: OWL Reasoning
- description: Native high-performance RDF triplestore for persistent graph storage.
  name: TDB2 Triplestore
- description: SPARQL Graph Store HTTP Protocol for named graph management.
  name: Graph Store Protocol
- description: Support for Turtle, JSON-LD, N-Triples, RDF/XML, and TriG serialization.
  name: Multiple RDF Formats
- description: High-level API for working with OWL and RDFS ontologies.
  name: Ontology API
finops:
- name: Apache Jena Finops
  service_category: API
  slug: apache-jena-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-jena.png
integrations:
- description: Integrate full-text search with SPARQL queries via Solr text index.
  name: Apache Solr
- description: Full-text search integration for Fuseki text search capabilities.
  name: Elasticsearch
- description: Spring integration for Jena RDF operations in enterprise Java apps.
  name: Spring Framework
json_schemas:
- name: Binding
  property_count: 3
  slug: fuseki-sparql-api-binding
- name: DatasetList
  property_count: 1
  slug: fuseki-sparql-api-dataset-list
- name: DatasetRequest
  property_count: 2
  slug: fuseki-sparql-api-dataset-request
- name: Dataset
  property_count: 3
  slug: fuseki-sparql-api-dataset
- name: RDFTerm
  property_count: 4
  slug: fuseki-sparql-api-rdf-term
- name: SparqlResults
  property_count: 3
  slug: fuseki-sparql-api-sparql-results
json_structures:
- name: Fuseki Sparql Api Binding Structure
  property_count: 3
  slug: fuseki-sparql-api-binding-structure
- name: Fuseki Sparql Api Dataset List Structure
  property_count: 1
  slug: fuseki-sparql-api-dataset-list-structure
- name: Fuseki Sparql Api Dataset Request Structure
  property_count: 2
  slug: fuseki-sparql-api-dataset-request-structure
- name: Fuseki Sparql Api Dataset Structure
  property_count: 3
  slug: fuseki-sparql-api-dataset-structure
- name: Fuseki Sparql Api Rdf Term Structure
  property_count: 4
  slug: fuseki-sparql-api-rdf-term-structure
- name: Fuseki Sparql Api Sparql Results Structure
  property_count: 3
  slug: fuseki-sparql-api-sparql-results-structure
jsonld:
- class_count: 6
  name: Apache Jena Fuseki Sparql Api Context
  property_count: 18
  slug: apache-jena-fuseki-sparql-api-context
layout: provider
modified: '2026-05-19'
name: Apache Jena
nav: Providers
network: true
overview: 'Apache Jena publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Dataset Management API, Graph Store Protocol API, SPARQL Query API, and 1 more. Tagged areas include Java, Linked Data, OWL, Ontology, and Open-Source.


  The Apache Jena catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Jena''s developer surface includes documentation, getting-started guide, and 14 more developer resources.'
plans:
- name: Apache Jena Plans Pricing
  plan_count: 3
  slug: apache-jena-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apache Jena Rate Limits
  slug: apache-jena-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Jena API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-jena-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Apache Jena API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 4
    warn: 7
  slug: apache-jena-spectral-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 54.4
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-jena/refs/heads/main/screenshots/apache-jena-2026-06-20T172111.png
security:
- kind: domain-security
  name: Apache Jena Domain Security
  slug: apache-jena-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Jena Vulnerability Disclosure
  slug: apache-jena-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-jena
tags:
- Java
- Linked Data
- OWL
- Ontology
- Open-Source
- RDF
- Semantic Web
- SPARQL
use_cases:
- description: Build and query knowledge graphs using RDF and SPARQL.
  name: Knowledge Graph Management
- description: Publish Linked Data endpoints with Fuseki SPARQL server.
  name: Linked Data Publishing
- description: Enable semantic search over structured RDF datasets.
  name: Semantic Search
- description: Integrate heterogeneous data sources using RDF as a common data model.
  name: Data Integration
---
