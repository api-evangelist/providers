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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Build hybrid smart contracts with Chainlink
  name: Chainlink
  slug: chainlink
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chainlink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chainlink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chain.link/developer-resources
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Build hybrid smart contracts with Chainlink
graphqls:
- description: Chainlink exposes a GraphQL API as part of its node operator interface — the same API powering the Chainlink Operator UI (formerly Chainlink Dashboard). It provides programmatic access to node managem
  name: Chainlink GraphQL API
  slug: chainlink-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chainlink.png
layout: provider
modified: '2026-05-28'
name: Chainlink
nav: Providers
network: true
overview: Chainlink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain and Public APIs.
random_paper: 61
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
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chainlink/refs/heads/main/screenshots/chainlink-2026-06-20T174200.png
security:
- kind: domain-security
  name: Chainlink Domain Security
  slug: chainlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chainlink Vulnerability Disclosure
  slug: chainlink-vulnerability-disclosure
  summary_line: Hackerone
slug: chainlink
tags:
- Blockchain
- Public APIs
website: https://chain.link/developer-resources
---
