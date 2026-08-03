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
    consent_identity: false
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
  score: 0.0
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: Historical partner/owner REST API used by fleet-management integrators (CarSync, FleetWire, Kitts) to sync bookings onto external calendars, block vehicle availability, generate invoices for professio
  name: Getaround Owner API
  slug: getaround-owner-api
- description: Native iOS (Objective-C) SDK for the Getaround Connect smart-lock hardware fitted to shared vehicles - discovers nearby Connect devices over Bluetooth LE and issues lock/unlock commands via BlueforceC
  name: Getaround Connect Blueforce SDK
  slug: getaround-connect-blueforce-sdk
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/getaround-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getaround-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Getaround
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getaround
- group: company
  title: ''
  type: Website
  url: https://getaround.com
- group: docs
  title: ''
  type: Documentation
  url: https://getaround.com/docs/api/owner/v1
- group: company
  title: ''
  type: Blog
  url: https://getaround.com/blog/feed
created: '2026-07-03'
description: Getaround was a peer-to-peer and connected car-sharing marketplace (merged with France's Drivy in 2019) that let owners list personal or fleet vehicles fitted with Getaround Connect - a BLE/telematics smart-lock kit - for keyless, app-based rental. Getaround historically ran a documented Owner API and webhook program for fleet-management partners (CarSync, FleetWire, Invers Fleet Hawk) plus a native Connect Blueforce BLE SDK for lock/unlock. OPERATING STATUS (as of 2026-07-03) - the company is winding down - it shut down U.S. operations (including its HyreCar subsidiary) in February 2025, sold its European car-sharing business to Denmark's GoMore ApS effective April 30, 2026, and Getaround Inc.'s board voted June 5, 2026 to pursue formal Delaware dissolution and liquidation (stockholder vote July 29, 2026, no distribution expected). The api.getaround.com API host no longer resolves and its owner API documentation page is now empty, so the API described here is historical/discontinued
  rather than currently operable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getaround.png
layout: provider
modified: '2026-07-03'
name: Getaround
nav: Providers
network: true
overview: 'Getaround publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Car Sharing, Mobility, Connected Car, Fleet Management, and Peer to Peer.


  Getaround''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getaround/refs/heads/main/screenshots/getaround-2026-07-25T215717.png
security:
- kind: domain-security
  name: Getaround Domain Security
  slug: getaround-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getaround Vulnerability Disclosure
  slug: getaround-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: getaround
tags:
- Car Sharing
- Mobility
- Connected Car
- Fleet Management
- Peer to Peer
- Discontinued
website: https://getaround.com
---
