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
  href: https://raw.githubusercontent.com/api-evangelist/rentify/refs/heads/main/security/rentify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rentify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rentify.com/
created: '2026-07-17'
description: Rentify was a London-based property technology (PropTech) startup founded in 2011 that built an online lettings and property-management platform for landlords, letting them list, market, price, and manage rental properties directly without a traditional high-street agent. It raised a Series A from Balderton Capital and later a crowdfunding round before ceasing operations. Surfaced as a balderton-capital portfolio company and added to the API Evangelist network for enrichment; the enrichment pass found no live developer portal, documentation, or public API surface (the company is no longer operating and rentify.com no longer serves an application).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rentify.png
layout: provider
modified: '2026-09-16'
name: rentify
nav: Providers
network: true
overview: rentify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PropTech, Real Estate, Property Management, and Lettings.
random_paper: 21
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
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
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
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
screenshot: https://raw.githubusercontent.com/api-evangelist/rentify/refs/heads/main/screenshots/rentify-2026-09-02T153444.png
security:
- kind: domain-security
  name: Rentify Domain Security
  slug: rentify-domain-security
  summary_line: TLSv1.3
slug: rentify
tags:
- Company
- PropTech
- Real Estate
- Property Management
- Lettings
- Rentals
- United Kingdom
- Defunct
website: https://www.rentify.com/
---
