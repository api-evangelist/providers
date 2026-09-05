---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Modo Energy Agentic Access
  operation_count: 5
  slug: modo-energy-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Modo Energy's API is designed for battery operators, owners, and utilities looking to build state-of-the-art energy data systems. RESTful, JSON-encoded, authenticated via x-token header.
  name: Modo Energy
  slug: modo-energy
- baseURL: https://api.modoenergy.com/pub/v1
  baseurl_source: declared
  description: ERCOT (Texas) battery operations
  name: Modo Energy ERCOT API
  slug: modo-energy-ercot-api
- baseURL: https://api.modoenergy.com/pub/v1
  baseurl_source: declared
  description: Great Britain market datasets
  name: Modo Energy GB API
  slug: modo-energy-gb-api
- baseURL: https://api.modoenergy.com/pub/v1
  baseurl_source: declared
  description: Australian National Electricity Market
  name: Modo Energy NEM API
  slug: modo-energy-nem-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Modo Energy ERCOT API
  slug: open-modo-energy-ercot-api
- collection_type: open
  name: Modo Energy ERCOT GB API
  slug: open-modo-energy-gb-api
- collection_type: open
  name: Modo Energy ERCOT NEM API
  slug: open-modo-energy-nem-api
- collection_type: open
  name: Modo Energy API
  slug: open-modo-energy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modo-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modo-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modo-energy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/modo-energy
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.modoenergy.com/llms.txt
created: '2025-05-02'
description: Modo Energy's API is designed for battery operators, owners, and utilities looking to build state-of-the-art energy data systems.
finops:
- name: Modo Energy Finops
  service_category: API
  slug: modo-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/modo-energy.png
layout: provider
modified: '2026-04-28'
name: Modo Energy
nav: Providers
network: true
overview: 'Modo Energy publishes 3 APIs on the [APIs.io](https://apis.io/) network: ERCOT API, GB API, and NEM API. Tagged areas include Energy, Battery Storage, Utilities, and Data.


  Modo Energy''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Modo Energy Plans Pricing
  plan_count: 3
  slug: modo-energy-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Modo Energy Rate Limits
  slug: modo-energy-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 20.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modo-energy/refs/heads/main/screenshots/modo-energy-2026-06-20T185702.png
security:
- kind: authentication
  name: Modo Energy Authentication
  slug: modo-energy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Modo Energy Domain Security
  slug: modo-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: modo-energy
tags:
- Energy
- Battery Storage
- Utilities
- Data
---
