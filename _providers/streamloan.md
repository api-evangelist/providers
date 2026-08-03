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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamloan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://streamloan.io
created: '2026-07-17'
description: StreamLoan was a digital mortgage software company offering a point-of-sale (POS) and loan-origination platform that connected loan officers, borrowers, and real-estate agents to convert leads into funded home loans faster. Its toolkit spanned lead management, borrower communication and collaboration, workflow automation, document collection, security/privacy controls, and a branded borrower experience aimed at cutting the 40+ day mortgage close cycle. Backed by 500 Global. As of this enrichment pass the company appears defunct - streamloan.io is parked on a registrar IP and every developer/app/api/docs/portal subdomain is unreachable (DNS records remain but no host responds), and no public API or developer program was ever documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/streamloan.png
layout: provider
modified: '2026-07-21'
name: StreamLoan
nav: Providers
network: true
overview: StreamLoan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mortgage, Lending, Loan Origination, and Point of Sale.
random_paper: 33
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Streamloan Domain Security
  slug: streamloan-domain-security
  summary_line: no transport/DNS hardening detected
slug: streamloan
tags:
- Company
- Mortgage
- Lending
- Loan Origination
- Point of Sale
- Fintech
- Real Estate
- SaaS
- Banking
- Financial Services
website: https://streamloan.io
---
