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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bykea-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bykea-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bykea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bykea.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bykea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bykea.com
created: '2026-07-17'
description: Bykea is a Karachi-based Pakistani mobility and logistics super-app that offers app-hailed motorbike rides, on-demand parcel and food delivery, cash pickup and drop-off, and digital payments across major Pakistani cities. It connects a large network of motorbike captains with riders and merchants, positioning itself as a low-cost transport, last-mile logistics, and financial services platform for the mass market. Backed by Prosus Ventures (Naspers), Bykea was added to the API Evangelist network as a mobility-sector portfolio lead; this profile has been enriched with the provider's public security surface (a live RFC 9116 security.txt and a HackerOne bug bounty program) and domain-security posture. No public developer portal, OpenAPI, or partner API documentation is exposed - the primary web surface sits behind Cloudflare bot protection.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bykea.png
layout: provider
modified: '2026-07-18'
name: Bykea
nav: Providers
network: true
overview: Bykea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Logistics, Delivery, and Ride Hailing.
random_paper: 48
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Bykea Domain Security
  slug: bykea-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bykea Vulnerability Disclosure
  slug: bykea-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bykea
tags:
- Company
- Mobility
- Logistics
- Delivery
- Ride Hailing
- Payments
- Pakistan
website: https://bykea.com
---
