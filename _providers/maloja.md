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
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Simple self-hosted music scrobble database to create personal listening statistics.
  name: Maloja API
  slug: maloja-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/maloja/well-known/maloja-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/maloja-well-known.yml
- group: auth
  href: https://artifacts.apis.io/maloja/security/maloja-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maloja-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/maloja/llms/maloja-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maloja-llms.txt
- group: other
  href: https://artifacts.apis.io/maloja/hosts/maloja-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maloja-hosts.yml
- group: other
  href: https://artifacts.apis.io/maloja/vendors/maloja-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maloja-vendors.yml
- group: build
  href: https://artifacts.apis.io/maloja/packages/maloja-packages.yml
  title: ''
  type: SDKs
  url: packages/maloja-packages.yml
- group: build
  href: https://artifacts.apis.io/maloja/packages/maloja-packages.yml
  title: ''
  type: Packages
  url: packages/maloja-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.last.fm/api/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.last.fm/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.last.fm/login
- group: company
  title: ''
  type: Blog
  url: https://blog.last.fm/
- group: company
  title: ''
  type: Website
  url: https://www.last.fm/login?next=/api/account/create
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/krateng/maloja#readme
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/krateng/maloja#readme
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/krateng/maloja#readme
- group: operate
  title: ''
  type: Support
  url: https://github.com/krateng/maloja/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/krateng
coverage:
  checked: '2026-10-29'
  detail: The Last.fm API documentation is publicly readable HTML but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other spec.
  evidence:
  - status: 200
    url: https://www.last.fm/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Maloja is an open-source, self-hosted music scrobble database that lets users collect and analyze their listening habits. It provides charts, artist association insights, and customizable images without relying on external music services. Users can run it via Docker or Podman, configure API keys for Last.fm or Spotify, and integrate with existing scrobble clients through a standard-compliant API. The project emphasizes privacy, data ownership, and simplicity, offering manual scrobbling and proxy capabilities.
image: https://raw.githubusercontent.com/krateng/maloja/master/screenshot.png
layout: provider
modified: '2026-10-29'
name: Maloja
nav: Providers
network: true
overview: 'Maloja is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Self-Hosted, Scrobble, Statistics, and Open Source.


  Maloja''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, and 12 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 22.3
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/maloja/maloja-2026-11-03T135305.png
security:
- kind: domain-security
  name: Maloja Domain Security
  slug: maloja-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: maloja
tags:
- Music
- Self-Hosted
- Scrobble
- Statistics
- Open Source
- Company
website: https://www.last.fm/login?next=/api/account/create
---
