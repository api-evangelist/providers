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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://nowpay.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nowpay-domain-security.yml
created: '2026-07-17'
description: NowPay is an employer-integrated financial wellness platform whose core product lets employees access their earned salary early and repay it in installments, positioned as a workplace benefit rather than a consumer lender. It was surfaced as a portfolio company of 500 Global and added to the API Evangelist network. As of this enrichment pass NowPay publishes only a client-rendered marketing site (nowpay.cash, which redirects to nowpay.com) with no public developer portal, API reference, OpenAPI, SDKs, or /.well-known discovery surface; every probed path returns the single-page-app shell. This profile therefore carries identity and a live domain-security probe only.
image: https://elasticbeanstalk-us-east-1-927288046810.s3.us-east-1.amazonaws.com/Logos/NowPay%20Logo.png
layout: provider
modified: '2026-07-20'
name: Nowpay
nav: Providers
network: true
overview: Nowpay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial Wellness, Earned Wage Access, and Salary Advance.
random_paper: 19
score:
  band: minimal
  composite: 1.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nowpay/refs/heads/main/screenshots/nowpay-2026-08-07T185638.png
security:
- kind: domain-security
  name: Nowpay Domain Security
  slug: nowpay-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nowpay
tags:
- Company
- Fintech
- Financial Wellness
- Earned Wage Access
- Salary Advance
- Payroll
- Employee Benefits
- Embedded Finance
- Payments
website: https://nowpay.com
---
