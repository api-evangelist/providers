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
  url: security/southstate-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.southstatebank.com/
- group: operate
  title: ''
  type: Support
  url: https://www.southstatebank.com/global/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.southstatebank.com/global/help/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.southstatebank.com/global/help/online-privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/south-state-bank
created: '2026-07-23'
description: 'SouthState Bank, National Association is an OCC-chartered national commercial bank headquartered in Winter Haven, Florida, and the principal subsidiary of SouthState Bank Corporation (NASDAQ: SSB). Formed through the 2020 merger of South State Corporation and CenterState Bank and redomiciled to Florida in 2025, it holds roughly $67 billion in assets and operates across the Southeast, Texas, Colorado, and Virginia. Like most US regional banks, SouthState runs no public first-party developer portal and publishes no downloadable OpenAPI or Swagger definitions. Consumer-permissioned data access is delivered through third-party aggregators rather than a direct API: the Open Banking Tracker records SouthState reachable via Plaid only, with no documented Financial Data Exchange (FDX) endpoint and no published CFPB Section 1033 data-access surface. Its open-finance posture is therefore aggregator-mediated, not a self-serve developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: SouthState Bank
nav: Providers
network: true
overview: 'SouthState Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Regional Bank, and National Bank.


  SouthState Bank''s developer surface includes support and 5 more developer resources.'
random_paper: 64
score:
  band: minimal
  composite: 11.2
  delta: -3.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Southstate Bank Domain Security
  slug: southstate-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: southstate-bank
tags:
- Financial Services
- Banking
- United States
- Regional Bank
- National Bank
- Open Finance
- Data Aggregation
website: https://www.southstatebank.com/
---
