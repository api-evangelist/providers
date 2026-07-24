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
- description: Global macroeconomic data
  name: Econdb
  slug: econdb
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/econdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.econdb.com/api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Global macroeconomic data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/econdb.png
layout: provider
modified: '2026-05-28'
name: Econdb
nav: Providers
network: true
overview: Econdb publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.
random_paper: 7
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
screenshot: https://raw.githubusercontent.com/api-evangelist/econdb/refs/heads/main/screenshots/econdb-2026-06-20T180430.png
security:
- kind: domain-security
  name: Econdb Domain Security
  slug: econdb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: econdb
tags:
- Finance
- Public APIs
website: https://www.econdb.com/api/
---
