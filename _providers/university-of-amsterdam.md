---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 58
  human_in_the_loop: 1
  name: University Of Amsterdam Agentic Access
  operation_count: 106
  slug: university-of-amsterdam-agentic-access
  summary_line: 106 operations · 58 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: OAI-PMH metadata harvesting endpoint for the University of Amsterdam central library catalogue, served via Ex Libris Alma.
  name: UvA Central Catalogue OAI-PMH
  slug: oai-catalogue
- description: OAI-PMH endpoint exposing archival collection descriptions (EAD) from the University of Amsterdam Library archives.
  name: UvA Archives Collection Descriptions OAI-PMH
  slug: oai-archives
- description: OAI-PMH harvesting endpoint for the University of Amsterdam research data repository hosted on Figshare, providing dataset metadata for the UvA portal.
  name: UvA Research Data Repository OAI-PMH (Figshare)
  slug: oai-figshare-repository
- description: Account and group management
  name: University of Amsterdam Accounts API
  slug: university-of-amsterdam-accounts-api
- description: File asset management
  name: University of Amsterdam Assets API
  slug: university-of-amsterdam-assets-api
- description: Dataset CRUD
  name: University of Amsterdam Datasets API
  slug: university-of-amsterdam-datasets-api
- description: GraphQL endpoints
  name: University of Amsterdam GraphQL API
  slug: university-of-amsterdam-graphql-api
- description: Named graph management
  name: University of Amsterdam Graphs API
  slug: university-of-amsterdam-graphs-api
- description: Webhooks
  name: University of Amsterdam Hooks API
  slug: university-of-amsterdam-hooks-api
- description: Instance information
  name: University of Amsterdam Info API
  slug: university-of-amsterdam-info-api
- description: 'Data import jobs. Linked data can be uploaded in two ways: **Simple upload** (< 5 MB): Send the file as `multipart/form-data` in the `POST /datasets/{account}/{dataset}/jobs` request. The job is creat'
  name: University of Amsterdam Jobs API
  slug: university-of-amsterdam-jobs-api
- description: Global RDF prefix management
  name: University of Amsterdam Prefixes API
  slug: university-of-amsterdam-prefixes-api
- description: Saved SPARQL queries
  name: University of Amsterdam Queries API
  slug: university-of-amsterdam-queries-api
- description: Elasticsearch and simple search
  name: University of Amsterdam Search API
  slug: university-of-amsterdam-search-api
- description: Triple store service management
  name: University of Amsterdam Services API
  slug: university-of-amsterdam-services-api
- description: SPARQL query endpoints
  name: University of Amsterdam SPARQL API
  slug: university-of-amsterdam-sparql-api
- description: Data stories
  name: University of Amsterdam Stories API
  slug: university-of-amsterdam-stories-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-amsterdam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-amsterdam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-amsterdam-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uva.nl/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uba.uva.nl/en/support/open-data/open-data.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uva
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-amsterdam/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-amsterdam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-amsterdam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-amsterdam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Amsterdam (Universiteit van Amsterdam, UvA) is a public research university in Amsterdam, Netherlands, ranked #43 in the QS World University Rankings 2025. Its public developer/API footprint is centered on the University Library''s open-data program: a Linked Open Data platform (Triply) exposing digitized collections via REST, SPARQL, and GraphQL, plus OAI-PMH metadata-harvesting endpoints for the central catalogue, archival collection descriptions, and the Figshare-backed research data repository. UvA does not publish a unified, key-issuing public developer portal; the confirmed machine-readable interfaces are library/open-data oriented and most institutional/SIS APIs are internal or gated.'
examples:
- key_count: 20
  name: University Of Amsterdam Get Dataset Example
  slug: university-of-amsterdam-get-dataset-example
- key_count: 2
  name: University Of Amsterdam Sparql Query Example
  slug: university-of-amsterdam-sparql-query-example
finops:
- name: University Of Amsterdam Finops
  service_category: Education
  slug: university-of-amsterdam-finops
graphqls:
- description: ''
  name: University of Amsterdam GraphQL API
  slug: university-of-amsterdam-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-amsterdam.png
json_schemas:
- name: TriplyDB Account
  property_count: 14
  slug: university-of-amsterdam-account
- name: TriplyDB Dataset
  property_count: 22
  slug: university-of-amsterdam-dataset
json_structures:
- name: University Of Amsterdam Dataset Structure
  property_count: 20
  slug: university-of-amsterdam-dataset-structure
jsonld:
- class_count: 15
  name: University Of Amsterdam Context
  property_count: 14
  slug: university-of-amsterdam-context
layout: provider
modified: '2026-06-03'
name: University of Amsterdam
nav: Providers
network: true
overview: 'University of Amsterdam publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Assets API, Datasets API, and 11 more. Tagged areas include Education, Higher Education, University, Open Data, and Linked Data.


  The University of Amsterdam catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Amsterdam''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: University Of Amsterdam Plans Pricing
  plan_count: 2
  slug: university-of-amsterdam-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 1
  name: University Of Amsterdam Rate Limits
  slug: university-of-amsterdam-rate-limits
rules:
- name: University of Amsterdam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-amsterdam-jsonschema-spectral-rules
- name: University of Amsterdam API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: university-of-amsterdam-rules
score:
  band: developing
  composite: 43.3
  delta: -4.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 71.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-amsterdam/refs/heads/main/screenshots/university-of-amsterdam-2026-06-20T200128.png
security:
- kind: authentication
  name: University Of Amsterdam Authentication
  slug: university-of-amsterdam-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: University Of Amsterdam Domain Security
  slug: university-of-amsterdam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-amsterdam
tags:
- Education
- Higher Education
- University
- Open Data
- Linked Data
- Library
- Netherlands
- Europe
website: https://www.uva.nl/en
---
