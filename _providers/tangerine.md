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
  url: security/tangerine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tangerine.ca
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tangerine.ca/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tangerine.ca/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.tangerine.ca/en/help-centre
- group: company
  title: ''
  type: Blog
  url: https://www.tangerine.ca/en/thejuice
- group: start
  title: ''
  type: SignUp
  url: https://www.tangerine.ca/app/#/visitor-enroll/instructions?locale=en_CA
- group: start
  title: ''
  type: Login
  url: https://www.tangerine.ca/app/#/login/login-id?locale=en_CA
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/tangerine-bank
created: '2026-07-23'
description: Tangerine is a Canadian direct (branchless) bank headquartered in Toronto, Ontario, and a federally regulated Schedule I bank chartered as Tangerine Bank (institution number 614). Founded in 1997 as ING Direct Canada, it was acquired by Scotiabank in 2012 and rebranded as Tangerine in 2014; it remains a separate legal entity operating as Scotiabank's digital-banking arm, serving roughly two million clients with no-fee chequing and savings accounts, GICs, mortgages, mutual funds, and a cash-back Mastercard delivered entirely through mobile and web. On API and open-finance posture, Tangerine publishes no first-party public developer portal or downloadable API specifications; Canada has no operational consumer-driven-banking mandate yet (the federal framework is legislated but not live), so third-party access to Tangerine account and transaction data today is aggregator-based via Plaid and Finicity (Mastercard) rather than through a documented first-party API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Tangerine
nav: Providers
network: true
overview: 'Tangerine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Digital Bank, and Neobank.


  Tangerine''s developer surface includes support, engineering blog, signup flow, and 6 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 17.2
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.2
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
  name: Tangerine Domain Security
  slug: tangerine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tangerine
tags:
- Financial Services
- Banking
- Canada
- Digital Bank
- Neobank
- Schedule I Bank
- Data Aggregation
- Interac
website: https://www.tangerine.ca
---
