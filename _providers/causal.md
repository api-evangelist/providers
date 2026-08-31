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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/causal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.causal.app/
- group: start
  title: ''
  type: Login
  url: https://my.causal.app/
created: '2026-07-17'
description: Causal (causal.app) is a financial planning and business modeling platform for building spreadsheet-style models, forecasts, dashboards, and scenario analysis, aimed at finance teams and startups doing FP&A and extended planning and analysis (xP&A). Causal was acquired by Lucanet and its capabilities are now delivered as part of the Lucanet CFO Solution Platform; the marketing site redirects to Lucanet while existing customers sign in at my.causal.app. No public developer API, OpenAPI, or docs surface is currently published. Backed by Accel and Kindred Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/causal.png
layout: provider
modified: '2026-07-18'
name: Causal
nav: Providers
network: true
overview: Causal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial Planning, FP&A, and Business Modeling.
random_paper: 3
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/causal/refs/heads/main/screenshots/causal-2026-07-25T204814.png
security:
- kind: domain-security
  name: Causal Domain Security
  slug: causal-domain-security
  summary_line: TLSv1.2 · DMARC
slug: causal
tags:
- Company
- Fintech
- Financial Planning
- FP&A
- Business Modeling
- Forecasting
- Spreadsheets
- xP&A
- Software-as-a-Service
website: https://www.causal.app/
---
