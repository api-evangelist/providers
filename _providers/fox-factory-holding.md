---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - '{''url'': ''https://www.foxfactory.com'', ''status'': 301, ''note'': ''declared website redirects to https://ridefox.com/ — a different registrable domain (foxfactory.com -> ridefox.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Fox Factory Holding API provides access to platform services and data for enterprise integration and automation.
  name: Fox Factory Holding API
  slug: fox-factory-holding-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fox-factory-holding-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foxfactory
- group: company
  title: ''
  type: Website
  url: https://www.foxfactory.com
created: '2026-04-19'
description: Fox Factory Holding is a major US corporation and Fortune 1000 company. The Fox Factory Holding API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Fox Factory Holding Finops
  service_category: Manufacturing & Components
  slug: fox-factory-holding-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fox-factory-holding.png
layout: provider
modified: '2026-04-19'
name: Fox Factory Holding
nav: Providers
network: true
overview: Fox Factory Holding publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Suspension, Cycling, and Power-Sports.
plans:
- name: Fox Factory Holding Plans Pricing
  plan_count: 1
  slug: fox-factory-holding-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Fox Factory Holding Rate Limits
  slug: fox-factory-holding-rate-limits
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fox-factory-holding/refs/heads/main/screenshots/fox-factory-holding-2026-06-20T181504.png
security:
- kind: domain-security
  name: Fox Factory Holding Domain Security
  slug: fox-factory-holding-domain-security
  summary_line: TLSv1.3
slug: fox-factory-holding
tags:
- Suspension
- Cycling
- Power-Sports
website: https://www.foxfactory.com
---
