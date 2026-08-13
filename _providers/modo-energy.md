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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Modo Energy Agentic Access
  operation_count: 5
  slug: modo-energy-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: Modo Energy's API is designed for battery operators, owners, and utilities looking to build state-of-the-art energy data systems. RESTful, JSON-encoded, authenticated via x-token header.
  name: Modo Energy
  slug: modo-energy
- description: ERCOT (Texas) battery operations
  name: Modo Energy ERCOT API
  slug: modo-energy-ercot-api
- description: Great Britain market datasets
  name: Modo Energy GB API
  slug: modo-energy-gb-api
- description: Australian National Electricity Market
  name: Modo Energy NEM API
  slug: modo-energy-nem-api
artifact_total: 11
collections:
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
random_paper: 46
rate_limits:
- limit_count: 5
  name: Modo Energy Rate Limits
  slug: modo-energy-rate-limits
score:
  band: emerging
  composite: 26.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 62.7
    developer_ergonomics: 10.9
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.5
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
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
