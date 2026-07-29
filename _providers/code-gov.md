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
    agent_card: false
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
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The primary platform for Open Source and code sharing for the U.S. Federal Government
  name: Code.gov
  slug: codegov
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/code-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://code.gov
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: The primary platform for Open Source and code sharing for the U.S. Federal Government
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/code-gov.png
layout: provider
modified: '2026-05-28'
name: Code.gov
nav: Providers
network: true
overview: Code.gov publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 68
score:
  band: minimal
  composite: 6.5
  delta: -1.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/code-gov/refs/heads/main/screenshots/code-gov-2026-06-20T174654.png
security:
- kind: domain-security
  name: Code Gov Domain Security
  slug: code-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: code-gov
tags:
- Government
- Public APIs
website: https://code.gov
---
