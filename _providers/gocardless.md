---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Gocardless Agentic Access
  operation_count: 48
  slug: gocardless-agentic-access
  summary_line: 48 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The billing_request_flows API from GoCardless — 2 operation(s) for billing_request_flows.
  name: GoCardless Billing Request Flows API
  slug: gocardless-billing-request-flows-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The billing_requests API from GoCardless — 2 operation(s) for billing_requests.
  name: GoCardless Billing Requests API
  slug: gocardless-billing-requests-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The blocks API from GoCardless — 2 operation(s) for blocks.
  name: GoCardless Blocks API
  slug: gocardless-blocks-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The creditor_bank_accounts API from GoCardless — 1 operation(s) for creditor_bank_accounts.
  name: GoCardless Creditor Bank Accounts API
  slug: gocardless-creditor-bank-accounts-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The creditors API from GoCardless — 2 operation(s) for creditors.
  name: GoCardless Creditors API
  slug: gocardless-creditors-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The customer_bank_accounts API from GoCardless — 2 operation(s) for customer_bank_accounts.
  name: GoCardless Customer Bank Accounts API
  slug: gocardless-customer-bank-accounts-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The customers API from GoCardless — 2 operation(s) for customers.
  name: GoCardless Customers API
  slug: gocardless-customers-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The events API from GoCardless — 2 operation(s) for events.
  name: GoCardless Events API
  slug: gocardless-events-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The instalment_schedules API from GoCardless — 2 operation(s) for instalment_schedules.
  name: GoCardless Instalment Schedules API
  slug: gocardless-instalment-schedules-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The institutions API from GoCardless — 1 operation(s) for institutions.
  name: GoCardless Institutions API
  slug: gocardless-institutions-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The mandates API from GoCardless — 3 operation(s) for mandates.
  name: GoCardless Mandates API
  slug: gocardless-mandates-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The payer_authorisations API from GoCardless — 2 operation(s) for payer_authorisations.
  name: GoCardless Payer Authorisations API
  slug: gocardless-payer-authorisations-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The payments API from GoCardless — 3 operation(s) for payments.
  name: GoCardless Payments API
  slug: gocardless-payments-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The payouts API from GoCardless — 2 operation(s) for payouts.
  name: GoCardless Payouts API
  slug: gocardless-payouts-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The refunds API from GoCardless — 2 operation(s) for refunds.
  name: GoCardless Refunds API
  slug: gocardless-refunds-api
- baseURL: https://api.gocardless.com
  baseurl_source: declared
  description: The subscriptions API from GoCardless — 3 operation(s) for subscriptions.
  name: GoCardless Subscriptions API
  slug: gocardless-subscriptions-api
artifact_total: 46
asyncapis:
- description: AsyncAPI description of the GoCardless webhook surface. GoCardless POSTs a JSON envelope containing one or more events (up to 250 per request) to each subscribed `webhook_endpoint`. Every request incl
  name: GoCardless Webhooks
  slug: gocardless-asyncapi
collections:
- collection_type: open
  name: GoCardless REST billing_request_flows API
  slug: open-gocardless-billing-request-flows-api
- collection_type: open
  name: GoCardless REST billing_request_flows billing_requests API
  slug: open-gocardless-billing-requests-api
- collection_type: open
  name: GoCardless REST billing_request_flows blocks API
  slug: open-gocardless-blocks-api
- collection_type: open
  name: GoCardless REST billing_request_flows creditor_bank_accounts API
  slug: open-gocardless-creditor-bank-accounts-api
- collection_type: open
  name: GoCardless REST billing_request_flows creditors API
  slug: open-gocardless-creditors-api
- collection_type: open
  name: GoCardless REST billing_request_flows customer_bank_accounts API
  slug: open-gocardless-customer-bank-accounts-api
- collection_type: open
  name: GoCardless REST billing_request_flows customers API
  slug: open-gocardless-customers-api
- collection_type: open
  name: GoCardless REST billing_request_flows events API
  slug: open-gocardless-events-api
- collection_type: open
  name: GoCardless REST billing_request_flows instalment_schedules API
  slug: open-gocardless-instalment-schedules-api
- collection_type: open
  name: GoCardless REST billing_request_flows institutions API
  slug: open-gocardless-institutions-api
- collection_type: open
  name: GoCardless REST billing_request_flows mandates API
  slug: open-gocardless-mandates-api
- collection_type: open
  name: GoCardless REST billing_request_flows payer_authorisations API
  slug: open-gocardless-payer-authorisations-api
- collection_type: open
  name: GoCardless REST billing_request_flows payments API
  slug: open-gocardless-payments-api
- collection_type: open
  name: GoCardless REST billing_request_flows payouts API
  slug: open-gocardless-payouts-api
- collection_type: open
  name: GoCardless REST billing_request_flows refunds API
  slug: open-gocardless-refunds-api
- collection_type: open
  name: GoCardless REST billing_request_flows subscriptions API
  slug: open-gocardless-subscriptions-api
- collection_type: open
  name: GoCardless REST API
  slug: open-gocardless
common:
- group: operate
  href: https://artifacts.apis.io/gocardless/rate-limits/gocardless-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gocardless-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gocardless/plans/gocardless-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gocardless-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/gocardless/capabilities/gocardless-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gocardless-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gocardless/agentic-access/gocardless-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gocardless-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/gocardless/security/gocardless-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gocardless-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/gocardless/security/gocardless-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gocardless-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gocardless/authentication/gocardless-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gocardless-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gocardless/security/gocardless-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gocardless-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gocardless/scopes/gocardless-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gocardless-scopes.yml
- group: start
  href: https://artifacts.apis.io/gocardless/sandbox/gocardless-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gocardless-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gocardless/conventions/gocardless-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gocardless-conventions.yml
- group: operate
  href: https://artifacts.apis.io/gocardless/changelog/gocardless-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gocardless-changelog.yml
- group: design
  href: https://artifacts.apis.io/gocardless/components/gocardless-components.yml
  title: ''
  type: Components
  url: components/gocardless-components.yml
- group: design
  href: https://artifacts.apis.io/gocardless/data-model/gocardless-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gocardless-data-model.yml
- group: build
  href: https://artifacts.apis.io/gocardless/errors/gocardless-decline-codes.yml
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
finops:
- has_sources: true
  method: derived
  name: Gocardless Finops
  primary_unit: transaction
  service_category: ''
  slug: gocardless-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gocardless.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.gocardless.com over HTTP.
  name: GoCardless MCP Server
  slug: gocardless
modified: '2026-05-30'
name: GoCardless
nav: Providers
network: true
overview: 'GoCardless publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing Request Flows API, Billing Requests API, Blocks API, and 13 more. Tagged areas include Payments, Direct Debit, Bank Debit, Recurring Payments, and Subscription.


  The GoCardless catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  GoCardless'' developer surface includes authentication, sandbox, changelog, documentation, pricing, signup flow, support, and 18 more developer resources.'
plans:
- name: Gocardless Plans Pricing
  plan_count: 6
  slug: gocardless-plans-pricing
- name: Gocardless Price Estimates
  plan_count: 0
  slug: gocardless-price-estimates
random_paper: 7
rate_limits:
- limit_count: 0
  name: Gocardless Rate Limits
  slug: gocardless-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: GoCardless — asyncapi rules
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
  band: strong
  composite: 54.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.8
    catalog_earned_first_party: 12.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 71.1
    contract_governance: 11.4
    contract_quality: 52.8
    developer_ergonomics: 52.4
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/gocardless/gocardless-2026-06-20T181944.png
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
- Subscription
- SEPA
- Bacs
- ACH
- Open Banking
- Fintech
website: https://gocardless.com
---
