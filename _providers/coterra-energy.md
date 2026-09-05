---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Coterra Energy API provides access to platform services and data for enterprise integration and automation.
  name: Coterra Energy API
  slug: coterra-energy-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coterra-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coterra-energy
- group: company
  title: ''
  type: Website
  url: https://www.coterra.com
created: '2026-04-19'
description: Coterra Energy is a major US corporation and Fortune 1000 company. The Coterra Energy API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Coterra Energy Finops
  service_category: Oil & Gas Exploration and Production
  slug: coterra-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coterra-energy.png
layout: provider
modified: '2026-04-19'
name: Coterra Energy
nav: Providers
network: true
overview: Coterra Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil and Gas, and Exploration.
plans:
- name: Coterra Energy Plans Pricing
  plan_count: 0
  slug: coterra-energy-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Coterra Energy Rate Limits
  slug: coterra-energy-rate-limits
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coterra-energy/refs/heads/main/screenshots/coterra-energy-2026-06-20T175054.png
security:
- kind: domain-security
  name: Coterra Energy Domain Security
  slug: coterra-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coterra-energy
tags:
- Energy
- Oil and Gas
- Exploration
website: https://www.coterra.com
---
