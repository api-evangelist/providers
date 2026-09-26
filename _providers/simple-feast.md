---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/simple-feast/refs/heads/main/security/simple-feast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simple-feast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://food.simplefeast.com/en
created: '2026-07-17'
description: Simple Feast was a Danish plant-based, ready-to-eat meal company surfaced as a portfolio company of balderton-capital and added to the API Evangelist network as a stub for enrichment. As of this enrichment pass the consumer app host food.simplefeast.com no longer resolves and the root domain simplefeast.com is parked on one.com nameservers, so the company appears defunct. No developer portal, API, documentation, or other machine-readable API surface could be discovered during enrichment; this profile is retained as a historical portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simple-feast.png
layout: provider
modified: '2026-09-15'
name: Simple Feast
nav: Providers
network: true
overview: Simple Feast is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Meal Kit, Meal Delivery, and Plant-Based.
random_paper: 16
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Simple Feast Domain Security
  slug: simple-feast-domain-security
  summary_line: DNSSEC
slug: simple-feast
tags:
- Company
- Food
- Meal Kit
- Meal Delivery
- Plant-Based
- E-Commerce
- Defunct
website: https://food.simplefeast.com/en
---
