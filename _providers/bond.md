---
access_model:
  confidence: medium
  label: Sales-led · Sandbox available
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - documentation
  trial: true
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-01'
api_count: 9
apis:
- description: Create, retrieve, update, and delete individual consumer customer resources for a brand and run Know-Your-Customer (KYC) identity verification against them. Endpoints start and retrieve KYC status, re
  name: Bond Customers & KYC API
  slug: bond-customers-kyc-api
- description: 'Manage commercial customer entities for embedded business banking — create and update businesses, business addresses, and beneficial owners with their addresses, then run Know-Your-Business (KYB) and '
  name: Bond Businesses & KYB API
  slug: bond-businesses-kyb-api
- description: Issue and manage physical, virtual, debit, secured charge, and credit-builder cards. Create cards and card accounts, retrieve and update card details, reissue and activate physical cards, close cards,
  name: Bond Cards API
  slug: bond-cards-api
- description: 'Open and manage consumer and commercial deposit accounts, credit accounts, and security-deposit accounts, with documented account types, account states, and account lifecycle management. Generate and '
  name: Bond Accounts & Statements API
  slug: bond-accounts-statements-api
- description: Move money between accounts with ACH transfers and account-to-account fund transfers, and link and manage external bank accounts using Plaid before initiating transfers. Documents the ACH transfer mod
  name: Bond Transfers API
  slug: bond-transfers-api
- description: 'Retrieve all transactions available to a brand with pagination and optional filtering, and fetch details for a single transaction by id. Documents the transaction lifecycle and states, payment types, '
  name: Bond Ledger (Transactions) API
  slug: bond-ledger-transactions-api
- description: Open and service credit accounts for credit-builder and secured charge card programs — submit credit applications, surface credit-account data to customers, handle instant funding for credit-builder c
  name: Bond Credit API
  slug: bond-credit-api
- description: 'Subscribe to and manage webhook event notifications so applications react in real time to KYC/KYB status changes, card events, transactions, and account activity. Create, retrieve, update, and delete '
  name: Bond Webhooks API
  slug: bond-webhooks-api
- description: 'Sandbox-only endpoints for deterministically testing banking flows before going live — simulate a card transaction authorization, simulate transaction settlement, and force KYC pass or fail outcomes, '
  name: Bond Simulation (Sandbox) API
  slug: bond-simulation-api
artifact_total: 13
asyncapis:
- description: ''
  name: Bond Webhooks
  slug: bond-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/bond-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bond.tech/security
- group: company
  title: ''
  type: Website
  url: https://www.bond.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.bond.tech
- group: start
  title: ''
  type: Login
  url: https://portal.bond.tech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bond.tech/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bond.tech/reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bond.tech/docs/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bond-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bondfintech
- group: company
  title: ''
  type: Blog
  url: https://www.bond.tech/blog
- group: operate
  title: ''
  type: Support
  url: https://www.bond.tech/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bond.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bond.tech/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/bond-technologies/workspace/bond-api
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.bond.tech/llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bond-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bond-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bond-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bond-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/bond-ach-return-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bond-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bond-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bond-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bond-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/bond-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bond-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bond-conformance.yml
created: '2026-07-17'
description: Bond Financial Technologies is an enterprise-grade banking-as-a-service (BaaS) and embedded finance platform that lets software companies and fintechs embed financial products directly into their applications through a single REST API. The platform covers consumer and commercial deposit accounts, credit-builder and secured charge cards, debit and virtual card issuing and management, money movement (ACH and account-to-account transfers, external-account linking via Plaid), a transaction ledger, statements, identity verification (KYC, KYB, and beneficial-owner verification powered by Persona), webhook event subscriptions, and a full sandbox with simulation endpoints for authorizations, settlements, and KYC/KYB scenarios. Bond exposes API-key authenticated endpoints under api.bond.tech with pre-integrated bank partnerships. Bond was acquired by FIS in June 2023; its developer documentation remains live at docs.bond.tech. Surfaced originally as a portfolio company of Canaan Partners
  and enriched here from Bond's public developer documentation.
image: https://cdn.prod.website-files.com/5ede8b305ed324245dbaf418/60f9b479c42dd4be9f152c3e_Frame%2018.png
layout: provider
modified: '2026-07-23'
name: Bond
nav: Providers
network: true
overview: 'Bond publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, United States, Banking as a Service, Embedded Finance, and Fintech.


  The Bond catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bond''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 21 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 61.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 50.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/screenshots/bond-2026-07-25T203549.png
security:
- kind: authentication
  name: Bond Authentication
  slug: bond-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bond Domain Security
  slug: bond-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Bond Trust Center
  slug: bond-trust-center
  summary_line: SOC 2, PCI DSS
slug: bond
tags:
- Company
- United States
- Banking as a Service
- Embedded Finance
- Fintech
- Payments
- Card Issuing
- Deposit Accounts
- Money Movement
- ACH
- KYC
- KYB
- Credit
- Open Finance
website: https://www.bond.tech
---
