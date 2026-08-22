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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.7
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Cryptocurrency Trading Platform
  name: KuCoin
  slug: kucoin
artifact_total: 4
asyncapis:
- description: 'AsyncAPI 2.6 description of KuCoin''s public WebSocket streaming API for the Classic (Spot/Margin) account. ## Obtaining the connection endpoint The WebSocket endpoint and a short-lived bearer token ar'
  name: KuCoin Public WebSocket API
  slug: kucoin-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kucoin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.kucoin.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.kucoin.com/blog
created: '2026-05-28'
description: Cryptocurrency Trading Platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kucoin.png
layout: provider
modified: '2026-05-29'
name: KuCoin
nav: Providers
network: true
overview: 'KuCoin publishes 1 API on the [APIs.io](https://apis.io/) network: KuCoin. Tagged areas include Cryptocurrency and Public APIs.


  The KuCoin catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  KuCoin''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 19
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: KuCoin API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: kucoin-asyncapi-spectral-rules
score:
  band: emerging
  composite: 19.3
  delta: -5.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 0.0
  previous_composite: 24.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/kucoin/refs/heads/main/screenshots/kucoin-2026-06-20T184213.png
security:
- kind: domain-security
  name: Kucoin Domain Security
  slug: kucoin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kucoin
tags:
- Cryptocurrency
- Public APIs
website: https://docs.kucoin.com/
---
