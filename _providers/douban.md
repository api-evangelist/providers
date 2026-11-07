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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Douban provides data about movies, books, music and events.
  name: Douban API
  slug: douban-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/douban/hosts/douban-hosts.yml
  title: ''
  type: Hosts
  url: hosts/douban-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/douban
- group: auth
  href: https://artifacts.apis.io/douban/security/douban-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/douban-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://douban.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.douban.com/
coverage:
  checked: '2026-10-28'
  detail: Main site returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://douban.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Douban.com, launched on 6 March 2005, is a Chinese online database and social networking service that allows registered users to record information and create content related to film, books, music, recent events, and activities in Chinese cities. Named after a hutong in Chaoyang District, Beijing, Douban has become a major platform for cultural discussion and recommendation.
image: https://www.douban.com/favicon.ico
layout: provider
modified: '2026-10-28'
name: Douban
nav: Providers
network: true
overview: 'Douban is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social, Media, Entertainment, and China.


  Douban''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.5
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
screenshot: https://apis.io/screenshots/douban/douban-2026-11-03T131000.png
security:
- kind: domain-security
  name: Douban Domain Security
  slug: douban-domain-security
  summary_line: TLSv1.2
slug: douban
tags:
- Social
- Media
- Entertainment
- China
website: https://douban.com/
---
