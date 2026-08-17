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
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bsquare-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bsquare.com/vulnerability-reporting
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bsquare-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bsquare-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bsquare-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://bsquare.com
created: '2026-07-17'
description: Bsquare is an IoT and edge-software company known for Windows IoT device licensing, OS consulting (Windows, Linux, Android), device management, and its DataV IoT analytics and SquareOne data platform. Bsquare was acquired by Kontron; the bsquare.com domain now 301-redirects to www.kontron-americas.com, and the Bsquare brand operates as part of Kontron's connected-device software portfolio serving healthcare, avionics, energy, manufacturing, logistics, transportation, and hospitality. No independent public developer API or documentation surface is currently published; this profile carries the honest enrichment of the domain's live security and DNS posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bsquare.png
layout: provider
modified: '2026-07-18'
name: Bsquare
nav: Providers
network: true
overview: Bsquare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Edge Computing, Device Management, and Windows IoT.
random_paper: 10
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
screenshot: https://raw.githubusercontent.com/api-evangelist/bsquare/refs/heads/main/screenshots/bsquare-2026-07-25T204012.png
security:
- kind: domain-security
  name: Bsquare Domain Security
  slug: bsquare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bsquare Vulnerability Disclosure
  slug: bsquare-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bsquare
tags:
- Company
- IoT
- Edge Computing
- Device Management
- Windows IoT
- IoT Analytics
- Kontron
website: https://bsquare.com
---
