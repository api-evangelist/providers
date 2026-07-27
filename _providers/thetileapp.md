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
  type: VulnerabilityDisclosure
  url: security/thetileapp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/life360
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thetileapp-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thetileapp-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thetileapp-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thetileapp-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.thetileapp.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thetileapp.com/en-us/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thetileapp.com/en-us/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://thetileapp.com
created: '2026-07-17'
description: Tile is a consumer Bluetooth-tracker company whose Tile Mate, Pro, Slim, and Sticker devices help people find everyday items such as keys, wallets, bags, and phones, backed by the crowd-sourced Tile "Find" network that anonymously relays location when another Tile user passes a lost item. Founded in 2012, Tile was acquired by Life360 in 2021 and now operates as part of the Life360 family-safety platform. Tile publishes consumer apps for iOS and Android and a support and legal surface, but does not offer an official public developer API, developer portal, or SDK; only third-party community libraries wrap its private app API. This API Evangelist profile captures the company's public web and security-program surface. Surfaced as a portfolio company of Slow Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thetileapp.png
layout: provider
modified: '2026-07-21'
name: Tile (thetileapp)
nav: Providers
network: true
overview: 'Tile (thetileapp) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bluetooth, Location, Tracking, and Consumer Electronics.


  Tile (thetileapp)''s developer surface includes support and 9 more developer resources.'
random_paper: 52
score:
  band: minimal
  composite: 13.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 13.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Thetileapp Domain Security
  slug: thetileapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thetileapp Vulnerability Disclosure
  slug: thetileapp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: thetileapp
tags:
- Company
- Bluetooth
- Location
- Tracking
- Consumer Electronics
- IoT
- Find My
- Life360
website: https://thetileapp.com
---
