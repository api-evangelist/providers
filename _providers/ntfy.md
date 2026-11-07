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
- group: auth
  href: https://artifacts.apis.io/ntfy/well-known/ntfy-ntfy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ntfy-ntfy-security.txt
- group: agent
  href: https://artifacts.apis.io/ntfy/well-known/ntfy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ntfy-well-known.yml
- group: other
  href: https://artifacts.apis.io/ntfy/vendors/ntfy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ntfy-vendors.yml
- group: other
  href: https://artifacts.apis.io/ntfy/hosts/ntfy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ntfy-hosts.yml
- group: build
  href: https://artifacts.apis.io/ntfy/packages/ntfy-packages.yml
  title: ''
  type: SDKs
  url: packages/ntfy-packages.yml
- group: build
  href: https://artifacts.apis.io/ntfy/packages/ntfy-packages.yml
  title: ''
  type: Packages
  url: packages/ntfy-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ntfy.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.ntfy.sh/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ntfy.sh/releases/
- group: company
  title: ''
  type: Blog
  url: https://blog.ntfy.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ntfy.sh/
- group: auth
  href: https://artifacts.apis.io/ntfy/security/ntfy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ntfy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ntfy.sh/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI or other machine‑readable contract was found despite public documentation.
  evidence:
  - status: 200
    url: https://ntfy.sh/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: ntfy provides a simple HTTP‑based publish‑subscribe notification service that lets developers send push notifications to phones, desktops, or other devices via a straightforward REST API or command‑line tools. It is open‑source, self‑hostable, and offers both a hosted service at ntfy.sh and a Docker image for private deployments. Features include topic‑based messaging, message retention, access control, and integration with mobile apps for Android, iOS, and desktop platforms.
image: https://ntfy.sh/static/img/ntfy.png
layout: provider
modified: '2026-10-26'
name: ntfy
nav: Providers
network: true
overview: 'ntfy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Notification, Open Source, Self-Hosted, and Pub/Sub.


  ntfy''s developer surface includes changelog, engineering blog, documentation, and 10 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 39.3
    operational_transparency: 26.3
  previous_composite: 15.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ntfy/ntfy-2026-11-03T140336.png
security:
- kind: domain-security
  name: Ntfy Domain Security
  slug: ntfy-domain-security
  summary_line: TLSv1.3
slug: ntfy
tags:
- Notification
- Open Source
- Self-Hosted
- Pub/Sub
website: https://ntfy.sh/
---
