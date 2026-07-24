---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 8
apis:
- description: Details and summary information for member accounts, including name, status, activity dates, balances, and more. Part of Navy Federal's consumer- permissioned Open Banking API Catalog; access is gated
  name: Account Details API
  slug: account-details
- description: Information on account ownership and member relationships for consented member accounts. Part of Navy Federal's consumer-permissioned Open Banking API Catalog.
  name: Account Holders API
  slug: account-holders
- description: Statements for accounts over a given period, including statement names and images with details. Part of Navy Federal's consumer-permissioned Open Banking API Catalog.
  name: Account Statements API
  slug: account-statements
- description: Transactions for accounts over a given period, including amounts, description, running balance, status, and more. Part of Navy Federal's consumer-permissioned Open Banking API Catalog.
  name: Account Transactions API
  slug: account-transactions
- description: Client registration and OAuth authentication management used to onboard third parties and obtain member consent tokens for the Open Banking API Catalog.
  name: API Management API
  slug: api-management
- description: Listing of consented member accounts with basic details. Part of Navy Federal's consumer-permissioned Open Banking API Catalog.
  name: Customer Accounts API
  slug: customer-accounts
- description: Member information independent of accounts, including name, address, date of birth, IDs, and other personal information. Part of Navy Federal's consumer-permissioned Open Banking API Catalog.
  name: Customer Details API
  slug: customer-details
- description: Connection test to the API platform providing a basic message response, used to prove out a working request over mTLS with whitelisting. Part of Navy Federal's Open Banking API Catalog.
  name: Gateway Connectivity API
  slug: gateway-connectivity
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/navy-federal-credit-union-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navy-federal-credit-union-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.navyfederal.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.navyfederal.org/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.navyfederal.org/document-library.html
- group: start
  title: ''
  type: SignUp
  url: https://developer.navyfederal.org/register.html
- group: operate
  title: ''
  type: Support
  url: https://developer.navyfederal.org/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.navyfederal.org/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.navyfederal.org/policy/privacy.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.navyfederal.org/open-banking-api-catalog.html
- group: operate
  title: ''
  type: Support
  url: https://developer.navyfederal.org/support/faqs.html
- group: start
  title: ''
  type: Login
  url: https://developer.navyfederal.org/login.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navy-federal-credit-union
- group: company
  title: ''
  type: Blog
  url: https://www.navyfederal.org/makingcents.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/navy-federal-credit-union-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/navy-federal-credit-union-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/navy-federal-credit-union-security.txt
- group: auth
  title: ''
  type: Security
  url: https://navyfederal.responsibledisclosure.com/hc/en-us
- group: auth
  title: ''
  type: Authentication
  url: authentication/navy-federal-credit-union-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/navy-federal-credit-union-conformance.yml
created: '2026-07-23'
description: Navy Federal Credit Union is a federally chartered credit union headquartered in Vienna, Virginia, and the largest credit union in the world by both assets and membership, serving more than 14 million members across the armed forces, Department of Defense, veterans, and their families. As a not-for-profit, member-owned financial cooperative regulated by the National Credit Union Administration (NCUA), it offers deposit accounts, credit cards, auto and mortgage lending, and investment services. On the open-finance front, Navy Federal operates a genuine first-party developer program — the Navy Federal API Exchange at developer.navyfederal.org — that publishes a consumer- permissioned, open-banking-style API catalog of eight data-access products (account details, holders, statements, transactions, customer accounts, customer details, plus OAuth/API-management and an mTLS gateway-connectivity test). Access is partner-gated behind registration and a signed Data Access Agreement,
  secured with OAuth member consent and mutual-TLS whitelisting; no OpenAPI/Swagger is publicly downloadable pre-login. Navy Federal also exposes member-permissioned data through aggregators (Plaid, Envestnet | Yodlee via a 2021 data access agreement, Flinks) rather than solely direct first-party integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Navy Federal Credit Union
nav: Providers
network: true
overview: 'Navy Federal Credit Union publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Banking, United States, Credit Union, and Open Finance.


  Navy Federal Credit Union''s developer surface includes documentation, signup flow, support, API reference, engineering blog, authentication, and 14 more developer resources.'
random_paper: 44
score:
  band: thin
  composite: 31.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 10.5
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.4
  schema_version: 0.5
  scored_at: '2026-07-23'
security:
- kind: authentication
  name: Navy Federal Credit Union Authentication
  slug: navy-federal-credit-union-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Navy Federal Credit Union Domain Security
  slug: navy-federal-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Navy Federal Credit Union Vulnerability Disclosure
  slug: navy-federal-credit-union-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: navy-federal-credit-union
tags:
- Financial Services
- Banking
- United States
- Credit Union
- Open Finance
- Open Banking
- Data Aggregation
- Payments
website: https://www.navyfederal.org/
---
