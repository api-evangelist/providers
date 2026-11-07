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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/asianrecs-com/hosts/asianrecs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asianrecs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asianrecs-com/vendors/asianrecs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asianrecs-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/asianrecs-com/security/asianrecs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asianrecs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asianrecs.com/
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires POST, which is disallowed, preventing contract retrieval.
  evidence:
  - status: 405
    url: https://asianrecs.com/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Asian Recs provides a curated ranking of restaurants in San Francisco and New York City based on preferences of Asian diners. The platform aggregates reviews, ratings, and cuisine types to help users discover Chinese, Japanese, Vietnamese, Korean, Thai, and other Asian food options, as well as broader categories. It offers searchable listings, detailed restaurant profiles, and community-driven insights to guide dining choices across major urban areas.
image: https://asianrecs.com/logo.png
layout: provider
modified: '2026-11-01'
name: Asian Recs
nav: Providers
network: true
overview: Asian Recs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Food, Rankings, and Asian Cuisine.
random_paper: 21
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 3.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asianrecs Com Domain Security
  slug: asianrecs-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: asianrecs-com
tags:
- Company
- Restaurant
- Food
- Rankings
- Asian Cuisine
website: https://asianrecs.com/
---
