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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Orbital Agentic Access
  operation_count: 18
  slug: orbital-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 6
apis:
- description: The Caches API from Orbital — 1 operation(s) for caches.
  name: Orbital Caches API
  slug: orbital-caches-api
- description: The Connections API from Orbital — 2 operation(s) for connections.
  name: Orbital Connections API
  slug: orbital-connections-api
- description: The Schemas API from Orbital — 2 operation(s) for schemas.
  name: Orbital Schemas API
  slug: orbital-schemas-api
- description: The Services API from Orbital — 2 operation(s) for services.
  name: Orbital Services API
  slug: orbital-services-api
- description: The Taxiql API from Orbital — 1 operation(s) for taxiql.
  name: Orbital Taxiql API
  slug: orbital-taxiql-api
- description: The Types API from Orbital — 2 operation(s) for types.
  name: Orbital Types API
  slug: orbital-types-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orbital Query Caches API
  slug: open-orbital-caches-api
- collection_type: open
  name: Orbital Query Caches Connections API
  slug: open-orbital-connections-api
- collection_type: open
  name: Orbital Query API
  slug: open-orbital-query-api
- collection_type: open
  name: Orbital Schema Management API
  slug: open-orbital-schema-management-api
- collection_type: open
  name: Orbital Query Caches Schemas API
  slug: open-orbital-schemas-api
- collection_type: open
  name: Orbital Query Caches Services API
  slug: open-orbital-services-api
- collection_type: open
  name: Orbital Query Caches Taxiql API
  slug: open-orbital-taxiql-api
- collection_type: open
  name: Orbital Query Caches Types API
  slug: open-orbital-types-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orbital-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orbital-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orbital-finance
- group: company
  title: ''
  type: Website
  url: https://orbitalhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://orbitalhq.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://orbitalhq.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://orbitalhq.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://orbitalhq.com/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://orbitalhq.com/llms.txt
created: '2026-01-05'
description: Orbital is a data gateway and integration platform that connects APIs, databases, event streams, and other data sources without requiring glue code or manual integration maintenance. The platform delivers self-repairing integrations through instant, on-the-fly orchestration that automatically adapts as APIs and schemas evolve, eliminating the need to write resolvers, generate API clients, or maintain YAML mapping files.
finops:
- name: Orbital Finops
  service_category: API
  slug: orbital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orbital.png
json_schemas:
- name: Orbital Cache
  property_count: 3
  slug: cache
- name: Orbital Connection
  property_count: 6
  slug: connection
- name: Orbital Query
  property_count: 5
  slug: query
- name: Orbital Schema
  property_count: 8
  slug: schema
- name: Orbital Service
  property_count: 7
  slug: service
- name: Orbital Type
  property_count: 5
  slug: type
jsonld:
- class_count: 35
  name: Orbital Context
  property_count: 0
  slug: orbital-context
layout: provider
modified: '2026-05-19'
name: Orbital
nav: Providers
network: true
overview: 'Orbital publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Caches API, Connections API, Schemas API, and 3 more. Tagged areas include Data and Gateways.


  The Orbital catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Orbital''s developer surface includes documentation, changelog, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Orbital Plans Pricing
  plan_count: 3
  slug: orbital-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Orbital Rate Limits
  slug: orbital-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Orbital API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: orbital-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 64.3
    developer_ergonomics: 11.9
    discoverability: 63.0
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orbital/refs/heads/main/screenshots/orbital-2026-06-20T191159.png
security:
- kind: domain-security
  name: Orbital Domain Security
  slug: orbital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orbital
tags:
- Data
- Gateways
website: https://orbitalhq.com/
---
