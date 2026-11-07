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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Official REST API for managing bookmarks, collections, tags, highlights and user data. Documentation is hosted at the developer portal and requires OAuth authentication.
  name: Raindrop.io API
  slug: raindrop-io-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/raindrop-io/llms/raindrop-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/raindrop-io-llms.txt
- group: other
  href: https://artifacts.apis.io/raindrop-io/a2a/raindrop-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/raindrop-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/raindrop-io/well-known/raindrop-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/raindrop-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/raindrop-io/hosts/raindrop-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raindrop-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/raindrop-io/vendors/raindrop-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/raindrop-io-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://help.raindrop.io/security
- group: start
  title: ''
  type: Login
  url: https://app.raindrop.io/account/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/raindropio
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.raindrop.io/more/changelog
- group: auth
  href: https://artifacts.apis.io/raindrop-io/security/raindrop-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raindrop-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://raindrop.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.raindrop.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.raindrop.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.raindrop.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.raindrop.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.raindrop.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://raindrop.io/pro/buy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.raindrop.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.raindrop.io/privacy
created: '2026-10-26'
description: Raindrop.io is an all‑in‑one bookmark manager that lets users save, organize, and sync bookmarks across devices and browsers. It offers collections, tags, highlights, AI‑assisted search, and integrations with services like Dropbox, Google Drive, and various browsers. The platform provides a web app, desktop apps, and mobile apps, supporting collaboration, backup, and public sharing of bookmark collections. Raindrop.io emphasizes security with SSL, VPC‑protected architecture, and no ads or trackers.
image: https://raindrop.io/_next/static/media/screenshot.e362c4f5.jpg
layout: provider
modified: '2026-10-26'
name: Raindrop.io (bookmarks)
nav: Providers
network: true
overview: 'Raindrop.io (bookmarks) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Bookmark, Productivity, Cloud, and Collaboration.


  Raindrop.io (bookmarks)''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 13 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 64.3
    operational_transparency: 15.8
  previous_composite: 29.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/raindrop-io/raindrop-io-2026-11-03T141911.png
security:
- kind: domain-security
  name: Raindrop Io Domain Security
  slug: raindrop-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: raindrop-io
tags:
- Bookmark
- Productivity
- Cloud
- Collaboration
website: https://raindrop.io/
---
