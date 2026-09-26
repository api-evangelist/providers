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
  href: https://raw.githubusercontent.com/api-evangelist/beek/refs/heads/main/security/beek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beek.io/
created: '2026-07-17'
description: 'Beek was a Spanish-language audiobook and ebook streaming platform serving Latin America and Spain, backed by Accel and Lightspeed Venture Partners. At its peak it reached over 4 million users who streamed nearly 200 million minutes of audio content, including its exclusive Beek Originals catalog. The service has since shut down: Amazon''s Audible acquired a significant portion of the Beek Originals catalog, and Beek now redirects listeners to Audible to continue their libraries. Beek ran a private backend service (api.beek.io) but published no public developer program, OpenAPI specification, SDKs, or developer documentation, so it has no consumable API surface to enrich.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beek.png
layout: provider
modified: '2026-09-15'
name: Beek
nav: Providers
network: true
overview: Beek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Intelligent Apps, Audiobooks, Media, and Streaming.
random_paper: 11
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
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
screenshot: https://raw.githubusercontent.com/api-evangelist/beek/refs/heads/main/screenshots/beek-2026-07-25T202627.png
security:
- kind: domain-security
  name: Beek Domain Security
  slug: beek-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beek
tags:
- Company
- Intelligent Apps
- Audiobooks
- Media
- Streaming
- Consumer
- Entertainment
- Spanish Language
- Latin America
- Defunct
website: https://beek.io/
---
