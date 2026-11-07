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
  href: https://artifacts.apis.io/listenbrainz/hosts/listenbrainz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/listenbrainz-hosts.yml
- group: build
  href: https://artifacts.apis.io/listenbrainz/packages/listenbrainz-packages.yml
  title: ''
  type: SDKs
  url: packages/listenbrainz-packages.yml
- group: build
  href: https://artifacts.apis.io/listenbrainz/packages/listenbrainz-packages.yml
  title: ''
  type: Packages
  url: packages/listenbrainz-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.listenbrainz.org/search
- group: auth
  href: https://artifacts.apis.io/listenbrainz/security/listenbrainz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/listenbrainz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://listenbrainz.org/
- group: docs
  title: ''
  type: Documentation
  url: https://listenbrainz.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.listenbrainz.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://listenbrainz.org/docs/#getting-started
coverage:
  checked: '2026-10-28'
  detail: The main site https://listenbrainz.org/ serves only a JavaScript shell, preventing machine‑readable extraction of contracts.
  evidence:
  - status: 200
    url: https://listenbrainz.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: ListenBrainz is an open music listening tracking platform that lets users record, explore, visualise and share the music they listen to. It provides a public API for accessing listening data, user profiles, and music metadata, enabling developers to build applications and services around music listening habits.
image: https://listenbrainz.org/static/img/share-header.png
layout: provider
modified: '2026-10-28'
name: ListenBrainz
nav: Providers
network: true
overview: 'ListenBrainz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Open Source, Community, Data API, and Social Listening.


  ListenBrainz''s developer surface includes documentation, API reference, getting-started guide, and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 12.5
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
screenshot: https://apis.io/screenshots/listenbrainz/listenbrainz-2026-11-03T134937.png
security:
- kind: domain-security
  name: Listenbrainz Domain Security
  slug: listenbrainz-domain-security
  summary_line: DMARC
slug: listenbrainz
tags:
- Music
- Open Source
- Community
- Data API
- Social Listening
website: https://listenbrainz.org/
---
