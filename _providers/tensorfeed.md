---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Real-time AI news, model pricing, service status, and agent activity feeds
  name: TensorFeed
  slug: tensorfeed
artifact_total: 3
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/tensorfeed-a2a.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tensorfeed-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tensorfeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tensorfeed.ai/developers
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Real-time AI news, model pricing, service status, and agent activity feeds
layout: provider
modified: '2026-05-28'
name: TensorFeed
nav: Providers
network: true
overview: TensorFeed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Machine Learning and Public APIs.
random_paper: 18
score:
  band: minimal
  composite: 5.4
  delta: -1.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tensorfeed/refs/heads/main/screenshots/tensorfeed-2026-06-20T195119.png
security:
- kind: domain-security
  name: Tensorfeed Domain Security
  slug: tensorfeed-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Tensorfeed Vulnerability Disclosure
  slug: tensorfeed-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tensorfeed
tags:
- Machine Learning
- Public APIs
website: https://tensorfeed.ai/developers
---
