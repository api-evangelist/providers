---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: documented
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Openmercantil Agentic Access
  operation_count: 36
  slug: openmercantil-agentic-access
  summary_line: 36 operations · 2 acting
api_count: 14
apis:
- description: Stripe checkout and donation endpoints
  name: OpenMercantil Billing API
  slug: openmercantil-billing-api
- description: Company reports, registry events, officers and export
  name: OpenMercantil Companies API
  slug: openmercantil-companies-api
- description: Public procurement (PLACSP) rankings
  name: OpenMercantil Contracts API
  slug: openmercantil-contracts-api
- description: Daily BORME summary feeds
  name: OpenMercantil Daily API
  slug: openmercantil-daily-api
- description: Bulk and per-resource export endpoints
  name: OpenMercantil Export API
  slug: openmercantil-export-api
- description: Geolocation enrichment
  name: OpenMercantil Geocode API
  slug: openmercantil-geocode-api
- description: Company relationship network and embargoes
  name: OpenMercantil Network API
  slug: openmercantil-network-api
- description: Person search and person reports
  name: OpenMercantil Persons API
  slug: openmercantil-persons-api
- description: Company score, trust score and activity timeseries
  name: OpenMercantil Score API
  slug: openmercantil-score-api
- description: Company and person search endpoints
  name: OpenMercantil Search API
  slug: openmercantil-search-api
- description: CNAE sector taxonomy and sector statistics
  name: OpenMercantil Sectors API
  slug: openmercantil-sectors-api
- description: External sources and dataset freshness
  name: OpenMercantil Sources API
  slug: openmercantil-sources-api
- description: Aggregate statistics by region and sector
  name: OpenMercantil Stats API
  slug: openmercantil-stats-api
- description: Service health and metadata
  name: OpenMercantil System API
  slug: openmercantil-system-api
artifact_total: 31
collections:
- collection_type: open
  name: OpenMercantil Public API
  slug: open-openmercantil
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openmercantil-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openmercantil-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openmercantil-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openmercantil.es/
- group: docs
  title: ''
  type: Documentation
  url: https://openmercantil.es/api/documentacion
- group: other
  title: ''
  type: APIsJSON
  url: https://openmercantil.es/apis.json
- group: commercial
  title: ''
  type: Pricing
  url: https://openmercantil.es/precios
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openmercantil.es/terminos-de-uso
- group: operate
  title: ''
  type: Support
  url: https://openmercantil.es/soporte
- group: other
  title: ''
  type: Downloads
  url: https://openmercantil.es/descargas
- group: build
  title: ''
  type: GitHubProject
  url: https://github.com/PabloCirre/OpenBorme
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openmercantil-company-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openmercantil-event-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/openmercantil-company-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/openmercantil-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-search-companies-example.json
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-get-company-example.json
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-get-company-events-example.json
- group: build
  title: ''
  type: Examples
  url: examples/openmercantil-health-example.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/openmercantil-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openmercantil-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openmercantil-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openmercantil-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openmercantil-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://openmercantil.es/llms.txt
created: '2026-05-09'
description: OpenMercantil is an independent public-data API for Spanish company intelligence. It indexes the Boletin Oficial del Registro Mercantil (BORME) and cross-references it with 29+ public sources (CNMV, OEPM, PLACSP, BDNS, OpenSanctions, CCAA gazettes, CNMC, CENDOJ and more) to expose company search, structured company reports, registry event timelines, officer records, CNAE sector navigation, daily summaries, public-procurement rankings, a v1.4 cross-source trust score, and CSV/JSON exports. The public REST API is free, requires no API key, and is rate-limited per IP. The project is informational and does not replace official Registro Mercantil certificates.
examples:
- key_count: 2
  name: Openmercantil Get Company Events Example
  slug: openmercantil-get-company-events-example
- key_count: 2
  name: Openmercantil Get Company Example
  slug: openmercantil-get-company-example
- key_count: 2
  name: Openmercantil Health Example
  slug: openmercantil-health-example
- key_count: 2
  name: Openmercantil Search Companies Example
  slug: openmercantil-search-companies-example
finops:
- name: Openmercantil Finops
  service_category: Open Data / Public Records
  slug: openmercantil-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openmercantil.png
json_schemas:
- name: OpenMercantil Company
  property_count: 13
  slug: openmercantil-company
- name: OpenMercantil Company Event
  property_count: 5
  slug: openmercantil-event
json_structures:
- name: Openmercantil Company Structure
  property_count: 13
  slug: openmercantil-company-structure
jsonld:
- class_count: 31
  name: Openmercantil Context
  property_count: 2
  slug: openmercantil-context
layout: provider
modified: '2026-05-19'
name: OpenMercantil
nav: Providers
network: true
overview: 'OpenMercantil publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Companies API, Contracts API, and 11 more. Tagged areas include Open Data, Spain, Company Data, Business Registry, and BORME.


  The OpenMercantil catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  OpenMercantil''s developer surface includes authentication, documentation, pricing, support, code examples, and 20 more developer resources.'
plans:
- name: Openmercantil Plans Pricing
  plan_count: 3
  slug: openmercantil-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Openmercantil Rate Limits
  slug: openmercantil-rate-limits
rules:
- name: OpenMercantil API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openmercantil-jsonschema-spectral-rules
- name: OpenMercantil API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 4
  slug: openmercantil-rules
score:
  band: developing
  composite: 50.7
  delta: -5.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.3
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 56.0
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
    score: 38.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/openmercantil/refs/heads/main/screenshots/openmercantil-2026-06-20T191016.png
security:
- kind: authentication
  name: Openmercantil Authentication
  slug: openmercantil-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openmercantil Domain Security
  slug: openmercantil-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openmercantil
tags:
- Open Data
- Spain
- Company Data
- Business Registry
- BORME
- Public Records
- Spanish Companies
- CIF
- CNAE
- Public Procurement
- PLACSP
- CNMV
- OEPM
- BDNS
- OpenSanctions
- Public-Interest Data
- Spanish Open Data
- REST API
- JSON
- CSV
- Geocoding
- Trust Score
- Registry Timeline
- Daily Summary
website: https://openmercantil.es/
---
