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
- description: Educational content about the US Health Insurance Marketplace
  name: Healthcare.gov
  slug: healthcaregov
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/healthcare-gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.healthcare.gov/developers/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Educational content about the US Health Insurance Marketplace
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/healthcare-gov.png
layout: provider
modified: '2026-05-28'
name: Healthcare.gov
nav: Providers
network: true
overview: Healthcare.gov publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 24
score:
  band: minimal
  composite: 6.0
  delta: -1.7
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
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/healthcare-gov/refs/heads/main/screenshots/healthcare-gov-2026-06-20T182558.png
security:
- kind: domain-security
  name: Healthcare Gov Domain Security
  slug: healthcare-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: healthcare-gov
tags:
- Health
- Public APIs
website: https://www.healthcare.gov/developers/
---
