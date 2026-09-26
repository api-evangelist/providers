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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://plerk.com
- group: other
  title: ''
  type: Successor
  url: https://raw.githubusercontent.com/api-evangelist/minu/refs/heads/main/apis.yml
created: '2026-07-17'
description: Plerk was a Mexican fintech startup offering an employee-benefits and perks platform ("beneficios para colaboradores") for companies in Mexico, backed by 500 Global. During 2023 Plerk merged with minu to consolidate the employee benefits offering in Mexico, and the standalone Plerk product was wound down. Its primary domain plerk.com no longer resolves (DNS fully lapsed; last web archive May 2023) and plerk.io redirects to the now-defunct plerk.com. Support was handled at soporte@plerk.io. This profile is retained as a defunct/acquired lead; the surviving product and any API surface live under minu. No live developer portal, API, SDK, or documentation surface exists for Plerk.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plerk.png
layout: provider
modified: '2026-07-20'
name: Plerk
nav: Providers
network: true
overview: Plerk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Benefits, Fintech, Mexico, and Human Resources.
random_paper: 14
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: plerk
tags:
- Company
- Employee Benefits
- Fintech
- Mexico
- Human Resources
- Perks
- Defunct
- Acquired
website: https://plerk.com
---
