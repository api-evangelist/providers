---
access_model:
  confidence: medium
  label: Partner-gated · Commercial onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - apis
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: The Authorization API issues OAuth2 access tokens for the SVB commercial banking platform (now part of First Citizens). Partners exchange client credentials at /v1/security/oauth/token for a bearer to
  name: SVB Authorization API
  slug: svb-authorization-api
- description: The Account Balance API returns current and available balance information for SVB commercial deposit accounts. Clients query /v1/accounts/balances to retrieve real-time balance positions for cash mana
  name: SVB Account Balance API
  slug: svb-account-balance-api
- description: The Account Transfer API moves funds between a client's own SVB accounts. Partners create transfers at /v1/payment/account-transfers and retrieve transfer status by id, enabling internal book transfer
  name: SVB Account Transfer API
  slug: svb-account-transfer-api
- description: The ACH Transfers API (v2.1) originates domestic ACH credits and debits, verified ACH transfers, and IAT (International ACH Transaction) domestic entries. It exposes /v2/transfer/domestic-achs, /v2/tr
  name: SVB ACH Transfers API
  slug: svb-ach-transfers-api
- description: The Instant Payments API sends and tracks real-time payments over U.S. instant rails. Partners create payments at /v1/payment/instant-payments and retrieve payment status by id for immediate, irrevoca
  name: SVB Instant Payments API
  slug: svb-instant-payments-api
- description: The Wires API (v2.1) initiates and manages domestic and international wire transfers. Partners create wires at /v2/payment/wires, retrieve wire status by id, and cancel pending wires, supporting high-
  name: SVB Wires API
  slug: svb-wires-api
- description: The Stop Payment API places and inspects stop-payment orders on checks drawn against SVB commercial accounts. Partners create stop requests at /v1/payment/stop-checks and retrieve stop status by id to
  name: SVB Stop Payment API
  slug: svb-stop-payment-api
- description: The Virtual Cards API (v2.0) issues and manages virtual card numbers (VCN) for accounts-payable, procurement, and travel spend. It exposes /v2/card/virtualcards plus authorizations, clearings, real-ca
  name: SVB Virtual Cards API
  slug: svb-virtual-cards-api
- description: The Webhook API (v2.0) delivers asynchronous event notifications for payment and account activity. Partners manage event-types, events, publishers, and subscriptions under /v2/event/*, creating subscr
  name: SVB Webhook API
  slug: svb-webhook-api
- description: The Reference API provides look-up and reachability data supporting the payment products. It exposes /v1/reference/reachability/instant-payments/{creditor_agent_id} so partners can verify whether a re
  name: SVB Reference API
  slug: svb-reference-api
artifact_total: 14
asyncapis:
- description: ''
  name: First Citizens Bancshares Webhooks
  slug: first-citizens-bancshares-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/first-citizens-bancshares-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://firstcitizensbank.responsibledisclosure.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-citizens-bancshares-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-citizens-bancshares-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/first-citizens-bancshares-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/first-citizens-bancshares-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.svb.com/apis/commercial-banking-apis/ach-transfers/2.1/ach-transfers-v2-migration-guide
- group: start
  title: ''
  type: Sandbox
  url: sandbox/first-citizens-bancshares-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/first-citizens-bancshares-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-citizens-bancshares-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-citizens-bancshares-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/first-citizens-bancshares-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-citizens-bancshares-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.firstcitizens.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.svb.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.svb.com/apis/docs-home
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/svb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-citizens-bank
- group: operate
  title: ''
  type: Support
  url: https://developer.svb.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstcitizens.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstcitizens.com/privacy
created: '2025-03-01'
description: First Citizens BancShares is a super-regional financial holding company (parent of First-Citizens Bank & Trust) providing general banking, trust, investment, insurance, and asset-management services to individuals, businesses, and professionals. Its programmable surface runs through Silicon Valley Bank (SVB) — acquired in 2023 and now a division of First Citizens — whose Apigee-backed developer portal at developer.svb.com publishes a family of commercial banking REST APIs covering authorization, account balance, transfers, ACH, instant payments, wires, stop payment, virtual cards, webhooks, and reference/reachability. Access is partner-gated (commercial onboarding); consumer account data is reachable via the Plaid aggregator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-citizens-bancshares.png
layout: provider
modified: '2026-07-23'
name: First Citizens BancShares
nav: Providers
network: true
overview: 'First Citizens BancShares publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial Services, Commercial Banking, Payments, and ACH.


  The First Citizens BancShares catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  First Citizens BancShares'' developer surface includes authentication, sandbox, documentation, support, and 17 more developer resources.'
random_paper: 54
score:
  band: thin
  composite: 38.8
  delta: 1.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 39.1
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 31.6
  previous_composite: 37.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-citizens-bancshares/refs/heads/main/screenshots/first-citizens-bancshares-2026-06-20T181238.png
security:
- kind: authentication
  name: First Citizens Bancshares Authentication
  slug: first-citizens-bancshares-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: First Citizens Bancshares Domain Security
  slug: first-citizens-bancshares-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: First Citizens Bancshares Vulnerability Disclosure
  slug: first-citizens-bancshares-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: first-citizens-bancshares
tags:
- Banking
- Financial Services
- Commercial Banking
- Payments
- ACH
- Wire Transfers
- Virtual Cards
- Open Banking
- Trust
- Investment
- Insurance
- United States
- Super Regional
website: https://www.firstcitizens.com
---
