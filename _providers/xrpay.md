---
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Xrpay Agentic Access
  operation_count: 45
  slug: xrpay-agentic-access
  summary_line: 45 operations · 24 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Connected account API from XRPay — 3 operation(s) for connected account.
  name: XRPay Connected account API
  slug: xrpay-connected-account-api
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Payment intents API from XRPay — 5 operation(s) for payment intents.
  name: XRPay Payment intents API
  slug: xrpay-payment-intents-api
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Payouts API from XRPay — 8 operation(s) for payouts.
  name: XRPay Payouts API
  slug: xrpay-payouts-api
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Payroll API from XRPay — 9 operation(s) for payroll.
  name: XRPay Payroll API
  slug: xrpay-payroll-api
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Refunds API from XRPay — 2 operation(s) for refunds.
  name: XRPay Refunds API
  slug: xrpay-refunds-api
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Sandbox API from XRPay — 2 operation(s) for sandbox.
  name: XRPay Sandbox API
  slug: xrpay-sandbox-api
- baseURL: https://api.xrpay.it
  baseurl_source: declared
  description: The Webhooks API from XRPay — 3 operation(s) for webhooks.
  name: XRPay Webhooks API
  slug: xrpay-webhooks-api
artifact_total: 19
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/agentic-access/xrpay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xrpay-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/plans/xrpay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xrpay-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/rules/xrpay-rules.yml
  title: ''
  type: Spectral
  url: rules/xrpay-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/json-ld/xrpay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xrpay-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/vocabulary/xrpay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xrpay-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/data-model/xrpay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xrpay-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/conventions/xrpay-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xrpay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/conventions/xrpay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xrpay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/errors/xrpay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xrpay-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/conformance/xrpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xrpay-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/hosts/xrpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xrpay-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.xrpay.it/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://www.xrpay.it/status
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/authentication/xrpay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xrpay-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/security/xrpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xrpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xrpay.it/
- group: docs
  title: ''
  type: APIReference
  url: https://api.xrpay.it/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.xrpay.it/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.xrpay.it/docs/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.xrpay.it/dashboard/developers/connect
- group: company
  title: ''
  type: Blog
  url: https://www.xrpay.it/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.xrpay.it/changelog
- group: start
  title: ''
  type: Login
  url: https://www.xrpay.it/login
- group: start
  title: ''
  type: SignUp
  url: https://www.xrpay.it/signup?plan=starter
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xrpay.it/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xrpay.it/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xrpay.it/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.xrpay.it/support
created: '2026-10-09'
description: XRPay, built by Xbit Innovations, is a merchant payments platform whose Cashier API lets businesses create payment intents, issue refunds, receive webhooks and connect platform apps (XRPay Connect). The REST API at api.xrpay.it is described by a published OpenAPI 3.1 document and secured with bearer secret keys or Connect access tokens.
json_schemas:
- name: PaymentIntentCreate
  property_count: 19
  slug: xrpay-payment-intent-create
- name: PaymentIntent
  property_count: 31
  slug: xrpay-payment-intent
- name: PayoutQuote
  property_count: 17
  slug: xrpay-payout-quote
- name: Payout
  property_count: 16
  slug: xrpay-payout
- name: PayrollRun
  property_count: 13
  slug: xrpay-payroll-run
- name: WebhookEndpointCreate
  property_count: 3
  slug: xrpay-webhook-endpoint-create
jsonld:
- class_count: 26
  name: Xrpay Context
  property_count: 115
  slug: xrpay-context
layout: provider
modified: '2026-10-09'
name: XRPay
nav: Providers
network: true
overview: 'XRPay publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connected account API, Payment intents API, Payouts API, and 4 more. Tagged areas include Company, Payments, Merchant Payments, Refunds, and Webhook.


  The XRPay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  XRPay''s developer surface includes authentication, API reference, documentation, getting-started guide, engineering blog, changelog, signup flow, and 21 more developer resources.'
plans:
- name: Xrpay Plans Pricing
  plan_count: 3
  slug: xrpay-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: XRPay API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: xrpay-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 72.0
    catalog_earned_first_party: 12.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 84.2
    contract_governance: 19.7
    contract_quality: 60.9
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 31.6
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/xrpay/refs/heads/main/screenshots/xrpay-2026-10-11T194906.png
security:
- kind: authentication
  name: Xrpay Authentication
  slug: xrpay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xrpay Domain Security
  slug: xrpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xrpay
tags:
- Company
- Payments
- Merchant Payments
- Refunds
- Webhook
- Fintech
website: https://www.xrpay.it/
---
