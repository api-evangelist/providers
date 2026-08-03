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
  url: security/cibc-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://us.cibc.com
- group: company
  title: ''
  type: About
  url: https://us.cibc.com/en/about-us.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cibc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.cibc.com/en/privacy-security.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.cibc.com/en/legal.html
- group: other
  title: ''
  type: SignOn
  url: https://us.cibc.com/en/sign-on-hub.html
- group: other
  title: ''
  type: DataAggregation
  url: https://plaid.com/institutions/cibc/
- group: operate
  title: ''
  type: Support
  url: https://us.cibc.com/en/contact-us.html
created: '2026-07-23'
description: 'CIBC Bank USA is an Illinois state-chartered, FDIC-insured commercial bank (FDIC Cert #33306) headquartered at 120 South LaSalle Street in Chicago, Illinois. Formerly The PrivateBank and Trust Company, it was acquired in 2017 and rebranded, and today operates as a wholly owned US subsidiary of Canadian Imperial Bank of Commerce (CIBC) through the intermediate holding company CIBC Bancorp USA Inc. The bank focuses on commercial banking, capital markets, wealth management, trust services, private banking, and cross-border services for clients with North American operations, rather than mass-market retail. As a US regional institution, CIBC Bank USA publishes no first-party public developer portal or open API program; consumer-permissioned account and balance data is reached only through third-party aggregators such as Plaid, and the CIBC group has a data-access agreement with MX. It is not a documented direct Financial Data Exchange (FDX) participant and has published no explicit
  CFPB Section 1033 data-access posture, making its honest API surface aggregator-mediated only.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: CIBC Bank USA
nav: Providers
network: true
overview: 'CIBC Bank USA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Commercial Banking, and Regional Bank.


  CIBC Bank USA''s developer surface includes support and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 11.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cibc-us/refs/heads/main/screenshots/cibc-us-2026-07-25T205337.png
security:
- kind: domain-security
  name: Cibc Us Domain Security
  slug: cibc-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cibc-us
tags:
- Financial Services
- Banking
- United States
- Commercial Banking
- Regional Bank
- Private Banking
- Open Finance
- Data Aggregation
website: https://us.cibc.com
---
