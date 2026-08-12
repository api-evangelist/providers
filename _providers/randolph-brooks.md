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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: start
  title: ''
  type: Login
  url: https://www.rbfcu.org/online/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/randolph-brooks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rbfcu.org
- group: company
  title: ''
  type: Blog
  url: https://www.rbfcu.org/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rbfcu.org/privacy-security
- group: operate
  title: ''
  type: Support
  url: https://www.rbfcu.org/contact-us
created: '2026-07-23'
description: Randolph-Brooks Federal Credit Union (RBFCU) is a member-owned, not-for-profit federal credit union headquartered in Live Oak, Texas, federally insured by the NCUA and serving more than one million members across Texas and beyond. Chartered as a federal credit union rather than a state or national bank, RBFCU is one of the largest credit unions in the United States by membership and assets, offering retail banking, mortgages, auto loans, credit cards, and deposit products through branches and digital channels. As a member-focused retail institution, RBFCU publishes no first-party public developer program, API documentation, or downloadable OpenAPI/Swagger specifications; consumer-permissioned account data is reached through third-party aggregators (such as Plaid, MX, Finicity, or Akoya) rather than a directly documented open-finance API, and it publishes no stated CFPB Section 1033 data-access posture or documented FDX participation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23T15:30:00Z'
name: Randolph-Brooks FCU
nav: Providers
network: true
overview: 'Randolph-Brooks FCU is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Credit Union, and Retail Banking.


  Randolph-Brooks FCU''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 49
score:
  band: minimal
  composite: 11.3
  delta: 2.3
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Randolph Brooks Domain Security
  slug: randolph-brooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: randolph-brooks
tags:
- Financial Services
- Banking
- United States
- Credit Union
- Retail Banking
- Open Finance
- Data Aggregation
website: https://www.rbfcu.org
---
