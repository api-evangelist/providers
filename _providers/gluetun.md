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
  href: https://artifacts.apis.io/gluetun/hosts/gluetun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gluetun-hosts.yml
- group: auth
  href: https://artifacts.apis.io/gluetun/security/gluetun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gluetun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gluetun.org
- group: docs
  title: ''
  type: Documentation
  url: https://gluetun.org/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://gluetun.org/guides/docker-compose/
- group: operate
  title: ''
  type: Support
  url: https://gluetun.org/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gluetun.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gluetun.org/privacy/
created: '2026-10-28'
description: Gluetun is an open-source VPN client that runs in a lightweight Docker container, supporting multiple VPN providers via OpenVPN and WireGuard, with DNS over TLS, firewall kill‑switch, and built‑in proxy servers. It provides a swiss‑army‑knife‑like solution for users to route traffic securely through a variety of VPN services, offering extensive configuration options and frequent updates. The project is maintained on GitHub and includes comprehensive documentation, Docker images, and community support.
image: https://gluetun.org/assets/img/og-cover.png
layout: provider
modified: '2026-10-28'
name: Gluetun
nav: Providers
network: true
overview: 'Gluetun is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include VPN, Open Source, Docker, WireGuard, and OpenVPN.


  Gluetun''s developer surface includes documentation, getting-started guide, support, and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 14.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gluetun/gluetun-2026-11-03T132849.png
security:
- kind: domain-security
  name: Gluetun Domain Security
  slug: gluetun-domain-security
  summary_line: TLSv1.3
slug: gluetun
tags:
- VPN
- Open Source
- Docker
- WireGuard
- OpenVPN
- Privacy
website: https://gluetun.org
---
