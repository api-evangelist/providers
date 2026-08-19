---
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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.everbank.com/
- group: company
  title: ''
  type: About
  url: https://www.everbank.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.everbank.com/about/news
- group: auth
  title: ''
  type: Security
  url: https://www.everbank.com/security
- group: operate
  title: ''
  type: Support
  url: https://www.everbank.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everbank.com/legal/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy-central.securiti.ai/#/notices/b47ec243-ddfe-430d-8d01-17047bea9f8d
- group: start
  title: ''
  type: Login
  url: https://secure.everbank.com/
- group: start
  title: ''
  type: SignUp
  url: https://apply.everbank.com/openaccount-sb/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.everbank.com/rates
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everbank
created: '2026-07-23'
description: EverBank, N.A. is a Jacksonville, Florida based national bank (Member FDIC) focused on high-yield consumer deposits, business and treasury banking, and commercial lending, serving customers nationwide online plus a small network of financial centers in Florida, California and New York. The bank operated as TIAA Bank from 2017 until 2023, when it was acquired by an investor group and reverted to the EverBank brand as an independent institution. Like most US banks, EverBank publishes NO first-party public developer API or developer portal; there is no documented open-banking, FDX, or CFPB Section 1033 data-access API exposed directly. Consumer-permissioned account data is reached only through third-party aggregators (e.g. Plaid, MX, Finicity), which is the honest, non-fabricated posture recorded here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: EverBank
nav: Providers
network: true
overview: 'EverBank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, National Bank, and Deposits.


  EverBank''s developer surface includes engineering blog, support, signup flow, pricing, and 8 more developer resources.'
random_paper: 101
score:
  band: emerging
  composite: 14.7
  delta: -2.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everbank/refs/heads/main/screenshots/everbank-2026-07-25T213722.png
security:
- kind: domain-security
  name: Everbank Domain Security
  slug: everbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: everbank
tags:
- Financial Services
- Banking
- United States
- National Bank
- Deposits
- Commercial Banking
- Open Finance
- Data Aggregation
website: https://www.everbank.com/
---
