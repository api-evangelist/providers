---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Ibanfirst Agentic Access
  operation_count: 38
  slug: ibanfirst-agentic-access
  summary_line: 38 operations · 16 acting
api_count: 2
apis:
- description: First-party hosted remote MCP server, launched with API 1.7.0 on 2026-06-05, exposing 16 read tools over wallets, balances, financial movements, payments, live FX rates, spot trades, fixed forwards an
  name: iBanFirst MCP Connector
  slug: ibanfirst-mcp-connector
- description: PSD2 access-to-account API for registered third-party providers, covering account information services (AIS), payment initiation services (PIS) and strong customer authentication. A sandbox is publish
  name: iBanFirst PSD2 XS2A API
  slug: ibanfirst-psd2-xs2a-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: Each of your accounts has its own specific currency and IBAN. The API allows you to get details and balances about each account in real time. **Note :** ***accounts*** are also labelled as ***wallets*
  name: iBanFirst Accounts API
  slug: ibanfirst-accounts-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: A beneficiary can be either your own account in another bank or a third party recipient account. Beneficiaries can be created or deleted through the API. **Note :** ***beneficiaries*** are also labell
  name: iBanFirst Beneficiaries API
  slug: ibanfirst-beneficiaries-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The API allows you to access your documents stored on the iBanFirst platform through a one-time access link. Documents must be generated on the platform before being available through the API.
  name: iBanFirst Documents API
  slug: ibanfirst-documents-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The API allows you to retrieve all financial movements from your accounts.
  name: iBanFirst Financial movements API
  slug: ibanfirst-financial-movements-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: 'Book a fixed forward payment contracts instantly on iBanFirst without manual intervention. - Available currency pairs: - **EUR/USD** - **EUR/GBP** - **GBP/USD** - Maturities: **up to 6 months**. - Tra'
  name: iBanFirst Fixed forward payment contract API
  slug: ibanfirst-fixed-forward-payment-contract-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The Logs API from iBanFirst — 2 operation(s) for logs.
  name: iBanFirst Logs API
  slug: ibanfirst-logs-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: 'Sending funds from one of your iBanFirst accounts to your own external bank account or a third-party recipient involves two steps: 1. Generate the payment object with the ''Create payment'' method. A un'
  name: iBanFirst Payments API
  slug: ibanfirst-payments-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: The API provides a deliverable FX facility and deliverable FX liquidity. You will become counterparty to iBanFirst and can market and sell deliverable FX services to corporate and private clients as w
  name: iBanFirst Spot trades API
  slug: ibanfirst-spot-trades-api
- baseURL: https://api.ibanfirst.com/api
  baseurl_source: declared
  description: '**1. WHAT IS A WEBHOOK ?** - Webhooks are events based real-time notifications providing updates on transactions and removing the need for periodic polling. - Webhook notifications are sent as HTTPS P'
  name: iBanFirst Webhook subscriptions API
  slug: ibanfirst-webhook-subscriptions-api
artifact_total: 51
asyncapis:
- description: ''
  name: Ibanfirst Webhooks
  slug: ibanfirst-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/agentic-access/ibanfirst-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ibanfirst-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/rules/ibanfirst-rules.yml
  title: ''
  type: Spectral
  url: rules/ibanfirst-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/json-ld/ibanfirst-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ibanfirst-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/vocabulary/ibanfirst-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ibanfirst-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/lifecycle/ibanfirst-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ibanfirst-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/hosts/ibanfirst-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ibanfirst-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/vendors/ibanfirst-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ibanfirst-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ibanfirst.com/newsroom
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/capabilities/ibanfirst-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ibanfirst-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.ibanfirst.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ibanfirst.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ibanfirst.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ibanfirst.com/api/clientapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ibanfirst.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.ibanfirst.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.ibanfirst.com/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iBanFirst
- group: commercial
  title: ''
  type: Pricing
  url: https://ibanfirst.com/fees
- group: start
  title: ''
  type: SignUp
  url: https://info.ibanfirst.com/en/request-an-account
- group: start
  title: ''
  type: Login
  url: https://platform.ibanfirst.com/login?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ibanfirst.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ibanfirst.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/productibf/ibanfirst-rest-api-workspace/collection/d24hl8d/ibanfirst-rest-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ibanfirst.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/changelog/ibanfirst-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ibanfirst-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/llms/ibanfirst-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ibanfirst-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.ibanfirst.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/well-known/ibanfirst-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ibanfirst-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/well-known/ibanfirst-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ibanfirst-security.txt
- group: auth
  title: ''
  type: Security
  url: https://ibanfirst.com/security-policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/security/ibanfirst-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibanfirst-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/security/ibanfirst-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ibanfirst-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/authentication/ibanfirst-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ibanfirst-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/conventions/ibanfirst-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ibanfirst-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/conformance/ibanfirst-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ibanfirst-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://ibanfirst.com/psd2-api
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/errors/ibanfirst-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ibanfirst-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/lifecycle/ibanfirst-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ibanfirst-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/data-model/ibanfirst-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ibanfirst-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/asyncapi/ibanfirst-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ibanfirst-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/sandbox/ibanfirst-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ibanfirst-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/plans/ibanfirst-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ibanfirst-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/rate-limits/ibanfirst-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ibanfirst-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/mcp/ibanfirst-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ibanfirst-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/overlays/ibanfirst-clientapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ibanfirst-clientapi-overlay.yaml
created: '2026-08-17'
description: iBanFirst is a Brussels-headquartered cross-border payment and foreign-exchange platform for businesses, licensed as a payment institution by the National Bank of Belgium (company number 0849.872.824) and operating across Belgium, France, the Netherlands, Germany, Spain, Romania, Bulgaria, Italy, Hungary and the United Kingdom. It provides multi-currency "augmented currency accounts" with dedicated IBANs, SWIFT and SEPA payments with payment tracking, spot FX in 30+ currencies, and fixed forward payment contracts for currency-risk hedging. Its developer surface is a public REST API (iBanFirst API 1.6.0, 38 operations over accounts, financial movements, beneficiaries, payments, spot trades, fixed forwards, documents and webhook subscriptions), X-WSSE token authentication, HMAC-SHA256-signed webhooks for payment and trade events, a separate eIDAS/QWAC-gated PSD2 XS2A API for AIS and PIS third-party providers, and a hosted first-party remote MCP server that gives agents read access
  to treasury data.
image: https://ibanfirst.com/_next/static/media/iban-og-image.1rlnmbejef6_m.jpg
json_schemas:
- name: Amount
  property_count: 2
  slug: ibanfirst-amount
- name: Balance
  property_count: 3
  slug: ibanfirst-balance
- name: CurrencyPair
  property_count: 0
  slug: ibanfirst-currency-pair
- name: Currency
  property_count: 0
  slug: ibanfirst-currency
- name: Date
  property_count: 0
  slug: ibanfirst-date
- name: Datetime
  property_count: 0
  slug: ibanfirst-datetime
- name: Document
  property_count: 7
  slug: ibanfirst-document
- name: events
  property_count: 0
  slug: ibanfirst-events
- name: ExternalBankAccount
  property_count: 8
  slug: ibanfirst-external-bank-account
- name: ExternalBankAccountVOP
  property_count: 9
  slug: ibanfirst-external-bank-account-vop
- name: FinancialMovement
  property_count: 17
  slug: ibanfirst-financial-movement
- name: FixedForwardQuote
  property_count: 6
  slug: ibanfirst-fixed-forward-quote
- name: FixedForwardTrade
  property_count: 11
  slug: ibanfirst-fixed-forward-trade
- name: HolderBank
  property_count: 5
  slug: ibanfirst-holder-bank
- name: Holder
  property_count: 3
  slug: ibanfirst-holder
- name: ID
  property_count: 0
  slug: ibanfirst-id
- name: Log
  property_count: 14
  slug: ibanfirst-log
- name: PaymentOption
  property_count: 1
  slug: ibanfirst-payment-option
- name: Payment
  property_count: 17
  slug: ibanfirst-payment
- name: PaymentVOP
  property_count: 18
  slug: ibanfirst-payment-vop
- name: ProcessResult
  property_count: 1
  slug: ibanfirst-process-result
- name: quoteRef
  property_count: 0
  slug: ibanfirst-quote-ref
- name: Quote
  property_count: 7
  slug: ibanfirst-quote
- name: TradeReconciliation
  property_count: 13
  slug: ibanfirst-trade-reconciliation
- name: Trade
  property_count: 8
  slug: ibanfirst-trade
- name: url
  property_count: 0
  slug: ibanfirst-url
- name: Wallet
  property_count: 8
  slug: ibanfirst-wallet
- name: webhookFailedNotification
  property_count: 6
  slug: ibanfirst-webhook-failed-notification
- name: webhookId
  property_count: 0
  slug: ibanfirst-webhook-id
- name: Webhook
  property_count: 3
  slug: ibanfirst-webhook
jsonld:
- class_count: 29
  name: Ibanfirst Context
  property_count: 104
  slug: ibanfirst-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.ibanfirst.com over HTTP requiring OAuth; 16 tools listed.
  name: iBanFirst MCP
  slug: ibanfirst-mcp
modified: '2026-08-17'
name: iBanFirst
nav: Providers
network: true
overview: 'iBanFirst publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Beneficiaries API, Documents API, and 8 more. Tagged areas include Company, Fintech Insurtech, Cross-Border Payments, Foreign Exchange, and B2B Payments.


  The iBanFirst catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  iBanFirst''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Ibanfirst Plans Pricing
  plan_count: 1
  slug: ibanfirst-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Ibanfirst Rate Limits
  slug: ibanfirst-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: iBanFirst API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 2
  slug: ibanfirst-rules
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.7
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 68.5
    developer_ergonomics: 68.5
    discoverability: 76.7
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 28.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ibanfirst/refs/heads/main/screenshots/ibanfirst-2026-09-02T145820.png
security:
- kind: authentication
  name: Ibanfirst Authentication
  slug: ibanfirst-authentication
  summary_line: apiKey/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Ibanfirst Domain Security
  slug: ibanfirst-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibanfirst Vulnerability Disclosure
  slug: ibanfirst-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ibanfirst
tags:
- Company
- Fintech Insurtech
- Cross-Border Payments
- Foreign Exchange
- B2B Payments
- Treasury
- multi-currency-accounts
- SEPA
- PSD2
- Open Banking
- currency-risk-management
- Webhook
- MCP
- Belgium
- Europe
- SWIFT
website: https://www.ibanfirst.com/
---
