---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.thetileapp.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tile-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tile-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tile-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/life360
created: '2026-07-17'
description: Tile is a consumer-electronics company known for its Bluetooth tracker devices, used to locate everyday items such as keys, wallets, bags, and phones through a companion mobile app and a crowd-sourced Find network. Tile was acquired by Life360 in 2021; its former site thetileapp.com now 301-redirects to life360.com. Surfaced as a portfolio company of Bessemer Venture Partners, Tile publishes no public developer API — this profile captures its security posture (security.txt, a HackerOne responsible-disclosure program, and probed domain security).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tile.png
layout: provider
modified: '2026-07-21'
name: Tile
nav: Providers
network: true
overview: Tile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Consumer Electronics, Bluetooth, and Tracking.
random_paper: 132
score:
  band: minimal
  composite: 6.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 6.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Tile Domain Security
  slug: tile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tile Vulnerability Disclosure
  slug: tile-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: tile
tags:
- Company
- Consumer
- Consumer Electronics
- Bluetooth
- Tracking
- Location
- IoT
- Hardware
website: https://www.thetileapp.com/
---
