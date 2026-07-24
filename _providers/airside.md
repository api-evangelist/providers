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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airside-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airsidemobile.com/
created: '2026-07-17'
description: 'Airside (formerly Airside Mobile) is a digital identity and mobile credential product whose website airsidemobile.com now permanently redirects (HTTP 301) to Entrust''s Airside app page, indicating the product and its assets were acquired by Entrust. As of this enrichment pass no public API, OpenAPI specification, SDK, developer portal, or developer documentation surface could be discovered: developer/api/docs subdomains do not resolve and the root domain and /.well-known/security.txt both redirect off-site to Entrust. The company was originally surfaced as a bain-capital-ventures portfolio lead (sector ai-apps) and remains a stub pending any first-party developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airside.png
layout: provider
modified: '2026-07-17'
name: Airside
nav: Providers
network: true
overview: Airside is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Digital Identity, Mobile Credentials, and Identity Verification.
random_paper: 23
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
security:
- kind: domain-security
  name: Airside Domain Security
  slug: airside-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airside
tags:
- Company
- Ai Apps
- Digital Identity
- Mobile Credentials
- Identity Verification
- Acquired
- Entrust
website: https://airsidemobile.com/
---
