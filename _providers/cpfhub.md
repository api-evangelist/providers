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
- description: Brazilian CPF lookup — returns full name, birth date, and gender for any CPF
  name: CPFHub
  slug: cpfhub
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cpfhub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cpfhub.io
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Brazilian CPF lookup — returns full name, birth date, and gender for any CPF
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cpfhub.png
layout: provider
modified: '2026-05-28'
name: CPFHub
nav: Providers
network: true
overview: CPFHub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 20
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cpfhub/refs/heads/main/screenshots/cpfhub-2026-06-20T175156.png
security:
- kind: domain-security
  name: Cpfhub Domain Security
  slug: cpfhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cpfhub
tags:
- Government
- Public APIs
website: https://cpfhub.io
---
