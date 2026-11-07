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
  href: https://artifacts.apis.io/sveriges-radio/hosts/sveriges-radio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sveriges-radio-hosts.yml
- group: build
  href: https://artifacts.apis.io/sveriges-radio/packages/sveriges-radio-packages.yml
  title: ''
  type: SDKs
  url: packages/sveriges-radio-packages.yml
- group: build
  href: https://artifacts.apis.io/sveriges-radio/packages/sveriges-radio-packages.yml
  title: ''
  type: Packages
  url: packages/sveriges-radio-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sverigesradio
- group: auth
  href: https://artifacts.apis.io/sveriges-radio/security/sveriges-radio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sveriges-radio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sverigesradio.se/
coverage:
  checked: '2026-10-15'
  detail: The provider’s website https://sverigesradio.se/ returns HTML but no machine‑readable API specification was found despite probing common spec locations.
  evidence:
  - status: 200
    url: https://sverigesradio.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Sveriges Radio is Sweden’s national publicly funded radio broadcasting organization, providing news, music, culture and educational programming across multiple channels and digital platforms. It operates several national and regional stations, offers podcasts, live streaming, and a comprehensive news service. The organization also provides open data and APIs for program schedules, news feeds, and media assets, supporting developers and researchers in accessing public broadcasting content.
image: https://image-api.sr.se/v1/d97c3f63-a481-4077-89a0-b5f51ee31360
layout: provider
modified: '2026-10-15'
name: Sveriges Radio
nav: Providers
network: true
overview: Sveriges Radio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Broadcasting, Sweden, and Public.
random_paper: 4
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 5.5
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
screenshot: https://apis.io/screenshots/sveriges-radio/sveriges-radio-2026-11-03T144139.png
security:
- kind: domain-security
  name: Sveriges Radio Domain Security
  slug: sveriges-radio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sveriges-radio
tags:
- Company
- Media
- Broadcasting
- Sweden
- Public
website: https://sverigesradio.se/
---
