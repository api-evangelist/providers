---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AudioMuse-AI provides a self‑hosted REST API for music analysis and playlist generation.
  name: AudioMuse API
  slug: audiomuse-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/audiomuse/authentication/audiomuse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audiomuse-authentication.yml
- group: design
  href: https://artifacts.apis.io/audiomuse/errors/audiomuse-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audiomuse-problem-types.yml
- group: other
  href: https://artifacts.apis.io/audiomuse/hosts/audiomuse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audiomuse-hosts.yml
- group: other
  href: https://artifacts.apis.io/audiomuse/vendors/audiomuse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audiomuse-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://neptunehub.github.io/AudioMuse-AI/
- group: docs
  title: ''
  type: Documentation
  url: https://neptunehub.github.io/AudioMuse-AI/
- group: start
  title: ''
  type: GettingStarted
  url: https://neptunehub.github.io/AudioMuse-AI/
- group: operate
  title: ''
  type: Support
  url: https://github.com/NeptuneHub/AudioMuse-AI/issues
- group: other
  title: ''
  type: Image
  url: https://neptunehub.github.io/AudioMuse-AI/screenshot/AM-AI-MAP.png?raw=true
coverage:
  checked: '2026-10-28'
  detail: Provider documentation describes API endpoints but no machine‑readable OpenAPI or other contract is published.
  evidence:
  - status: 200
    url: https://raw.githubusercontent.com/NeptuneHub/AudioMuse-AI/main/docs/AUTH.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: AudioMuse-AI is an open‑source, self‑hosted music analysis platform that uses sonic fingerprinting and AI to rediscover forgotten songs, generate intelligent playlists, and visualize music libraries. It integrates with popular self‑hosted media servers such as Navidrome, Jellyfin, LMS, Lyrion, Emby, and Plex, offering features like multi‑server support, clustering, instant playlist generation, music map visualizations, lyric and text search, and audio‑recording based song identification, all without relying on external metadata services.
layout: provider
modified: '2026-10-28'
name: AudioMuse-AI
nav: Providers
network: true
overview: 'AudioMuse-AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Artificial Intelligence, Open Source, Self-Hosted, and Playlist.


  AudioMuse-AI''s developer surface includes authentication, documentation, getting-started guide, support, and 5 more developer resources.'
plans:
- name: Audiomuse Plans Pricing
  plan_count: 0
  slug: audiomuse-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Audiomuse Rate Limits
  slug: audiomuse-rate-limits
scopes:
- name: Audiomuse Scopes
  scope_count: 0
  slug: audiomuse-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/audiomuse/audiomuse-2026-11-03T121309.png
security:
- kind: authentication
  name: Audiomuse Authentication
  slug: audiomuse-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Audiomuse Domain Security
  slug: audiomuse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audiomuse
tags:
- Music
- Artificial Intelligence
- Open Source
- Self-Hosted
- Playlist
- Audio Analysis
website: https://neptunehub.github.io/AudioMuse-AI/
---
