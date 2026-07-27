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
  type: DomainSecurity
  url: security/viajanet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/viajanet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/viajanet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/viajanet-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/viajanet-well-known.yml
- group: company
  title: ''
  type: Website
  url: http://www.viajanet.com.br/
created: '2026-07-17'
description: Viajanet is a Brazilian online travel agency (OTA) operated within the Despegar group, selling flights, hotels, vacation packages, car rentals and travel insurance to consumers in Brazil through www.viajanet.com.br. It was surfaced as a portfolio company of Redpoint Ventures and added to the API Evangelist network for enrichment. Viajanet publishes no public developer API, SDK, or developer portal; the enrichment pass captured its live security surface (a published security.txt with a Bugcrowd private bug bounty program run by the Despegar application-security team) and its domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/viajanet.png
layout: provider
modified: '2026-07-21'
name: Viajanet
nav: Providers
network: true
overview: Viajanet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Online Travel Agency, Flights, and Hotels.
random_paper: 34
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Viajanet Domain Security
  slug: viajanet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Viajanet Vulnerability Disclosure
  slug: viajanet-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: viajanet
tags:
- Company
- Travel
- Online Travel Agency
- Flights
- Hotels
- Booking
- Brazil
- E-commerce
website: http://www.viajanet.com.br/
---
