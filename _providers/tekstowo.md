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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tekstowo/hosts/tekstowo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tekstowo-hosts.yml
- group: other
  href: https://artifacts.apis.io/tekstowo/vendors/tekstowo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tekstowo-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tekstowo/security/tekstowo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tekstowo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tekstowo.pl/
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation page https://www.tekstowo.pl/docs returns HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.tekstowo.pl/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Tekstowo is a Polish online platform offering a vast collection of song lyrics, translations, and music videos. Users can search, contribute, and translate lyrics, with community-driven rankings and points. The site features automatic AI translations, user profiles, and extensive catalogs covering millions of songs, making it a central hub for music enthusiasts in Poland.
image: https://www.tekstowo.pl/static/v2/images/favicons/icon-512.png
layout: provider
modified: '2026-10-28'
name: Tekstowo
nav: Providers
network: true
overview: Tekstowo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Lyrics, Community, Polish, and Entertainment.
random_paper: 8
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 3.4
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/tekstowo/tekstowo-2026-11-03T144408.png
security:
- kind: domain-security
  name: Tekstowo Domain Security
  slug: tekstowo-domain-security
  summary_line: TLSv1.2 · DMARC
slug: tekstowo
tags:
- Music
- Lyrics
- Community
- Polish
- Entertainment
website: https://tekstowo.pl/
---
