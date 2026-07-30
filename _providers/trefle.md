---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
- acting_count: 0
  human_in_the_loop: 0
  name: Trefle Agentic Access
  operation_count: 18
  slug: trefle-agentic-access
  summary_line: 18 operations
api_count: 10
apis:
- description: Access geographic distribution zones and retrieve plants native or established in specific regions.
  name: Trefle Distributions API
  slug: trefle-distributions-api
- description: Retrieve botanical division class classification data.
  name: Trefle Division Classes API
  slug: trefle-division-classes-api
- description: Retrieve botanical division order classification data.
  name: Trefle Division Orders API
  slug: trefle-division-orders-api
- description: Retrieve botanical division classification data.
  name: Trefle Divisions API
  slug: trefle-divisions-api
- description: Retrieve plant family classification and taxonomy data.
  name: Trefle Families API
  slug: trefle-families-api
- description: Retrieve plant genus classification data.
  name: Trefle Genus API
  slug: trefle-genus-api
- description: Retrieve botanical kingdom classification data.
  name: Trefle Kingdoms API
  slug: trefle-kingdoms-api
- description: Search, list, and retrieve plant species by various attributes including common name, scientific name, slug, and taxonomic identifiers.
  name: Trefle Plants API
  slug: trefle-plants-api
- description: Access detailed species information including taxonomy, morphology, growth characteristics, soil requirements, and geographic distributions.
  name: Trefle Species API
  slug: trefle-species-api
- description: Retrieve botanical subkingdom classification data.
  name: Trefle Subkingdoms API
  slug: trefle-subkingdoms-api
artifact_total: 25
collections:
- collection_type: open
  name: Trefle API
  slug: open-trefle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trefle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trefle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trefle-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trefle-api
- group: company
  title: ''
  type: Website
  url: https://trefle.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trefle.io/
- group: start
  title: ''
  type: Signup
  url: https://trefle.io/users/sign_in
- group: build
  title: ''
  type: GitHub
  url: https://github.com/treflehq
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trefle-vocabulary.yml
created: '2025-02-24'
description: An open, freely accessible botanical data source and REST API for plant information covering over 400,000 plant species with taxonomy, morphology, growth requirements, and geographic distributions.
examples:
- key_count: 2
  name: Trefle Get Species Example
  slug: trefle-get-species-example
- key_count: 2
  name: Trefle Search Plants Example
  slug: trefle-search-plants-example
finops:
- name: Trefle Finops
  service_category: API
  slug: trefle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trefle.png
json_schemas:
- name: Trefle Plant
  property_count: 12
  slug: trefle-plant
- name: Trefle Species
  property_count: 19
  slug: trefle-species
json_structures:
- name: Trefle Species Structure
  property_count: 0
  slug: trefle-species-structure
jsonld:
- class_count: 44
  name: Trefle Context
  property_count: 0
  slug: trefle-context
layout: provider
modified: '2026-05-19'
name: Trefle
nav: Providers
network: true
overview: 'Trefle publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Distributions API, Division Classes API, Division Orders API, and 7 more. Tagged areas include Agriculture, Botany, Open Data, Plants, and Science.


  The Trefle catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trefle''s developer surface includes authentication, documentation, signup flow, GitHub presence, and 5 more developer resources.'
plans:
- name: Trefle Plans Pricing
  plan_count: 3
  slug: trefle-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Trefle Rate Limits
  slug: trefle-rate-limits
rules:
- name: Trefle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: trefle-jsonschema-spectral-rules
- name: Trefle API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: trefle-rules
score:
  band: developing
  composite: 47.7
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.1
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trefle/refs/heads/main/screenshots/trefle-2026-06-20T195651.png
security:
- kind: authentication
  name: Trefle Authentication
  slug: trefle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trefle Domain Security
  slug: trefle-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trefle
tags:
- Agriculture
- Botany
- Open Data
- Plants
- Science
website: https://trefle.io/
---
