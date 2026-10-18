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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Bond Agentic Access
  operation_count: 71
  slug: bond-agentic-access
  summary_line: 71 operations · 44 acting
api_count: 18
apis:
- description: Create, retrieve, update, and delete individual consumer customer resources for a brand and run Know-Your-Customer (KYC) identity verification against them. Endpoints start and retrieve KYC status, re
  name: Bond Customers & KYC API
  slug: bond-customers-kyc-api
- description: 'Manage commercial customer entities for embedded business banking — create and update businesses, business addresses, and beneficial owners with their addresses, then run Know-Your-Business (KYB) and '
  name: Bond Businesses & KYB API
  slug: bond-businesses-kyb-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: Issue and manage physical, virtual, debit, secured charge, and credit-builder cards. Create cards and card accounts, retrieve and update card details, reissue and activate physical cards, close cards,
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
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: Open and service credit accounts for credit-builder and secured charge card programs — submit credit applications, surface credit-account data to customers, handle instant funding for credit-builder c
  name: Bond Credit API
  slug: bond-credit-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: 'Subscribe to and manage webhook event notifications so applications react in real time to KYC/KYB status changes, card events, transactions, and account activity. Create, retrieve, update, and delete '
  name: Bond Webhooks API
  slug: bond-webhooks-api
- description: 'Sandbox-only endpoints for deterministically testing banking flows before going live — simulate a card transaction authorization, simulate transaction settlement, and force KYC pass or fail outcomes, '
  name: Bond Simulation (Sandbox) API
  slug: bond-simulation-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Accounts API from Bond — 4 operation(s) for accounts.
  name: Bond Accounts API
  slug: bond-accounts-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Beneficial owners address API from Bond — 2 operation(s) for beneficial owners address.
  name: Bond Beneficial owners address API
  slug: bond-beneficial-owners-address-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Beneficial owners API from Bond — 3 operation(s) for beneficial owners.
  name: Bond Beneficial owners API
  slug: bond-beneficial-owners-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Business address API from Bond — 2 operation(s) for business address.
  name: Bond Business address API
  slug: bond-business-address-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Businesses API from Bond — 2 operation(s) for businesses.
  name: Bond Businesses API
  slug: bond-businesses-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Card restrictions API from Bond — 2 operation(s) for card restrictions.
  name: Bond Card restrictions API
  slug: bond-card-restrictions-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Cards API from Bond — 5 operation(s) for cards.
  name: Bond Cards API
  slug: bond-cards-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Credit API from Bond — 4 operation(s) for credit.
  name: Bond Credit API
  slug: bond-credit-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Customers API from Bond — 3 operation(s) for customers.
  name: Bond Customers API
  slug: bond-customers-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The KYB API from Bond — 3 operation(s) for kyb.
  name: Bond KYB API
  slug: bond-kyb-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The KYC API from Bond — 2 operation(s) for kyc.
  name: Bond KYC API
  slug: bond-kyc-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Simulate API from Bond — 4 operation(s) for simulate.
  name: Bond Simulate API
  slug: bond-simulate-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Statements API from Bond — 2 operation(s) for statements.
  name: Bond Statements API
  slug: bond-statements-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Transactions API from Bond — 2 operation(s) for transactions.
  name: Bond Transactions API
  slug: bond-transactions-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Transfer API from Bond — 1 operation(s) for transfer.
  name: Bond Transfer API
  slug: bond-transfer-api
- baseURL: https://api.bond.tech/api/v0.1/
  baseurl_source: declared
  description: The Webhooks API from Bond — 2 operation(s) for webhooks.
  name: Bond Webhooks API
  slug: bond-webhooks-api
artifact_total: 67
asyncapis:
- description: ''
  name: Bond Webhooks
  slug: bond-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/agentic-access/bond-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bond-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/rules/bond-rules.yml
  title: ''
  type: Spectral
  url: rules/bond-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/json-ld/bond-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bond-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/vocabulary/bond-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bond-vocabulary.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bond.tech/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bond.tech/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/errors/bond-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bond-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/llms/bond-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bond-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/hosts/bond-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bond-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/vendors/bond-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bond-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/security/bond-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bond-trust-center.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/security/bond-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bond-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/authentication/bond-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bond-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/changelog/bond-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bond-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/errors/bond-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/bond-error-codes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/errors/bond-ach-return-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/bond-ach-return-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/conventions/bond-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bond-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/lifecycle/bond-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bond-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/sandbox/bond-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bond-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/asyncapi/bond-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bond-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/components/bond-components.yml
  title: ''
  type: Components
  url: components/bond-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/data-model/bond-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bond-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bond/refs/heads/main/conformance/bond-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bond-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://bond.tech/
created: '2026-07-17'
description: Bond Financial Technologies is an enterprise-grade banking-as-a-service (BaaS) and embedded finance platform that lets software companies and fintechs embed financial products directly into their applications through a single REST API. The platform covers consumer and commercial deposit accounts, credit-builder and secured charge cards, debit and virtual card issuing and management, money movement (ACH and account-to-account transfers, external-account linking via Plaid), a transaction ledger, statements, identity verification (KYC, KYB, and beneficial-owner verification powered by Persona), webhook event subscriptions, and a full sandbox with simulation endpoints for authorizations, settlements, and KYC/KYB scenarios. Bond exposes API-key authenticated endpoints under api.bond.tech with pre-integrated bank partnerships. Bond was acquired by FIS in June 2023; its developer documentation remains live at docs.bond.tech. Surfaced originally as a portfolio company of Canaan Partners
  and enriched here from Bond's public developer documentation.
image: https://cdn.prod.website-files.com/5ede8b305ed324245dbaf418/60f9b479c42dd4be9f152c3e_Frame%2018.png
json_schemas:
- name: account
  property_count: 0
  slug: bond-account-docs
- name: account-patch
  property_count: 1
  slug: bond-account-patch
- name: account-write
  property_count: 5
  slug: bond-account-write
- name: Address
  property_count: 8
  slug: bond-address
- name: AdverseActionsGet
  property_count: 6
  slug: bond-adverse-actions-get
- name: all-webhook
  property_count: 9
  slug: bond-all-webhooks
- name: BeneficialOwnerAddressPatchSerializer
  property_count: 8
  slug: bond-beneficial-owner-address-patch-serializer
- name: BeneficialOwnerPostSerializer
  property_count: 5
  slug: bond-beneficial-owner-post-serializer
- name: BusinessesPatchSerializer
  property_count: 11
  slug: bond-businesses-patch-serializer
- name: BusinessesPostSerializer
  property_count: 13
  slug: bond-businesses-post-serializer
- name: card-reissue
  property_count: 2
  slug: bond-card-reissue
- name: card-restriction
  property_count: 6
  slug: bond-card-restriction
- name: card-restriction-write
  property_count: 2
  slug: bond-card-restriction-write
- name: card
  property_count: 13
  slug: bond-card
- name: card-write-patch
  property_count: 1
  slug: bond-card-write-patch
- name: card-write-post
  property_count: 4
  slug: bond-card-write-post
- name: CreditApplicationGetMultiple
  property_count: 2
  slug: bond-credit-application-get-multiple
- name: credit-application-patch
  property_count: 1
  slug: bond-credit-application-patch
- name: credit-application
  property_count: 7
  slug: bond-credit-application
- name: credit-application-write
  property_count: 2
  slug: bond-credit-application-write
- name: customer-patch
  property_count: 9
  slug: bond-customer-patch
- name: Customer
  property_count: 14
  slug: bond-customer
- name: customer-write
  property_count: 11
  slug: bond-customer-write
- name: kyc
  property_count: 2
  slug: bond-kyc
- name: KYCPostPayload
  property_count: 8
  slug: bond-kycpost-payload
- name: PaginatedTransactions
  property_count: 5
  slug: bond-paginated-transactions
- name: settle
  property_count: 2
  slug: bond-settle
- name: simulate
  property_count: 10
  slug: bond-simulate
- name: statement
  property_count: 0
  slug: bond-statement
- name: TransactionSchema
  property_count: 13
  slug: bond-transaction-schema
- name: transfer
  property_count: 0
  slug: bond-transfer
- name: transfer-write
  property_count: 5
  slug: bond-transfer-write
- name: webhook-patch
  property_count: 5
  slug: bond-webhook-patch
- name: webhook-post
  property_count: 5
  slug: bond-webhook-post
- name: webhook
  property_count: 1
  slug: bond-webhook
jsonld:
- class_count: 46
  name: Bond Context
  property_count: 115
  slug: bond-context
layout: provider
modified: '2026-07-23'
name: Bond
nav: Providers
network: true
overview: 'Bond publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cards API, Credit API, Webhooks API, and 22 more. Tagged areas include Company, United States, Banking as a Service, Embedded Finance, and Fintech.


  The Bond catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bond''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 30 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bond API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: bond-rules
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.0
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 70.8
    developer_ergonomics: 57.1
    discoverability: 78.6
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
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
