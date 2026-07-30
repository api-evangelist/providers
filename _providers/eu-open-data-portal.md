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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eu Open Data Portal Agentic Access
  operation_count: 5
  slug: eu-open-data-portal-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The EU Open Data Portal SPARQL endpoint provides structured queries against linked open data from European Union institutions. Based on OpenLink Virtuoso, the endpoint enables querying of RDF datasets
  name: EU Open Data Portal SPARQL API
  slug: eu-open-data-portal-sparql-api
- description: Federated data catalogs and publishers
  name: EU Open Data Portal Catalogs API
  slug: eu-open-data-portal-catalogs-api
- description: Search and retrieve EU open datasets
  name: EU Open Data Portal Datasets API
  slug: eu-open-data-portal-datasets-api
- description: Access dataset distributions and download links
  name: EU Open Data Portal Distributions API
  slug: eu-open-data-portal-distributions-api
- description: Controlled vocabularies for DCAT-AP metadata
  name: EU Open Data Portal Vocabularies API
  slug: eu-open-data-portal-vocabularies-api
artifact_total: 14
collections:
- collection_type: open
  name: EU Open Data Portal Search API
  slug: open-eu-open-data-portal-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eu-open-data-portal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eu-open-data-portal-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/data-europa-eu
- group: company
  title: ''
  type: Blog
  url: https://data.europa.eu/en/news-events/news
description: The EU Open Data Portal (data.europa.eu) is the official portal for European Union open data, operated by the Publications Office of the European Union. It provides SPARQL and REST APIs for accessing statistical datasets, legislative documents, and institutional data from EU institutions under open licenses.
finops:
- name: Eu Open Data Portal Finops
  service_category: API
  slug: eu-open-data-portal-finops
image: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/refs/heads/main/image.png
json_schemas:
- name: EU Open Data Portal Dataset (DCAT-AP)
  property_count: 17
  slug: eu-open-data-portal-dataset
jsonld:
- class_count: 6
  name: Eu Open Data Portal Context
  property_count: 27
  slug: eu-open-data-portal-context
layout: provider
modified: '2026-04-28'
name: EU Open Data Portal
nav: Providers
network: true
overview: 'EU Open Data Portal publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalogs API, Datasets API, Distributions API, and 1 more. Tagged areas include Government, Open Data, SPARQL, EU, and Regulatory.


  The EU Open Data Portal catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EU Open Data Portal''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Eu Open Data Portal Plans Pricing
  plan_count: 3
  slug: eu-open-data-portal-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Eu Open Data Portal Rate Limits
  slug: eu-open-data-portal-rate-limits
rules:
- name: EU Open Data Portal API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: eu-open-data-portal-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.7
  delta: -3.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.7
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eu-open-data-portal/refs/heads/main/screenshots/eu-open-data-portal-2026-06-20T180843.png
security:
- kind: domain-security
  name: Eu Open Data Portal Domain Security
  slug: eu-open-data-portal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: eu-open-data-portal
tags:
- Government
- Open Data
- SPARQL
- EU
- Regulatory
- Linked Data
---
