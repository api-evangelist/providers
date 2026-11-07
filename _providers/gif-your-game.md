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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/gif-your-game/security/gif-your-game-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/gif-your-game-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/gif-your-game/hosts/gif-your-game-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gif-your-game-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.gifyourgame.com/login
- group: auth
  href: https://artifacts.apis.io/gif-your-game/security/gif-your-game-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gif-your-game-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gif-your-game/security/gif-your-game-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gif-your-game-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gifyourgame.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gifyourgame.com/privacypolicy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.gifyourgame.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Gif Your Game is a platform that enables developers and gamers to create, share, and embed animated GIFs of gameplay moments. By providing a simple API, it allows integration of dynamic game highlights into websites, social media, and streaming overlays. The service supports multiple game titles, offers metadata tagging, and ensures high-performance delivery of short looping clips, helping communities celebrate and showcase gaming achievements.
image: https://thumbs.gifyourgame.com/app_assets/square_ys898l.png
layout: provider
modified: '2026-10-25'
name: Gif Your Game
nav: Providers
network: true
overview: Gif Your Game is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Media, and Community.
random_paper: 1
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gif-your-game/gif-your-game-2026-11-03T132833.png
security:
- kind: domain-security
  name: Gif Your Game Domain Security
  slug: gif-your-game-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Gif Your Game Vulnerability Disclosure
  slug: gif-your-game-vulnerability-disclosure
  summary_line: no policy recorded
slug: gif-your-game
tags:
- Company
- Gaming
- Media
- Community
website: https://www.gifyourgame.com/
---
