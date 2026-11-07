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
api_count: 1
apis:
- description: Searchable archive of community‑made audiobook cover art with endpoints for searching by book title, author, or visual style.
  name: AudiobookCovers API
  slug: audiobookcovers-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/audiobookcovers/hosts/audiobookcovers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audiobookcovers-hosts.yml
- group: other
  href: https://artifacts.apis.io/audiobookcovers/vendors/audiobookcovers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audiobookcovers-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.audiobookcovers.com/
- group: auth
  href: https://artifacts.apis.io/audiobookcovers/security/audiobookcovers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audiobookcovers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audiobookcovers.com/
- group: docs
  title: ''
  type: Documentation
  url: https://audiobookcovers.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://audiobookcovers.com/search
- group: auth
  href: https://artifacts.apis.io/audiobookcovers/security/audiobookcovers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audiobookcovers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audiobookcovers.com/
coverage:
  checked: '2026-10-28'
  detail: The developer portal at https://dev.audiobookcovers.com/ loads its content via JavaScript, preventing machine‑readable discovery of API specifications.
  evidence:
  - status: 200
    url: https://dev.audiobookcovers.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: AudiobookCovers provides a searchable archive of community‑made audiobook cover art. Users can browse and download custom covers for any title, searching by book title, author, or visual style. The service is free, open to contributions, and aims to help listeners personalize their digital libraries with unique artwork.
image: https://audiobookcovers.com/favicon-32x32.png
layout: provider
modified: '2026-10-28'
name: AudiobookCovers
nav: Providers
network: true
overview: 'AudiobookCovers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audiobooks, CoverArt, Community, and Free.


  AudiobookCovers'' developer surface includes documentation, getting-started guide, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 10.5
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
screenshot: https://apis.io/screenshots/audiobookcovers/audiobookcovers-2026-11-03T121308.png
security:
- kind: domain-security
  name: Audiobookcovers Domain Security
  slug: audiobookcovers-domain-security
  summary_line: TLSv1.3 · DMARC
slug: audiobookcovers
tags:
- Company
- Audiobooks
- CoverArt
- Community
- Free
website: https://audiobookcovers.com/
---
