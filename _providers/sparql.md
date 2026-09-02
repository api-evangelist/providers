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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sparql Agentic Access
  operation_count: 3
  slug: sparql-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 2
apis:
- description: Standard SPARQL 1.1 Protocol HTTP endpoints for executing queries and updates against RDF datasets, plus the Graph Store HTTP Protocol for direct management of named graphs and the default graph, as d
  name: SPARQL Protocol API
  slug: sparql-protocol-api
- description: SPARQL query operation
  name: SPARQL Query API
  slug: sparql-query-api
- description: The Sparql API from SPARQL — 1 operation(s) for sparql.
  name: SPARQL Sparql API
  slug: sparql-sparql-api
- description: The Sparql Graph API from SPARQL — 1 operation(s) for sparql graph.
  name: SPARQL Sparql Graph API
  slug: sparql-sparql-graph-api
- description: The Sparql Update API from SPARQL — 1 operation(s) for sparql update.
  name: SPARQL Sparql Update API
  slug: sparql-sparql-update-api
- description: SPARQL update operation
  name: SPARQL Update API
  slug: sparql-update-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SPARQL 1.1 Protocol Query API
  slug: open-sparql-query-api
- collection_type: open
  name: 1.1 Protocol Query Sparql API
  slug: open-sparql-sparql-api
- collection_type: open
  name: SPARQL 1.1 Protocol Query Sparql Graph API
  slug: open-sparql-sparql-graph-api
- collection_type: open
  name: SPARQL 1.1 Protocol Query Sparql Update API
  slug: open-sparql-sparql-update-api
- collection_type: open
  name: SPARQL 1.1 Protocol Query Update API
  slug: open-sparql-update-api
- collection_type: open
  name: SPARQL 1.1 Protocol
  slug: open-sparql
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sparql-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparql-domain-security.yml
created: '2025'
description: SPARQL (SPARQL Protocol and RDF Query Language) is a W3C Recommendation that provides a standardized query language for retrieving and manipulating data stored in Resource Description Framework (RDF) format. It includes a protocol for submitting queries and updates over HTTP, a JSON results format for SELECT and ASK queries, and a Graph Store HTTP Protocol for managing RDF graphs.
finops:
- name: Sparql Finops
  service_category: API
  slug: sparql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sparql.png
layout: provider
modified: '2026-03-16'
name: SPARQL
nav: Providers
network: true
overview: SPARQL publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Query API, Sparql API, Sparql Graph API, and 2 more. Tagged areas include Linked Data, Query Language, RDF, Semantic Web, and SPARQL.
plans:
- name: Sparql Plans Pricing
  plan_count: 3
  slug: sparql-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Sparql Rate Limits
  slug: sparql-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 56.3
    developer_ergonomics: 0.0
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 40.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sparql/refs/heads/main/screenshots/sparql-2026-06-20T194246.png
security:
- kind: domain-security
  name: Sparql Domain Security
  slug: sparql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sparql
tags:
- Linked Data
- Query Language
- RDF
- Semantic Web
- SPARQL
- W3C
website: https://www.w3.org/TR/sparql11-overview/
---
