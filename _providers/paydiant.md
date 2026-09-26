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
created: '2026-07-17'
description: Paydiant was a Boston-based mobile-wallet, point-of-sale and cloud payments platform, backed by General Catalyst, that let banks, merchants and retailers build their own white-label mobile-payment and loyalty apps (notably powering the retailer-led MCX "CurrentC" wallet). PayPal acquired Paydiant in 2015 and folded the technology into its in-store and merchant products; Paydiant no longer operates as an independent company. This API Evangelist profile was surfaced as a General Catalyst portfolio lead; an enrichment probe on 2026-07-20 found no live independent API surface — the paydiant.com domain and its api/developer/docs subdomains wildcard-resolve to a PayPal/MarkMonitor brand-protection parking IP (3.33.139.32) and serve no content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paydiant.png
layout: provider
modified: '2026-09-16'
name: Paydiant
nav: Providers
network: true
overview: Paydiant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Mobile Wallet, Point-of-Sale, and Loyalty.
random_paper: 0
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: paydiant
tags:
- Company
- Payments
- Mobile Wallet
- Point-of-Sale
- Loyalty
- Acquired
- Defunct
---
