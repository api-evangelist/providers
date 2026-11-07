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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/notifiarr/hosts/notifiarr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/notifiarr-hosts.yml
- group: other
  href: https://artifacts.apis.io/notifiarr/vendors/notifiarr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/notifiarr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/notifiarr/security/notifiarr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/notifiarr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://notifiarr.com/
created: '2026-10-28'
description: Notifiarr provides a notification aggregation and system monitoring platform that integrates with over 30 services such as Discord, Apprise, Authentik, Better Stack, Cronitor, Crowdsec, Dockwatch, Duplicacy, Emby, Fail2ban, Github, Jellyfin, Plex, Synology, Tracearr, Uptime Kuma, Watchsync, and Watchtower. Users can monitor network health, server metrics, and receive alerts via multiple channels including Discord, SMS, Email, Slack, Telegram, and Matterless. The service offers a web dashboard, API access, and extensive documentation for developers.
layout: provider
modified: '2026-10-28'
name: Notifiarr
nav: Providers
network: true
overview: Notifiarr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Notification, Monitoring, Integration, and Open Source.
random_paper: 14
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.1
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
screenshot: https://apis.io/screenshots/notifiarr/notifiarr-2026-11-03T140317.png
security:
- kind: domain-security
  name: Notifiarr Domain Security
  slug: notifiarr-domain-security
  summary_line: TLSv1.3
slug: notifiarr
tags:
- Company
- Notification
- Monitoring
- Integration
- Open Source
website: https://notifiarr.com/
---
