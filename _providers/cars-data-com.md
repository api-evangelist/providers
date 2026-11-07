---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/cars-data-com/security/cars-data-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cars-data-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cars-data.com/
created: '2026-11-03'
description: Cars-Data.com is a global automotive data platform that provides detailed car specifications, comparisons, and structured data for over 100,000 vehicle variants across 120 manufacturers. Founded in 2009, it aims to make automotive information clear and accessible for buyers, enthusiasts, developers, and partners needing reliable vehicle data. The service offers searchable databases, API access, and multilingual support, helping users make informed decisions and integrate car specs into applications.
layout: provider
modified: '2026-11-03'
name: Cars-Data.com
nav: Providers
network: true
overview: Cars-Data.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Data, and Vehicles.
random_paper: 20
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 1
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cars Data Com Domain Security
  slug: cars-data-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cars-data-com
tags:
- Company
- Automotive
- Data
- Vehicles
website: https://cars-data.com/
---
