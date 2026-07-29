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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://meso.network
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meso-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/meso-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meso-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://meso.network/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meso-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meso-llms.txt
created: '2026-07-17'
description: Meso is payment infrastructure designed for crypto. Backed by Ribbit Capital, the company is positioned as a payments-rails provider for the cryptocurrency sector. As of this enrichment pass its public web presence is a single-page marketing site at meso.network with no publicly documented developer portal, API reference, or OpenAPI definition surfaced yet. The one machine-readable artifact the company publishes is a PGP-signed RFC 9116 security.txt at /.well-known/security.txt declaring a security contact and disclosure policy. This profile was added to the API Evangelist network as a Ribbit Capital portfolio lead and is tracked for future API surface as the product launches.
image: https://meso.network/assets/img/open-meta.png
layout: provider
modified: '2026-07-20'
name: Meso
nav: Providers
network: true
overview: Meso is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Payments, Payment Infrastructure, and Cryptocurrency.
random_paper: 41
score:
  band: minimal
  composite: 9.8
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Meso Domain Security
  slug: meso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meso Vulnerability Disclosure
  slug: meso-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meso
tags:
- Company
- Crypto
- Payments
- Payment Infrastructure
- Cryptocurrency
- Fintech
- Blockchain
website: https://meso.network
---
