---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: 'Deposit (formerly Direct Deposit Switching) lets users redirect all or part of their paycheck to a new account. Atomic connects to thousands of payroll providers and employers, signs in on the user''s '
  name: Atomic Deposit API
  slug: atomic-deposit-api
- description: Verify provides instant income and employment verification by connecting to the consumer's payroll provider or employer. Lenders, landlords, and fintechs use it to retrieve verified pay statements, gr
  name: Atomic Verify API
  slug: atomic-verify-api
- description: PayLink lets consumers update their card-on-file across merchants and subscription services. It is also the foundation for subscription discovery, bill management, and Atomic's Manage / Switch product
  name: Atomic PayLink API
  slug: atomic-paylink-api
- description: Tax retrieves W-2s, 1099s, and other tax documents directly from the user's payroll provider, and unlocks tax-refund use cases such as early-deposit and refund-advance products for banks and credit un
  name: Atomic Tax API
  slug: atomic-tax-api
- description: Atomic's authentication layer powers user-permissioned access to third-party payroll, employer, and merchant systems. Three flavors are supported - StandardAuth (credential / 2FA proxy), TrueAuth (dev
  name: Atomic Authentication API
  slug: atomic-authentication-api
- description: Atomic delivers task, company, and continuous-access events to your endpoint using the CloudEvents binary content mode. Events include task-status-updated, task-workflow-finished, payroll-data-fetched
  name: Atomic Webhooks API
  slug: atomic-webhooks-api
- description: The Transact SDK is the user-facing client that drives every Atomic flow — authentication, account selection, consent, and task execution. It ships as an embeddable web component plus native libraries
  name: Atomic Transact SDK
  slug: atomic-transact-sdk
artifact_total: 37
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atomic-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atomic.financial/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atomicfi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atomicfi.com/reference/api
- group: start
  title: ''
  type: Portal
  url: https://console.atomicfi.com/
- group: start
  title: ''
  type: Signup
  url: https://console.atomicfi.com/signup
- group: start
  title: ''
  type: Login
  url: https://console.atomicfi.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atomicfi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atomic-fi/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@atomic.financial
- group: operate
  title: ''
  type: Support
  url: https://atomic.financial/help-center/
- group: company
  title: ''
  type: Blog
  url: https://atomic.financial/insights/
- group: design
  title: ''
  type: Webhooks
  url: https://docs.atomicfi.com/reference/webhooks
- group: auth
  title: ''
  type: Authentication
  url: https://docs.atomicfi.com/reference/api
- group: start
  title: ''
  type: Sandbox
  url: https://docs.atomicfi.com/reference/api
created: '2026-05-25'
description: Atomic is the connected-banking infrastructure for income, payroll, and merchant data. Their user-permissioned APIs let banks, lenders, fintechs, and HR platforms link consumers to thousands of payroll providers, gig platforms, employers, and merchants — and then read or update that data in real time. Core use cases include direct-deposit switching, paycheck-linked income and employment verification, tax-document retrieval, and card-on-file / subscription management. Integration is done through the Transact SDK (web, iOS, Android, React Native, Flutter, Capacitor) plus a REST API at api.atomicfi.com that manages access tokens, tasks, companies, deposit accounts, and webhooks. Atomic is headquartered in Salt Lake City, Utah.
features:
- description: Reroute all or part of a user's paycheck to a new account at thousands of payroll providers, with total, fixed-amount, or percentage allocations.
  name: Deposit (Direct Deposit Switching)
- description: Instant payroll-sourced income and employment verification for lenders, landlords, and fintechs.
  name: Verify (Income & Employment)
- description: User-permissioned card-on-file updating across merchants and subscription services.
  name: PayLink
- description: AI-assisted subscription and recurring-bill management with pause / cancel / reactivate.
  name: Manage
- description: Bulk payment-method updates and card switching across merchants.
  name: Switch
- description: W-2 and 1099 document retrieval direct from payroll providers; powers refund-advance products.
  name: Tax
- description: StandardAuth (credential / 2FA), TrueAuth (deviceless, fully automated), and CoAuth (assisted) auth modes.
  name: Authentication suite
- description: Embeddable web component plus native libraries for iOS, Android, React Native, Flutter, and Capacitor.
  name: Transact SDK
- description: Long-lived linked-account connections that emit webhooks when payroll, deposit accounts, statements, timesheets, or taxes change.
  name: Continuous Access
- description: Task, company, and data-sync events delivered using CloudEvents binary content mode.
  name: CloudEvents webhooks
- description: Web dashboard for API keys, webhook endpoints, secrets, and task monitoring.
  name: Console
graphqls:
- description: Conceptual GraphQL schema for Atomic Financial's payroll connectivity, direct deposit switching, income and employment verification, tax document retrieval, and merchant card-on-file APIs.
  name: Atomic Financial GraphQL
  slug: atomic-financial-graphql
image: https://atomic.financial/wp-content/uploads/2023/02/atomic-logo.svg
integrations:
- description: Strategic partnership for card-switching and subscription management at scale.
  name: Mastercard
- description: Identity and credit-bureau ecosystem integration.
  name: Experian
- description: Open-banking and data-aggregation partnership.
  name: MX
- description: Core-banking distribution to community banks and credit unions.
  name: Jack Henry
- description: Card-issuing platform integration.
  name: Galileo
- description: Consumer-finance platform integration.
  name: MoneyLion
- description: Direct-deposit-switching customer.
  name: Frost Bank
layout: provider
modified: '2026-05-25'
name: Atomic
nav: Providers
network: true
overview: 'Atomic publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Income, Payroll, Direct Deposit, Employment Verification, and Open Banking.


  Atomic''s developer surface includes documentation, API reference, developer portal, signup flow, YouTube channel, support, engineering blog, and 8 more developer resources.'
random_paper: 75
score:
  band: thin
  composite: 28.8
  delta: 5.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 43.2
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 23.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/atomic-financial/refs/heads/main/screenshots/atomic-financial-2026-06-20T172532.png
security:
- kind: domain-security
  name: Atomic Financial Domain Security
  slug: atomic-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: atomic-financial
solutions:
- description: Win primacy through direct-deposit capture, retain through subscription management, and advance through tax refunds.
  name: Banks & Credit Unions
- description: Underwrite with payroll-sourced income, employment, and tax data.
  name: Lenders
- description: Connect to payroll for employment status, pay history, and timesheet data.
  name: HR & Earned-Wage-Access
- description: Subscription discovery, bill optimization, and direct-deposit setup as embedded features.
  name: Fintech & Neobank
tags:
- Income
- Payroll
- Direct Deposit
- Employment Verification
- Open Banking
- Financial
- Subscriptions
- Bill Pay
use_cases:
- description: Banks and credit unions use Deposit to move new account holders' paychecks into their institution.
  name: Primacy / Direct-Deposit Capture
- description: Lenders verify applicant pay and employer identity instantly during underwriting.
  name: Lending Income & Employment Verification
- description: Issuers retrieve W-2 / 1099 data to power early-refund and refund-advance products.
  name: Tax-Refund Advance
- description: Issuers, neobanks, and PFM apps surface and manage recurring subscriptions and bills.
  name: Subscription Discovery & Management
- description: Issuers move card-on-file across merchants when a customer gets a new card.
  name: Card-on-File Switching
- description: Lenders and PFM apps pull gig-platform pay history for underwriting and budgeting.
  name: Gig / 1099 Income Streams
website: https://atomic.financial/
---
