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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jadu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jadu.io
created: '2026-07-17'
description: 'Jadu is a General Catalyst-backed company tracked in the API Evangelist network. Its public site at jadu.io presents JADU as AI-powered crypto trading automation built on the Hyperliquid decentralized exchange. As of this enrichment pass the site is a single-page marketing shell with no public developer surface: no developer portal, API documentation, OpenAPI/AsyncAPI specification, SDKs, CLI, Postman collection, changelog, pricing page, status page, GitHub organization, or /.well-known discovery documents were found (the host returns its index page for every path, so probed well-known and llms.txt hits are SPA catch-alls, not real documents). This profile therefore carries identity and a domain-security probe only; no API artifacts could be honestly derived because the provider publishes no machine-readable API surface to ground them.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jadu.png
layout: provider
modified: '2026-07-19'
name: Jadu
nav: Providers
network: true
overview: Jadu is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Trading, Artificial Intelligence, and Automation.
random_paper: 0
score:
  band: minimal
  composite: 1.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.2
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jadu/refs/heads/main/screenshots/jadu-2026-07-25T223037.png
security:
- kind: domain-security
  name: Jadu Domain Security
  slug: jadu-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jadu
tags:
- Company
- Cryptocurrency
- Trading
- Artificial Intelligence
- Automation
- Hyperliquid
- Decentralized Finance
website: https://jadu.io
---
