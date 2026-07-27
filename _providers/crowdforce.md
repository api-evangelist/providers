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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdforce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crowdforce.io
created: '2026-07-17'
description: CrowdForce was a Nigerian fintech that operated the PayForce agent-banking network, deploying point-of-sale and digital financial-services agents to extend cash-in/cash-out, bill payments, and banking access to underbanked communities across Nigeria. Backed by 500 Global, its PayForce merchant/agent business merged with FairMoney's Fusion in 2023. As of this enrichment pass the crowdforce.io domain no longer serves an active product or developer surface. The homepage renders an empty Cloudflare-fronted shell and the /payforce path returns unrelated third-party (gambling) spam content, so no public API, developer portal, SDKs, or documentation could be verified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdforce.png
layout: provider
modified: '2026-07-18'
name: CrowdForce
nav: Providers
network: true
overview: CrowdForce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Agent Banking, and Financial Inclusion.
random_paper: 50
score:
  band: minimal
  composite: 7.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crowdforce/refs/heads/main/screenshots/crowdforce-2026-07-25T210807.png
security:
- kind: domain-security
  name: Crowdforce Domain Security
  slug: crowdforce-domain-security
  summary_line: TLSv1.3
slug: crowdforce
tags:
- Company
- Fintech
- Payments
- Agent Banking
- Financial Inclusion
- Nigeria
- Africa
website: https://crowdforce.io
---
