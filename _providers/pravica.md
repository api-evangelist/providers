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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pravica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pravica.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pravicasuite
- group: company
  title: ''
  type: Twitter
  url: https://x.com/pravicasuite
created: '2026-07-17'
description: Pravica is a financial-technology company providing institutional-grade infrastructure for programmable money. It enables banks, fintechs, and enterprises to launch secure, compliant digital payment systems spanning online and offline payments, remittances, and global settlement. The Pravica suite includes consumer-facing products such as Walletify and s3.money. Backed by 500 Global, Pravica was added to the API Evangelist network as a portfolio-lead stub. As of this enrichment pass the public site is marketing-only with no developer portal, API documentation, OpenAPI, SDK, or /.well-known discovery surface found, so this profile carries identity and domain-security signal but no API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pravica.png
layout: provider
modified: '2026-07-20'
name: Pravica
nav: Providers
network: true
overview: Pravica is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Payments, and Programmable Money.
random_paper: 146
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
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Pravica Domain Security
  slug: pravica-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pravica
tags:
- Company
- Financial Services
- Fintech
- Payments
- Programmable Money
- Infrastructure
- Remittances
- Settlement
website: https://pravica.io
---
