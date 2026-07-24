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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/republic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/republic-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://republic.com/security
- group: company
  title: ''
  type: Website
  url: https://republic.com
created: '2026-07-17'
description: 'Republic is a New York-based fintech and private investing platform (republic.com) that lets retail and accredited investors access early-stage startups, private companies, real estate, crypto, and other alternative assets through regulated investment crowdfunding offerings. Backed by prosus-ventures, Republic operates a consumer investing marketplace rather than a public developer platform: it publishes a security and compliance posture (SOC 2, ISO 27001) at republic.com/security but exposes no public API, developer portal, SDKs, or documentation surface at the time of this enrichment pass. This profile was surfaced as a portfolio-company lead and enriched with the provider-security signals that could be probed directly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/republic.png
layout: provider
modified: '2026-07-20'
name: Republic
nav: Providers
network: true
overview: Republic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investing, Crowdfunding, and Private Markets.
random_paper: 38
score:
  band: minimal
  composite: 9.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Republic Domain Security
  slug: republic-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Republic Trust Center
  slug: republic-trust-center
  summary_line: SOC 2, ISO 27001
slug: republic
tags:
- Company
- Fintech
- Investing
- Crowdfunding
- Private Markets
- Startups
- Crypto
website: https://republic.com
---
