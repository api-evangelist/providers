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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Cryptocurrency Trading Platform
  name: Coinbase Pro
  slug: coinbase-pro
artifact_total: 6
asyncapis:
- description: 'AsyncAPI specification covering the two publicly documented Coinbase real-time WebSocket feeds: 1. **Coinbase Exchange (formerly Coinbase Pro) WebSocket Feed** - URL: `wss://ws-feed.exchange.coinbase.'
  name: Coinbase WebSocket APIs
  slug: coinbase-pro-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinbase-pro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinbase-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.pro.coinbase.com/#api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency Trading Platform
graphqls:
- description: This conceptual GraphQL schema models the Coinbase Advanced Trade API (formerly Coinbase Pro). The schema covers the full surface of the Advanced Trade REST API as documented at https://docs.cdp.coinb
  name: Coinbase Advanced Trade GraphQL Schema
  slug: coinbase-pro-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinbase-pro.png
layout: provider
modified: '2026-05-29'
name: Coinbase Pro
nav: Providers
network: true
overview: 'Coinbase Pro publishes 1 API on the [APIs.io](https://apis.io/) network: Coinbase Pro. Tagged areas include Cryptocurrency and Public APIs.


  The Coinbase Pro catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 0
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Coinbase Pro API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: coinbase-pro-asyncapi-spectral-rules
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 84.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 11.4
    contract_quality: 54.8
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 11.4
    operational_transparency: 0.0
  previous_composite: 21.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinbase-pro/refs/heads/main/screenshots/coinbase-pro-2026-06-20T174731.png
security:
- kind: domain-security
  name: Coinbase Pro Domain Security
  slug: coinbase-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinbase Pro Vulnerability Disclosure
  slug: coinbase-pro-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: coinbase-pro
tags:
- Cryptocurrency
- Public APIs
website: https://docs.pro.coinbase.com/#api
---
