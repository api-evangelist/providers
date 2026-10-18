---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - '{''url'': ''https://www.wattswater.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.watts.com/ — a different registrable domain (wattswater.com -> watts.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Watts Water Technologies API provides access to platform services and data for enterprise integration and automation.
  name: Watts Water Technologies API
  slug: watts-water-technologies-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/watts-water-technologies/refs/heads/main/plans/watts-water-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/watts-water-technologies-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/watts-water-technologies/refs/heads/main/rate-limits/watts-water-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/watts-water-technologies-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/watts-water-technologies/refs/heads/main/finops/watts-water-technologies-finops.yml
  title: ''
  type: FinOps
  url: finops/watts-water-technologies-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/watts-water-technologies/refs/heads/main/security/watts-water-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/watts-water-technologies-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wattswater
- group: company
  title: ''
  type: Website
  url: https://www.wattswater.com
created: '2026-04-19'
description: Watts Water Technologies is a major US corporation and Fortune 1000 company. The Watts Water Technologies API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- has_sources: true
  method: generated
  name: Watts Water Technologies Finops
  primary_unit: ''
  service_category: Industrial / Water
  slug: watts-water-technologies-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/watts-water-technologies.png
layout: provider
modified: '2026-04-19'
name: Watts Water Technologies
nav: Providers
network: true
overview: Watts Water Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Water, Industrial, and Infrastructure.
plans:
- name: Watts Water Technologies Plans Pricing
  plan_count: 1
  slug: watts-water-technologies-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Watts Water Technologies Rate Limits
  slug: watts-water-technologies-rate-limits
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/watts-water-technologies/refs/heads/main/screenshots/watts-water-technologies-2026-10-11T194546.png
security:
- kind: domain-security
  name: Watts Water Technologies Domain Security
  slug: watts-water-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: watts-water-technologies
tags:
- Water
- Industrial
- Infrastructure
website: https://www.wattswater.com
---
