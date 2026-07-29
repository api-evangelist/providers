---
access_model:
  confidence: medium
  label: Partner-gated · Contact sales
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
api_count: 17
apis:
- description: The Enrollments API is typically the first API used in a partner integration and establishes the initial banking relationship for a new end user. It covers account creation, identity capture, KYC (Kno
  name: Green Dot Enrollments API
  slug: enrollments-api
- description: 'Account and user management endpoints for the BaaS platform: retrieve and update account details, manage account status and terms acceptances, manage users on an account, joint accounts, purses (prima'
  name: Green Dot Accounts & Users API
  slug: accounts-users-api
- description: Transaction history and enrichment endpoints for retrieving posted and pending transactions on an account, transaction events, and transaction categorization. Used by partner applications to render ac
  name: Green Dot Transaction History API
  slug: transaction-history-api
- description: Transfers APIs enable customers to move funds to and from internal accounts, purses, and external bank accounts. Includes single- and multi-phase transfers, instant transfer service, auto money moveme
  name: Green Dot Transfers & Money Movement API
  slug: transfers-money-movement-api
- description: 'ACH APIs support ACH transfers into and out of BaaS accounts, including retrieval and filtering of ACH transfers by status and date range, external account linking, and ACH transfer methods. Supports '
  name: Green Dot ACH API
  slug: ach-api
- description: The BillPay API enables bill payment functionality within partner applications, allowing end users to pay billers from their embedded account. Covers payee/biller management, payment scheduling, and p
  name: Green Dot BillPay API
  slug: billpay-api
- description: Payment Instruments APIs manage the cards and tokens tied to an account — issuing and managing payment instruments, custom card options, PCI data access (Full PCI Data Access V2), payment-instrument t
  name: Green Dot Payment Instruments API
  slug: payment-instruments-api
- description: External Card Management APIs let account holders link, list, and remove external debit or credit cards, and support card-funded flows. Used to attach outside cards to a BaaS account for funding and m
  name: Green Dot External Card Management API
  slug: external-card-management-api
- description: The Disbursements API supports paying out funds to recipients — creating recipients, linking payee accounts, executing single-phase transfers with webhook confirmation, and querying maintenance/status
  name: Green Dot Disbursements API
  slug: disbursements-api
- description: Cash Deposits and Payments APIs — Green Dot's retail cash network capability — let end users add cash or make cash payments at retail locations. Covers eCash, barcode generation and lookup, retailer a
  name: Green Dot Cash Deposits & eCash API
  slug: cash-deposits-ecash-api
- description: MRDC (Mobile Remote Deposit Capture) APIs manage mobile check deposits — submitting checks, retrieving MRDC transfers and lists, check images, on-hold transfers, MRDC funding, and paper checks. Includ
  name: Green Dot MRDC (Mobile Check Deposit) API
  slug: mrdc-check-deposit-api
- description: Closed Loop P2P (Peer-to-Peer) APIs move money between two account holders within the same program. Endpoints retrieve individual and listed P2P transfers, track states (accepted, cancelled, rejected,
  name: Green Dot Closed Loop P2P API
  slug: closed-loop-p2p-api
- description: Webhooks provide asynchronous event notifications to partner systems for account updates, transactions, and money-movement events. Documented with webhook samples, transaction webhook samples, and cal
  name: Green Dot Webhooks & Event Notifications
  slug: webhooks-api
- description: Interest Rate APIs add and manage interest rates on primary and savings purses and process accrued-interest calculations for a program, including interest-bearing statement details and INT-1099 tax re
  name: Green Dot Interest Rate & Accrued Interest API
  slug: interest-rate-api
- description: Cashback Rewards APIs manage cashback rewards programs on partner accounts — creating and managing rewards, plus related eGift capability. Lets partners layer loyalty and rewards experiences on top of
  name: Green Dot Cashback Rewards API
  slug: cashback-rewards-api
- description: Customer Care APIs create and manage customer support cases, customize UI for customer support, and enable customers to open support cases directly. Includes dispute automation endpoints so partners c
  name: Green Dot Customer Care API
  slug: customer-care-api
- description: ATM & Retail Locator APIs locate nearby ATMs and Green Dot retail locations for cash deposits, withdrawals, and reload, returning geospatial location and store data. Used to surface the nearest networ
  name: Green Dot ATM & Retail Locators API
  slug: atm-retail-locators-api
artifact_total: 24
asyncapis:
- description: ''
  name: Green Dot Webhooks
  slug: green-dot-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/green-dot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.greendot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.greendot.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.greendot.com/embedded-finance/docs/apis-overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.greendot.com/embedded-finance/reference/getting-started-with-your-api
- group: auth
  title: ''
  type: Authentication
  url: https://developer.greendot.com/embedded-finance/docs/baas-api-authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.greendot.com/embedded-finance/docs/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Green-Dot-Corporation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/green-dot-corporation
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.greendot.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/green-dot-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.greendot.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secure.greendot.com/greendot/account/technology-privacy-statement
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.greendot.com/embedded-finance/changelog
- group: design
  title: ''
  type: Conventions
  url: conventions/green-dot-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/green-dot-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/green-dot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/green-dot-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/green-dot-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/green-dot-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/green-dot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.greendot.com/embedded-finance/docs/release-notes
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/green-dot-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/green-dot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/green-dot-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/green-dot-changelog.yml
created: '2026-04-19'
description: 'Green Dot Corporation (NYSE: GDOT) is a US fintech and bank holding company whose subsidiary Green Dot Bank is a chartered, FDIC-insured member bank. Its Green Dot Arc embedded-finance / Banking-as-a-Service (BaaS) platform lets brands and fintech partners embed banking and payments — account enrollment, KYC/KYB, DDA and prepaid accounts, ACH, transfers, bill pay, card issuing, cash deposits, mobile check deposit, disbursements, and P2P — through a REST API surface. The public developer portal (developer.greendot.com) documents 300+ JSON/OAuth2 endpoints; production access, credentials, and the full Swagger definition are provisioned per-partner after a commercial onboarding.'
finops:
- name: Green Dot Finops
  service_category: Banking-as-a-Service / Embedded Finance
  slug: green-dot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/green-dot.png
layout: provider
modified: '2026-07-23'
name: Green Dot Corporation
nav: Providers
network: true
overview: 'Green Dot Corporation publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Banking as a Service, Embedded Finance, Prepaid Cards, and Banking.


  The Green Dot Corporation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Green Dot Corporation''s developer surface includes documentation, API reference, authentication, engineering blog, changelog, sandbox, and 21 more developer resources.'
plans:
- name: Green Dot Plans Pricing
  plan_count: 1
  slug: green-dot-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Green Dot Rate Limits
  slug: green-dot-rate-limits
scopes:
- name: Green Dot Scopes
  scope_count: 3
  slug: green-dot-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 48.9
  delta: 1.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 45.1
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 57.9
  previous_composite: 47.1
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/green-dot/refs/heads/main/screenshots/green-dot-2026-06-20T182350.png
security:
- kind: authentication
  name: Green Dot Authentication
  slug: green-dot-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Green Dot Domain Security
  slug: green-dot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: green-dot
tags:
- Fintech
- Banking as a Service
- Embedded Finance
- Prepaid Cards
- Banking
- Payments
- Money Movement
- United States
website: https://www.greendot.com
---
