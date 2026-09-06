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
  url: security/radiant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.radiantnuclear.com
created: '2026-07-17'
description: Radiant is a nuclear technology company developing portable, transportable microreactors designed to deliver clean, reliable power to remote sites, military installations, disaster-relief operations, and industrial locations that today depend on diesel generators. Its flagship Kaleidos reactor is a factory-built, containerized ~1 MW microreactor intended to ship by truck, plane, or ship and be operational quickly on-site. Founded by former SpaceX engineers and headquartered in El Segundo, California, Radiant is backed by DCVC and Union Square Ventures. As of this enrichment pass the company publishes a corporate and careers web presence but no public developer program, API, SDK, or technical documentation surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radiant.png
layout: provider
modified: '2026-07-20'
name: Radiant
nav: Providers
network: true
overview: Radiant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nuclear, Energy, Microreactor, and Clean Energy.
random_paper: 4
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radiant/refs/heads/main/screenshots/radiant-2026-09-02T152749.png
security:
- kind: domain-security
  name: Radiant Domain Security
  slug: radiant-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: radiant
tags:
- Company
- Nuclear
- Energy
- Microreactor
- Clean Energy
- Power Generation
- Hardware
website: https://www.radiantnuclear.com
---
