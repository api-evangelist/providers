---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 88
  human_in_the_loop: 1
  name: Monoova Agentic Access
  operation_count: 150
  slug: monoova-agentic-access
  summary_line: 150 operations · 88 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: '<h3> Overview </h3> <p> Having customers paying you by bank transfer might be easy for your customers but contains a reconciliation risk for you. If your customer mistypes or forgets the reference to '
  name: Monoova Automatcher (Bank Account Receivables) API
  slug: monoova-automatcher-bank-account-receivables-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> The BPAY APIs do not perform any financial transactions and are used to validate BPAY information that is used in the <a href="/payments#operation/TransactionExecute"> /financial/v
  name: Monoova BPAY API
  slug: monoova-bpay-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Create Payment Using Token API from Monoova — 1 operation(s) for create payment using token.
  name: Monoova Create Payment Using Token API
  slug: monoova-create-payment-using-token-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> <p> The Financial APIs enable you to process credits and debits, including transferring funds within Monoova to a Ledger Account, an mWallet (for BPAY transactions), or an mAccount
  name: Monoova Financial API
  slug: monoova-financial-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Generate a Bearer Token API from Monoova — 1 operation(s) for generate a bearer token.
  name: Monoova Generate a Bearer Token API
  slug: monoova-generate-a-bearer-token-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Generate a Client Session API from Monoova — 1 operation(s) for generate a client session.
  name: Monoova Generate a Client Session API
  slug: monoova-generate-a-client-session-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Get Async Request Status API from Monoova — 1 operation(s) for get async request status.
  name: Monoova Get Async Request Status API
  slug: monoova-get-async-request-status-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Get Payment Method Token Details API from Monoova — 1 operation(s) for get payment method token details.
  name: Monoova Get Payment Method Token Details API
  slug: monoova-get-payment-method-token-details-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Get Transaction By Date Range API from Monoova — 1 operation(s) for get transaction by date range.
  name: Monoova Get Transaction By Date Range API
  slug: monoova-get-transaction-by-date-range-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Get Transaction By Id API from Monoova — 1 operation(s) for get transaction by id.
  name: Monoova Get Transaction By Id API
  slug: monoova-get-transaction-by-id-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: Once a payment agreement is created you can trigger payments against it
  name: Monoova Initiate a Payment API
  slug: monoova-initiate-a-payment-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: Monoova allows virtual ledgers to be created and linked to an Automatcher account number and optional PayID that can be used to track funds received and paid. Moving funds in and out of ledgers is acc
  name: Monoova Ledger Account API
  slug: monoova-ledger-account-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> The mAccount is the name we have given our virtual account. It is at the centre of anything you do with our Payments Engine. In many ways, your mAccount(s) is you in the Engine, th
  name: Monoova M Account API
  slug: monoova-maccount-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: Methods to handle the payment agreement lifecycle. There are 2 ways in which a payment agreement can be amended – unilaterally (no payer approval needed), and Bilaterally (payer approval required)
  name: Monoova Manage Payment Agreements API
  slug: monoova-manage-payment-agreements-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> mWallet is the name we have given to the digital wallet required for our BPAY payments. For any other digital-wallet uses, we recommend our mAccount. The APIs in this section do no
  name: Monoova M Wallet API
  slug: monoova-mwallet-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Notification Management API from Monoova — 4 operation(s) for notification management.
  name: Monoova Notification Management API
  slug: monoova-notification-management-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> <p> A PayID is an alias for a bank account number that makes paying into account easier. A PayID can be an email address, phone number or ABN. PayIDs are issued and associated with
  name: Monoova Pay ID API
  slug: monoova-payid-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The `AsyncResponse` is used in operations where the request is accepted, but the processing is not immediate. This response format provides information for tracking and checking the request status. Th
  name: Monoova PayTo Async API
  slug: monoova-payto-async-api-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Public Endpoints API from Monoova — 3 operation(s) for public endpoints.
  name: Monoova Public Endpoints API
  slug: monoova-public-endpoints-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> <p> This feature enables customers to specify the criteria for accepting incoming NPP and DE payments in real time. The customer will be able to advise Monoova about the exact amou
  name: Monoova Reconciliation Rules API
  slug: monoova-reconciliation-rules-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: </br><h2>PayTo Reporting</h2> <p> A new report has been added specifically for NPP payments related to PayTo. Monoova’s PayTo NPP receivables – available <a href='https://api-docs.monoova.com/payments
  name: Monoova Reporting API
  slug: monoova-reporting-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> The APIs in the reports/v1 section help you keep track of balances and transactions. Payments automation is only helping you relax if you know where exactly your money is at any on
  name: Monoova Reports API
  slug: monoova-reports-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Request Refund Transaction API from Monoova — 1 operation(s) for request refund transaction.
  name: Monoova Request Refund Transaction API
  slug: monoova-request-refund-transaction-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> <p> The security/v1 APIs allows you to manage security tokens. This gives you an alternative to using signIn API KEY for BASIC authentication for each API call. Security tokens com
  name: Monoova Security API
  slug: monoova-security-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The endpoints in this section allow subscription and management of webhooks for the purpose of receiving transaction notifications.</br>
  name: Monoova Subscriptions API
  slug: monoova-subscriptions-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> <p> Using tokens is a way of increasing the security around sensitive information. A token can be used to obfuscate debit and credit details. The details of a token (its payload) a
  name: Monoova Token API
  slug: monoova-token-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> The APIs in the tools/v1/ section represent utilities that you may find useful while consuming the other APIs offered as part of the Engine other APIs.
  name: Monoova Tools API
  slug: monoova-tools-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: The Update Payment Method Token Status API from Monoova — 1 operation(s) for update payment method token status.
  name: Monoova Update Payment Method Token Status API
  slug: monoova-update-payment-method-token-status-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3>Overview</h3> <h3>Bank Account Ownership Verification</h3> <p>The purpose of this API is to verify access to a bank account or PayID details, which has several compliance and risk-mitigation appli
  name: Monoova Verify API
  slug: monoova-verify-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <p> In addition to callable reporting endpoints, webhooks will also be available for state changes for payment agreements and funds received. </p> </br></br>
  name: Monoova Webhooks API
  slug: monoova-webhooks-api
- baseURL: https://api.mpay.com.au
  baseurl_source: declared
  description: <h3> Overview </h3> <p> This feature enables whitelisting of bank accounts when receiving funds in automatcher accounts. Funds received from a non-whitelisted account will be automatically returned. U
  name: Monoova Whitelisting for Automatcher (Bank Account Receivables) API
  slug: monoova-whitelisting-for-automatcher-bank-account-receivables-api
artifact_total: 39
asyncapis:
- description: ''
  name: Monoova Webhooks
  slug: monoova-webhooks
collections:
- collection_type: open
  name: Monoova Card Payments API
  slug: open-monoova-cc
- collection_type: open
  name: Monoova Payments API
  slug: open-monoova-payments
- collection_type: open
  name: Monoova PayTo API
  slug: open-monoova-payto
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/monoova-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/monoova-cc-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monoova-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monoova-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monoova-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monoova-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.monoova.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.monoova.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.monoova.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.monoova.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.monoova.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.monoova.com/authentication
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/monoova/monoova-api
- group: operate
  title: ''
  type: StatusPage
  url: https://monoova.statuspage.io
- group: company
  title: ''
  type: Blog
  url: https://www.monoova.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monoova
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monoova
- group: start
  title: ''
  type: SignUp
  url: https://sandbox.monoova.com/
- group: operate
  title: ''
  type: Support
  url: https://www.monoova.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monoova.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monoova.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.monoova.com/security
- group: build
  title: ''
  type: Packages
  url: packages/monoova-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/monoova-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monoova-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monoova-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/monoova-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/monoova-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monoova-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/monoova-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.monoova.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monoova-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/monoova-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/monoova-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/monoova-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/monoova-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/monoova-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monoova-well-known.yml
created: '2026-07-24'
description: 'Monoova is an Australian payments platform that lets businesses receive, manage, and pay funds in AUD across every domestic rail through a single set of RESTful JSON APIs. Operated by Monoova Global Payments Pty Ltd (AFSL 421414) and enrolled with AUSTRAC, it connects directly to the New Payments Platform (real-time account-to-account transfers via NPP/Osko, PayID addressing, and PayTo mandated debits) alongside BPAY, direct entry (credit/debit), card acquiring, and Apple Pay / Google Pay. Its Automatcher reconciliation engine, virtual mAccount/mWallet hierarchies, Confirmation of Payee, account verification, payment tokenisation, and webhook-driven reporting target fintechs, marketplaces, payroll, lending, remittance, and SaaS businesses (customers include Wise, Nium, Finder, and Sharesies). Monoova is genuinely API-first: it ships a public developer portal, a Redoc API reference, downloadable OpenAPI specifications, and a public Postman workspace, plus a free self-serve sandbox.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Monoova
nav: Providers
network: true
overview: 'Monoova publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Automatcher (Bank Account Receivables) API, BPAY API, Create Payment Using Token API, and 28 more. Tagged areas include Payments, Australia, Real-Time Payments, NPP, and PayTo.


  The Monoova catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Monoova''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 32 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 65.6
    developer_ergonomics: 68.5
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monoova/refs/heads/main/screenshots/monoova-2026-08-07T184216.png
security:
- kind: authentication
  name: Monoova Authentication
  slug: monoova-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Monoova Domain Security
  slug: monoova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Monoova Trust Center
  slug: monoova-trust-center
  summary_line: SOC 2, PCI DSS
slug: monoova
tags:
- Payments
- Australia
- Real-Time Payments
- NPP
- PayTo
- PayID
- Account-to-Account
- BPAY
- Card Payments
- Money Movement
- Virtual Accounts
- Cross-Border
website: https://www.monoova.com/
---
