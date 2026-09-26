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
  href: https://raw.githubusercontent.com/api-evangelist/gxo-logistics/refs/heads/main/security/gxo-logistics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gxo-logistics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gxologistics
- group: company
  title: ''
  type: Website
  url: https://www.gxo-logistics.com
description: GXO Logistics is a leading global provider of pure-play contract logistics, offering warehousing, distribution, e-commerce fulfillment, supply chain optimization, and reverse logistics services.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gxo-logistics.png
layout: provider
modified: '2026-04-28'
name: GXO Logistics
nav: Providers
network: true
overview: GXO Logistics is profiled on the [APIs.io](https://apis.io/) network.
random_paper: 14
score:
  band: minimal
  composite: 1.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 14.0
    catalog_earned_first_party: 0.0
    catalog_gap: 101.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 25.0
    operational_transparency: 0.0
  previous_composite: 2.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gxo Logistics Domain Security
  slug: gxo-logistics-domain-security
  summary_line: DMARC
slug: gxo-logistics
website: https://www.gxo-logistics.com
---
