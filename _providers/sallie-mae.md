---
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sallie-mae-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.salliemae.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salliemae.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salliemae.com/legal/privacy-policies-and-notices/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SallieMae
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salliemae
- group: company
  title: ''
  type: Blog
  url: https://www.salliemae.com/resources/
created: '2026-07-23'
description: 'Sallie Mae Bank is a Utah state-chartered industrial bank (industrial loan company) founded on November 28, 2005 and headquartered in Salt Lake City, Utah, operating as the FDIC-insured banking subsidiary (FDIC cert #58177) of SLM Corporation (NASDAQ SLM), the publicly traded, S&P 400 consumer-finance company best known as the largest originator of private student loans in the United States. Beyond student and education lending, the bank offers retail deposit products including high-yield savings accounts, money market accounts, and certificates of deposit through salliemae.com. Sallie Mae Bank does not operate a first-party public developer program - there is no developer.salliemae.com portal, no api.salliemae.com host, and no published OpenAPI/Swagger definitions. Consumer account and transaction data is reachable only on a permissioned basis through third-party data aggregators (historically Plaid), and no first-party FDX data-access API or published CFPB Section 1033 data-rights
  posture could be confirmed. This is an identity-only, aggregator-access record reflecting the honest reality that this institution exposes no public API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Sallie Mae Bank
nav: Providers
network: true
overview: 'Sallie Mae Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Industrial Bank, and Student Loans.


  Sallie Mae Bank''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 14.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.8
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Sallie Mae Domain Security
  slug: sallie-mae-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sallie-mae
tags:
- Financial Services
- Banking
- United States
- Industrial Bank
- Student Loans
- Savings
- Consumer Finance
- Data Aggregation
website: https://www.salliemae.com/
---
