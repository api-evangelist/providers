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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finmark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finmark.com/
created: '2026-07-17'
description: 'Finmark was a financial planning, modeling, and forecasting SaaS platform for startups and small businesses, backed by Bessemer Venture Partners, letting founders build budgets, cash-flow runway, hiring plans, and scenario models without spreadsheets. It was acquired by BILL (bill.com) and wound down as a standalone product: as of this enrichment pass finmark.com and www.finmark.com return a 301 permanent redirect to https://www.bill.com/. There is no longer an independent Finmark developer portal, API, documentation, pricing, or status page to enrich; the domain-security probe below reflects the residual finmark.com DNS/TLS surface only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finmark.png
layout: provider
modified: '2026-07-19'
name: Finmark
nav: Providers
network: true
overview: Finmark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud, Financial Planning, FinTech, and SaaS.
random_paper: 66
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finmark/refs/heads/main/screenshots/finmark-2026-07-25T214541.png
security:
- kind: domain-security
  name: Finmark Domain Security
  slug: finmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finmark
tags:
- Company
- Cloud
- Financial Planning
- FinTech
- SaaS
- Startups
- Acquired
- Forecasting
website: https://finmark.com/
---
