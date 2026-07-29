---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Gocardless Agentic Access
  operation_count: 48
  slug: gocardless-agentic-access
  summary_line: 48 operations · 21 acting
api_count: 16
apis:
- description: The billing_request_flows API from GoCardless — 2 operation(s) for billing_request_flows.
  name: GoCardless billing_request_flows API
  slug: gocardless-billing-request-flows-api
- description: The billing_requests API from GoCardless — 2 operation(s) for billing_requests.
  name: GoCardless billing_requests API
  slug: gocardless-billing-requests-api
- description: The blocks API from GoCardless — 2 operation(s) for blocks.
  name: GoCardless blocks API
  slug: gocardless-blocks-api
- description: The creditor_bank_accounts API from GoCardless — 1 operation(s) for creditor_bank_accounts.
  name: GoCardless creditor_bank_accounts API
  slug: gocardless-creditor-bank-accounts-api
- description: The creditors API from GoCardless — 2 operation(s) for creditors.
  name: GoCardless creditors API
  slug: gocardless-creditors-api
- description: The customer_bank_accounts API from GoCardless — 2 operation(s) for customer_bank_accounts.
  name: GoCardless customer_bank_accounts API
  slug: gocardless-customer-bank-accounts-api
- description: The customers API from GoCardless — 2 operation(s) for customers.
  name: GoCardless customers API
  slug: gocardless-customers-api
- description: The events API from GoCardless — 2 operation(s) for events.
  name: GoCardless events API
  slug: gocardless-events-api
- description: The instalment_schedules API from GoCardless — 2 operation(s) for instalment_schedules.
  name: GoCardless instalment_schedules API
  slug: gocardless-instalment-schedules-api
- description: The institutions API from GoCardless — 1 operation(s) for institutions.
  name: GoCardless institutions API
  slug: gocardless-institutions-api
- description: The mandates API from GoCardless — 3 operation(s) for mandates.
  name: GoCardless mandates API
  slug: gocardless-mandates-api
- description: The payer_authorisations API from GoCardless — 2 operation(s) for payer_authorisations.
  name: GoCardless payer_authorisations API
  slug: gocardless-payer-authorisations-api
- description: The payments API from GoCardless — 3 operation(s) for payments.
  name: GoCardless payments API
  slug: gocardless-payments-api
- description: The payouts API from GoCardless — 2 operation(s) for payouts.
  name: GoCardless payouts API
  slug: gocardless-payouts-api
- description: The refunds API from GoCardless — 2 operation(s) for refunds.
  name: GoCardless refunds API
  slug: gocardless-refunds-api
- description: The subscriptions API from GoCardless — 3 operation(s) for subscriptions.
  name: GoCardless subscriptions API
  slug: gocardless-subscriptions-api
artifact_total: 25
asyncapis:
- description: AsyncAPI description of the GoCardless webhook surface. GoCardless POSTs a JSON envelope containing one or more events (up to 250 per request) to each subscribed `webhook_endpoint`. Every request incl
  name: GoCardless Webhooks
  slug: gocardless-asyncapi
collections:
- collection_type: open
  name: GoCardless REST API
  slug: open-gocardless
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gocardless-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gocardless-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gocardless-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gocardless-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gocardless-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gocardless-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gocardless-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gocardless-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gocardless-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/gocardless-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gocardless-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/gocardless-decline-codes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gocardless
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gocardless
- group: company
  title: ''
  type: Website
  url: https://gocardless.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gocardless.com
- group: commercial
  title: ''
  type: Pricing
  url: https://gocardless.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://manage.gocardless.com/signup
- group: operate
  title: ''
  type: Support
  url: https://hub.gocardless.com
- group: operate
  title: ''
  type: StatusPage
  url: https://www.gocardless-status.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.gocardless.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://gocardless.com/blog/
created: '2026-05-11'
description: GoCardless is a global account-to-account payments platform specializing in pull-based bank debit (UK Bacs, SEPA Direct Debit, ACH, BECS, PAD, Autogiro) and open-banking instant bank payments, used by businesses to collect recurring subscriptions, invoices, and one-off payments directly from customer bank accounts. The GoCardless REST API exposes customers, bank accounts, mandates, payments, payouts, subscriptions, refunds, events, webhooks, and verification flows. Authentication uses Bearer access tokens issued from the dashboard, with separate sandbox and live environments; every request must include a GoCardless-Version header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gocardless.png
layout: provider
modified: '2026-05-30'
name: GoCardless
nav: Providers
network: true
overview: 'GoCardless publishes 16 APIs on the [APIs.io](https://apis.io/) network, including billing_request_flows API, billing_requests API, blocks API, and 13 more. Tagged areas include Payments, Direct Debit, Bank Debit, Recurring Payments, and Subscriptions.


  The GoCardless catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  GoCardless'' developer surface includes authentication, sandbox, changelog, documentation, pricing, signup flow, support, and 15 more developer resources.'
random_paper: 23
rules:
- name: GoCardless API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: gocardless-asyncapi-spectral-rules
scopes:
- name: Gocardless Scopes
  scope_count: 1
  slug: gocardless-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 44.4
  delta: -6.1
  facets:
    commercial_clarity: 18.4
    contract_quality: 63.6
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 50.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/gocardless/refs/heads/main/screenshots/gocardless-2026-06-20T181944.png
security:
- kind: authentication
  name: Gocardless Authentication
  slug: gocardless-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gocardless Domain Security
  slug: gocardless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gocardless Vulnerability Disclosure
  slug: gocardless-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gocardless Trust Center
  slug: gocardless-trust-center
  summary_line: ISO/IEC 27001, FCA authorisation, PCI DSS
slug: gocardless
tags:
- Payments
- Direct Debit
- Bank Debit
- Recurring Payments
- Subscriptions
- SEPA
- Bacs
- ACH
- Open Banking
- Fintech
website: https://gocardless.com
---
