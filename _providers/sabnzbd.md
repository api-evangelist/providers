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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Sabnzbd Webhooks
  slug: sabnzbd-webhooks
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://sabnzbd.org/wiki/introduction/quick-setup
- group: design
  href: https://artifacts.apis.io/sabnzbd/asyncapi/sabnzbd-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sabnzbd-webhooks.yml
- group: other
  href: https://artifacts.apis.io/sabnzbd/hosts/sabnzbd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sabnzbd-hosts.yml
- group: other
  href: https://artifacts.apis.io/sabnzbd/vendors/sabnzbd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sabnzbd-vendors.yml
- group: build
  href: https://artifacts.apis.io/sabnzbd/packages/sabnzbd-packages.yml
  title: ''
  type: SDKs
  url: packages/sabnzbd-packages.yml
- group: build
  href: https://artifacts.apis.io/sabnzbd/packages/sabnzbd-packages.yml
  title: ''
  type: Packages
  url: packages/sabnzbd-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/sabnzbd/sabnzbd/releases/tag/5.1.3
- group: auth
  href: https://artifacts.apis.io/sabnzbd/security/sabnzbd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sabnzbd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sabnzbd.org/
- group: docs
  title: ''
  type: Documentation
  url: https://sabnzbd.org/wiki/
- group: docs
  title: ''
  type: APIReference
  url: https://sabnzbd.org/wiki/configuration/5.1/api
- group: operate
  title: ''
  type: Support
  url: https://forums.sabnzbd.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sabnzbd
coverage:
  checked: '2026-10-28'
  detail: API reference page provides HTML only, no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://sabnzbd.org/wiki/configuration/5.1/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: SABnzbd is an open-source binary newsreader that automates downloading from Usenet. It provides a web‑based interface and a rich HTTP API for managing queues, monitoring progress, and integrating post‑processing scripts. The service supports multiple platforms, offers detailed configuration options, and includes features such as RSS feeds, API authentication, and extensive documentation for developers.
layout: provider
modified: '2026-10-28'
name: SABnzbd
nav: Providers
network: true
overview: 'SABnzbd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Usenet, Downloader, and Open Source.


  The SABnzbd catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SABnzbd''s developer surface includes getting-started guide, changelog, documentation, API reference, support, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 23.8
    discoverability: 35.7
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.7
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sabnzbd/sabnzbd-2026-11-03T142625.png
security:
- kind: domain-security
  name: Sabnzbd Domain Security
  slug: sabnzbd-domain-security
  summary_line: TLSv1.3
slug: sabnzbd
tags:
- Company
- Usenet
- Downloader
- Open Source
website: https://sabnzbd.org/
---
