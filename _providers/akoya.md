---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 11
apis:
- description: FDX-aligned REST endpoints returning the list of a consumer's permissioned accounts and detailed account information (account identifiers, type, status, nickname, and product details) for the accounts
  name: Akoya Accounts API
  slug: accounts-api
- description: Returns real-time and available balance information for a consumer's permissioned accounts across the Akoya network. Balances are exposed as FDX-aligned fields and are commonly combined with the Accou
  name: Akoya Balances API
  slug: balances-api
- description: Retrieves transaction history for a consumer's permissioned accounts, returning FDX-aligned transaction records (amount, date, description, categorization, and status). Supports a mode query parameter
  name: Akoya Transactions API
  slug: transactions-api
- description: Provides FDX-aligned investment and brokerage account data for consumer-permissioned accounts, including holdings/positions and tax lots for wealth-management and investing use cases. The taxlots endp
  name: Akoya Investments API
  slug: investments-api
- description: Lists and retrieves account statements for a consumer's consented accounts, returning the set of available statements (period, type, and document reference) so recipients can access official statement
  name: Akoya Statements API
  slug: statements-api
- description: Returns FDX-aligned customer/party information for the consumer who owns the permissioned accounts — name, contact details, and identity attributes — supporting identity verification, account opening,
  name: Akoya Customers API
  slug: customers-api
- description: Provides secure, consumer-permissioned access to ACH and real-time payment (RTP) account credentials — tokenized account and routing identifiers (bankId, identifier, type, identifierType) — so recipie
  name: Akoya Payments API
  slug: payments-api
- description: Retrieves FDX-aligned tax documents for a consumer's permissioned accounts — 1099 form variants (1099-INT, 1099-DIV, 1099-B, and related) and associated tax data — so recipients such as tax-preparatio
  name: Akoya Tax API
  slug: tax-api
- description: Platform/service API for managing consumer consent grants across the Akoya network, letting data recipients look up and manage the consent records that authorize access to a consumer's financial data.
  name: Akoya Consent API
  slug: consent-api
- description: Platform/service API for creating and managing a data recipient's applications on the Akoya network — registering apps, managing client credentials and configuration, and administering the app registr
  name: Akoya Apps Management API
  slug: apps-management-api
- description: Platform/service API for subscribing to and receiving operational notifications about the Akoya network, such as data-provider outages and availability events, delivered via webhook callbacks to regis
  name: Akoya Notifications API
  slug: notifications-api
artifact_total: 18
asyncapis:
- description: ''
  name: Akoya Notifications Webhooks
  slug: akoya-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://akoya.com/
- group: start
  title: ''
  type: Portal
  url: https://akoya.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.akoya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.akoya.com/reference/api-overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akoya-llc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akoyanetwork
- group: operate
  title: ''
  type: Support
  url: https://akoya.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://akoya.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://akoya.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://akoya.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://akoya.com/security
- group: other
  title: ''
  type: FDX Standard
  url: https://financialdataexchange.org/
- group: auth
  title: ''
  type: TrustCenter
  url: security/akoya-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akoya-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/akoya-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akoya-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/akoya-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://akoya.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.akoya.com/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.akoya.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.akoya.com/changelog
- group: start
  title: ''
  type: Login
  url: https://recipient.ddp.akoya.com/login
- group: auth
  title: ''
  type: Authentication
  url: authentication/akoya-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/akoya-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/akoya-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/akoya-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/akoya-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://akoya.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/akoya-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/akoya-notifications-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/akoya-llms.txt
created: '2026-05-08'
description: Akoya operates a tokenized, consumer-permissioned data-access network for US open finance, reaching 4,500+ financial institutions and powering 7,500+ apps and data recipients. It implements the Financial Data Exchange (FDX) API standard to replace screen-scraping with token-permissioned, OAuth 2.0 access to consumer financial data. The Akoya API surface is a 100% API-driven catalog organized into consumer data-access products — Accounts, Balances, Transactions, Investments (holdings and tax lots), Statements, Customers, Tax forms, and Payments (ACH/RTP payment networks) — plus a set of platform/service APIs for Consent, Apps Management, and Notifications. Consumers authenticate at their own financial institution's authorization server; data recipients exchange authorization codes for access tokens and call FDX-aligned REST endpoints. Documentation is published as OpenAPI 3.1.0 (rendered via the docs.akoya.com reference hub); Akoya's GitHub org ships Go code samples for the OAuth
  client-credentials, auth-code, and account-fetch flows. There is no publicly downloadable OpenAPI/Postman artifact — production access requires a network membership agreement.
finops:
- name: Akoya Finops
  service_category: Open Banking
  slug: akoya-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akoya.png
layout: provider
modified: '2026-07-23'
name: Akoya
nav: Providers
network: true
overview: 'Akoya publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Open Banking, Open Finance, Aggregator, and Data Access Network.


  The Akoya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Akoya''s developer surface includes developer portal, documentation, support, pricing, engineering blog, API reference, getting-started guide, and 24 more developer resources.'
plans:
- name: Akoya Plans Pricing
  plan_count: 2
  slug: akoya-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Akoya Rate Limits
  slug: akoya-rate-limits
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 53.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akoya/refs/heads/main/screenshots/akoya-2026-06-20T171457.png
security:
- kind: authentication
  name: Akoya Authentication
  slug: akoya-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Akoya Domain Security
  slug: akoya-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Akoya Trust Center
  slug: akoya-trust-center
  summary_line: SOC 2 Type 2, FIPS 140
slug: akoya
tags:
- Fintech
- Open Banking
- Open Finance
- Aggregator
- Data Access Network
- Tokenized
- Consumer-Permissioned
- FDX
- Account Aggregation
- United States
website: https://akoya.com/
---
