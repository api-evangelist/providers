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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Exchange rates and currency conversion
  name: Bank of Russia
  slug: bank-of-russia
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-russia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cbr.ru/development/SXML/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Exchange rates and currency conversion
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-russia.png
layout: provider
modified: '2026-05-28'
name: Bank of Russia
nav: Providers
network: true
overview: Bank of Russia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Currency Exchange and Public APIs.
random_paper: 37
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-russia/refs/heads/main/screenshots/bank-of-russia-2026-06-20T172948.png
security:
- kind: domain-security
  name: Bank Of Russia Domain Security
  slug: bank-of-russia-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bank-of-russia
tags:
- Currency Exchange
- Public APIs
website: https://www.cbr.ru/development/SXML/
---
