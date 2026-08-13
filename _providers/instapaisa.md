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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instapaisa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instapaisa.com
created: '2026-07-17'
description: InstaPaisa was an India-based personal-finance and lending fintech surfaced as a 500 Global (500 Startups) portfolio company and added to the API Evangelist network as a stub for enrichment. As of this enrichment pass the company appears defunct or absorbed — its domain instapaisa.com resolves (Amazon CloudFront) but redirects to InCred Finance (incred.com), an Indian digital lending / NBFC platform, indicating an acquisition or wind-down. No public developer portal, API documentation, or machine-readable API specification was found for InstaPaisa, so no API artifacts could be harvested or derived; only live domain-security signals for instapaisa.com were probed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instapaisa.png
layout: provider
modified: '2026-07-19'
name: InstaPaisa
nav: Providers
network: true
overview: InstaPaisa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Personal Finance, and Payments.
random_paper: 109
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instapaisa/refs/heads/main/screenshots/instapaisa-2026-07-25T222615.png
security:
- kind: domain-security
  name: Instapaisa Domain Security
  slug: instapaisa-domain-security
  summary_line: no transport/DNS hardening detected
slug: instapaisa
tags:
- Company
- Fintech
- Lending
- Personal Finance
- Payments
- India
- 500 Global
- Acquired
website: https://instapaisa.com
---
