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
- description: Access to Open Data from Governments, Non-profits and NGOs around the world
  name: Socrata
  slug: socrata
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socrata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dev.socrata.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Access to Open Data from Governments, Non-profits and NGOs around the world
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/socrata.png
layout: provider
modified: '2026-05-28'
name: Socrata
nav: Providers
network: true
overview: Socrata publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 1
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
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/socrata/refs/heads/main/screenshots/socrata-2026-06-20T194121.png
security:
- kind: domain-security
  name: Socrata Domain Security
  slug: socrata-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: socrata
tags:
- Open Data
- Public APIs
website: https://dev.socrata.com/
---
