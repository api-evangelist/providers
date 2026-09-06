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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/masmovil-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.masmovil.es
created: '2026-07-17'
description: Masmovil (MasMovil Group) is a Spanish telecommunications operator providing mobile, fiber optic internet, and fixed-line services to consumers and businesses across Spain, with bundled fiber-plus-mobile packages, device sales, roaming, and international calling. The group operates a family of consumer telecom brands and, following its 2024 combination with Orange Spain, is part of the MasOrange joint venture. As of this enrichment pass Masmovil publishes no public developer portal, API documentation, or machine-readable API specification; the network profile carries the identity and a domain security posture probe only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/masmovil.png
layout: provider
modified: '2026-07-20'
name: Masmovil
nav: Providers
network: true
overview: Masmovil is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Telecommunications, Mobile, and Fiber.
random_paper: 11
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/masmovil/refs/heads/main/screenshots/masmovil-2026-07-25T230330.png
security:
- kind: domain-security
  name: Masmovil Domain Security
  slug: masmovil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: masmovil
tags:
- Company
- Consumer
- Telecommunications
- Mobile
- Fiber
- Internet
- Spain
website: https://www.masmovil.es
---
