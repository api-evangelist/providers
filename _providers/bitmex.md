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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 5.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Real-Time Cryptocurrency derivatives trading platform based in Hong Kong
  name: Bitmex
  slug: bitmex
artifact_total: 5
asyncapis:
- description: AsyncAPI 2.6 specification for the BitMEX public Realtime WebSocket API. BitMEX exposes a single WebSocket endpoint at `wss://ws.bitmex.com/realtime`. Clients subscribe to one or more topics ("tables"
  name: BitMEX Realtime WebSocket API
  slug: bitmex-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitmex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitmex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bitmex.com/app/apiOverview
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.bitmex.com/feed
created: '2026-05-28'
description: Real-Time Cryptocurrency derivatives trading platform based in Hong Kong
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitmex.png
layout: provider
modified: '2026-05-29'
name: Bitmex
nav: Providers
network: true
overview: 'Bitmex publishes 1 API on the [APIs.io](https://apis.io/) network: Bitmex. Tagged areas include Cryptocurrency and Public APIs.


  The Bitmex catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bitmex''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 37
rules:
- name: Bitmex API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 7
  slug: bitmex-asyncapi-spectral-rules
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 33.3
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 60.5
    operational_transparency: 0.0
  previous_composite: 22.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitmex/refs/heads/main/screenshots/bitmex-2026-06-20T173314.png
security:
- kind: domain-security
  name: Bitmex Domain Security
  slug: bitmex-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bitmex Vulnerability Disclosure
  slug: bitmex-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: bitmex
tags:
- Cryptocurrency
- Public APIs
website: https://www.bitmex.com/app/apiOverview
---
