---
access_model:
  confidence: medium
  label: Enterprise business APIs (advisor onboarding) + self-serve informational APIs on the developer portal
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
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
api_count: 9
apis:
- description: Self-serve informational API on the RBC External Developer Portal that accepts a postal code or keyword search and returns the address and hours of operation of the closest RBC branch, or a list of ne
  name: RBC Branch Locator API
  slug: branch-locator-api
- description: Self-serve informational API on the RBC External Developer Portal exposing RBC credit card product details, rates, and fees through a programmatic interface.
  name: RBC Credit Card Catalog API
  slug: credit-card-catalog-api
- description: Self-serve calculator API on the RBC External Developer Portal that computes the minimum down payment required for a given home purchase price under Canadian mortgage rules.
  name: RBC Minimum Down Payment API
  slug: minimum-down-payment-api
- description: Self-serve calculator API on the RBC External Developer Portal that returns the number of payments and amortization schedule for a mortgage given amount, amortization period, interest, and payment det
  name: RBC Amortization Schedule API
  slug: amortization-schedule-api
- description: Partner-gated Business Banking payment API that lets companies send near real-time Interac e-Transfer transactions in Canada from an embedded, real-time service, with optional enriched remittance/invo
  name: RBC Move Money API (Interac e-Transfer)
  slug: move-money-interac-api
- description: 'Partner-gated Business Banking payment API for embedding RBC payment capabilities into a company''s financial systems. Documented on the RBC Royal Bank Business Banking APIs page; onboarding is via an '
  name: RBC Pay API
  slug: rbc-pay-api
- description: Partner-gated Business Banking informational API providing real-time account balance and transaction information for a company's RBC accounts. Onboarding is via an RBC Advisor.
  name: RBC Balance and Transactions API
  slug: balance-and-transactions-api
- description: Partner-gated Business Banking informational API for tracking the status of payments and transfers within RBC business banking. Onboarding is via an RBC Advisor.
  name: RBC Tracking API
  slug: tracking-api
- description: Partner-gated Business Banking informational API for validating account or payment details prior to initiating a transaction. Onboarding is via an RBC Advisor.
  name: RBC Validation API
  slug: validation-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rbc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rbc.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rbc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rbcroyalbank.com/business/api/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rbc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rbc
- group: company
  title: ''
  type: Blog
  url: https://www.rbc.com/newsroom/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rbc.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rbc.com/privacysecurity/ca/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rbc.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.rbc.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.rbc.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rbc-llms.txt
created: '2026-07-23'
description: 'Royal Bank of Canada (RBC) is Canada''s largest bank by market capitalization and one of the country''s Big Six, a Schedule I domestic bank chartered under the federal Bank Act and publicly traded (TSX/NYSE: RY) with headquarters in Toronto. RBC serves personal, commercial, wealth, capital-markets, and insurance clients in Canada, the U.S., and internationally. It was the first Canadian bank to launch a public API developer portal (developer.rbc.com — the "RBC External Developer Portal"), which offers self-serve informational/utility APIs (branch locator, credit card catalog, mortgage down-payment and amortization calculators) alongside a partner-gated Business Banking API suite for corporate treasury integration (RBC Move Money via Interac e-Transfer, RBC Pay, and Balance/Transactions, Tracking, and Validation APIs). RBC exposes no first-party open-banking consumer-data API; consumer data sharing today is aggregator-based via bilateral agreements (e.g. Plaid, Yodlee). Canada''s
  federal Consumer-Driven Banking framework (Budget 2024 / Fall Economic Statement 2024, overseen by the FCAC) is legislated but not yet operational, so open finance in Canada remains voluntary and fragmented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Royal Bank of Canada
nav: Providers
network: true
overview: 'Royal Bank of Canada publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, Canada, Big Six, and Payments.


  Royal Bank of Canada''s developer surface includes documentation, engineering blog, getting-started guide, signup flow, API reference, and 8 more developer resources.'
random_paper: 65
score:
  band: emerging
  composite: 22.4
  delta: -2.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 83.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.7
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
  name: Rbc Domain Security
  slug: rbc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rbc
tags:
- Financial Services
- Banking
- Canada
- Big Six
- Payments
- Interac
- Open Banking
- Developer Portal
website: https://www.rbc.com/
---
