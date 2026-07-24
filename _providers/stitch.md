---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Stitch Agentic Access
  operation_count: 2
  slug: stitch-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 10
apis:
- description: Stitch Pay By Bank enables merchants to accept instant bank transfer payments directly from customers' bank accounts in South Africa and Nigeria.
  name: Stitch Pay By Bank
  slug: stitch-pay-by-bank
- description: Stitch integration with Capitec Bank's Capitec Pay payment method, enabling customers to pay via Capitec mobile banking.
  name: Stitch Capitec Pay
  slug: stitch-capitec-pay
- description: Stitch card payment processing enabling businesses to accept debit and credit card payments through the Stitch unified platform.
  name: Stitch Card Payments
  slug: stitch-card-payments
- description: Stitch DebiCheck integration providing authenticated debit orders for recurring payment collection in South Africa.
  name: Stitch DebiCheck
  slug: stitch-debicheck
- description: Stitch Manual EFT (Electronic Funds Transfer) enabling customers to pay via standard bank EFT with Stitch's streamlined reference management.
  name: Stitch Manual EFT
  slug: stitch-manual-eft
- description: Stitch Disbursements (Payouts) API enabling businesses to programmatically send funds to bank accounts, enabling mass payments, refunds, and marketplace disbursements.
  name: Stitch Disbursements
  slug: stitch-disbursements
- description: OAuth 2.0 token operations.
  name: Stitch Authentication API
  slug: stitch-authentication-api
- description: Outbound payment and payout operations.
  name: Stitch Disbursements API
  slug: stitch-disbursements-api
- description: Bank account and transaction data.
  name: Stitch Financial Data API
  slug: stitch-financial-data-api
- description: Payment initiation and management.
  name: Stitch Payments API
  slug: stitch-payments-api
artifact_total: 44
collections:
- collection_type: open
  name: Stitch API
  slug: open-stitch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stitch-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stitch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stitch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stitch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stitchdata
- group: company
  title: ''
  type: Website
  url: https://stitch.money/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stitch.money/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stitch-money
- group: start
  title: ''
  type: Signup
  url: https://stitch.money/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stitch.money/
- group: company
  title: ''
  type: Blog
  url: https://stitch.money/blog
created: '2026-03-27'
description: Stitch is an open banking and payments API platform providing unified access to financial data and payment rails across banks and financial institutions in Africa, primarily South Africa and Nigeria. Stitch enables businesses to accept payments via multiple channels, access bank account data, and issue disbursements through a single GraphQL API.
examples:
- key_count: 6
  name: Stitch Executegraphql Example
  slug: stitch-executegraphql-example
- key_count: 2
  name: Stitch Initiate Payment Example
  slug: stitch-initiate-payment-example
features:
- 'Stitch (Talend / Qlik): hundreds of services across Data Integration'
- 'Detailed pricing: see https://www.stitchdata.com/pricing/'
- 'Service: Stitch Data Loader'
- 'Service: 130+ pre-built sources'
- 'Service: Standard ($100/mo for 5M rows)'
- 'Service: Advanced ($1,250/mo)'
- 'Service: Premium ($2,500/mo)'
- 'Service: Now part of Qlik Data Integration platform'
finops:
- name: Stitch Finops
  service_category: Data Integration
  slug: stitch-finops
graphqls:
- description: The core Stitch API using GraphQL, available at api.stitch.money/graphql. Follows the Relay Server Specification for pagination. Supports all Stitch products including pay-ins, payouts, bank account d
  name: Stitch GraphQL API
  slug: stitch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stitch.png
json_schemas:
- name: Stitch Bank Account
  property_count: 6
  slug: stitch-bank-account
- name: BankAccount
  property_count: 6
  slug: stitch-bankaccount
- name: Disbursement
  property_count: 6
  slug: stitch-disbursement
- name: GraphQLError
  property_count: 2
  slug: stitch-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: stitch-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: stitch-graphqlresponse
- name: MoneyAmount
  property_count: 2
  slug: stitch-moneyamount
- name: Stitch Payment Initiation Request
  property_count: 7
  slug: stitch-payment
- name: PaymentInitiationRequest
  property_count: 5
  slug: stitch-paymentinitiationrequest
- name: TokenResponse
  property_count: 4
  slug: stitch-tokenresponse
json_structures:
- name: Stitch Payment Structure
  property_count: 0
  slug: stitch-payment-structure
- name: Stitch Structure
  property_count: 0
  slug: stitch-structure
jsonld:
- class_count: 20
  name: Stitch Context
  property_count: 0
  slug: stitch-context
layout: provider
modified: '2026-05-19'
name: Stitch
nav: Providers
network: true
overview: 'Stitch publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Disbursements API, Financial Data API, and 1 more. Tagged areas include Africa, Financial Data, Open Banking, Payments, and Unified API.


  The Stitch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stitch''s developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Stitch Plans Pricing
  plan_count: 3
  slug: stitch-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 2
  name: Stitch Rate Limits
  slug: stitch-rate-limits
rules:
- name: Stitch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stitch-jsonschema-spectral-rules
- name: Stitch API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: stitch-rules
score:
  band: developing
  composite: 50.5
  delta: -0.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.0
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 50.6
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stitch/refs/heads/main/screenshots/stitch-2026-06-20T194553.png
security:
- kind: authentication
  name: Stitch Authentication
  slug: stitch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stitch Domain Security
  slug: stitch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Stitch Vulnerability Disclosure
  slug: stitch-vulnerability-disclosure
  summary_line: security.txt
slug: stitch
tags:
- Africa
- Financial Data
- Open Banking
- Payments
- Unified API
- South Africa
- Nigeria
website: https://stitch.money/
---
