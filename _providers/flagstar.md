---
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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flagstar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flagstar.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.flagstar.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flagstar-bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flagstar.com/legal-disclaimers/privacy.html
created: '2026-07-23'
description: 'Flagstar Bank, N.A. is the OCC-chartered national bank subsidiary of Flagstar Financial, Inc. (NYSE: FLG), the Hicksville, New York holding company formerly known as New York Community Bancorp (NYCB). It is one of the largest regional (super-regional) banks in the United States, formed when NYCB acquired Flagstar Bancorp in December 2022, converted Flagstar Bank, FSB into a national bank (Flagstar Bank, N.A.), and subsequently acquired certain assets and liabilities of Signature Bridge Bank from the FDIC in March 2023; the holding company rebranded to Flagstar Financial in October 2024. Flagstar operates in retail and commercial banking, mortgage origination and servicing, and warehouse lending. On the API front, Flagstar runs a first-party developer portal at developer.flagstar.com (a Broadcom/Layer7 "LivePortal" API Developer Portal), but as of this review it publishes no public, self-serve API products, API documentation, or downloadable OpenAPI/Swagger to anonymous visitors
  — all products are sign-in gated behind partner/consumer-team access. Flagstar has no publicly documented FDX (Financial Data Exchange) participation or CFPB Section 1033 data-access posture; consumer-permissioned data sharing appears to be available only through third-party aggregators (e.g. Plaid, Tink, TrueLayer) rather than a first-party public API.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Flagstar
nav: Providers
network: true
overview: Flagstar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, National Bank, and Super-Regional Bank.
random_paper: 5
score:
  band: minimal
  composite: 9.4
  delta: -2.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flagstar/refs/heads/main/screenshots/flagstar-2026-07-25T214709.png
security:
- kind: domain-security
  name: Flagstar Domain Security
  slug: flagstar-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: flagstar
tags:
- Financial Services
- Banking
- United States
- National Bank
- Super-Regional Bank
- Mortgage
- Open Finance
- Data Aggregation
website: https://www.flagstar.com
---
