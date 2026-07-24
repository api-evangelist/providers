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
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Cryptocurrency Payment Processor
  name: CryptAPI
  slug: cryptapi
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cryptapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cryptapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.cryptapi.io/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency Payment Processor
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptapi.png
layout: provider
modified: '2026-05-28'
name: CryptAPI
nav: Providers
network: true
overview: CryptAPI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.
random_paper: 9
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cryptapi/refs/heads/main/screenshots/cryptapi-2026-06-20T175306.png
security:
- kind: domain-security
  name: Cryptapi Domain Security
  slug: cryptapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cryptapi Vulnerability Disclosure
  slug: cryptapi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cryptapi
tags:
- Cryptocurrency
- Public APIs
website: https://docs.cryptapi.io/
---
