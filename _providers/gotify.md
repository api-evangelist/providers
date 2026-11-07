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
  href: https://artifacts.apis.io/gotify/hosts/gotify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gotify-hosts.yml
- group: other
  href: https://artifacts.apis.io/gotify/vendors/gotify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gotify-vendors.yml
- group: build
  href: https://artifacts.apis.io/gotify/packages/gotify-packages.yml
  title: ''
  type: SDKs
  url: packages/gotify-packages.yml
- group: build
  href: https://artifacts.apis.io/gotify/packages/gotify-packages.yml
  title: ''
  type: Packages
  url: packages/gotify-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gotify
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/gotify/server/releases/latest
- group: start
  title: ''
  type: GettingStarted
  url: https://gotify.net/docs/dev-setup
- group: auth
  href: https://artifacts.apis.io/gotify/security/gotify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gotify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gotify.net/
- group: docs
  title: ''
  type: Documentation
  url: https://gotify.net/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://gotify.net/api-docs
coverage:
  checked: '2026-10-26'
  detail: Gotify documentation is rendered via VitePress JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://gotify.net/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Gotify provides a simple, self-hosted server for sending and receiving messages via a REST API and WebSocket. It includes a web UI, client libraries, and mobile apps, enabling developers to integrate push notifications and messaging into their applications. The platform is open-source, supports user and application management, and offers documentation, SDKs, and a CLI for easy interaction.
layout: provider
modified: '2026-10-26'
name: Gotify
nav: Providers
network: true
overview: 'Gotify is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Open Source, Self-Hosted, and Notification.


  Gotify''s developer surface includes changelog, getting-started guide, documentation, API reference, and 7 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 35.7
    operational_transparency: 10.5
  previous_composite: 13.0
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
screenshot: https://apis.io/screenshots/gotify/gotify-2026-11-03T132948.png
security:
- kind: domain-security
  name: Gotify Domain Security
  slug: gotify-domain-security
  summary_line: TLSv1.3 · HSTS
slug: gotify
tags:
- Messaging
- Open Source
- Self-Hosted
- Notification
website: https://gotify.net/
---
