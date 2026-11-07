---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 1
  name: Payments Ai Agentic Access
  operation_count: 102
  slug: payments-ai-agentic-access
  summary_line: 102 operations · 35 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: List, create, and revoke Merchant API keys for your merchant or any sub-merchant in your allowed set.
  name: payments-ai API Keys API
  slug: payments-ai-api-keys-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Buyer checkout API from payments-ai — 16 operation(s) for buyer checkout.
  name: payments-ai Buyer checkout API
  slug: payments-ai-buyer-checkout-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Checkout API from payments-ai — 9 operation(s) for checkout.
  name: payments-ai Checkout API
  slug: payments-ai-checkout-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Customers API from payments-ai — 2 operation(s) for customers.
  name: payments-ai Customers API
  slug: payments-ai-customers-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Invoices API from payments-ai — 3 operation(s) for invoices.
  name: payments-ai Invoices API
  slug: payments-ai-invoices-api
- baseURL: https://www.payments.ai
  baseurl_source: declared
  description: Read-only JSON endpoints under /api/v1
  name: payments-ai JSON API
  slug: payments-ai-json-api
- baseURL: https://www.payments.ai
  baseurl_source: declared
  description: Markdown representations and machine-readable text files
  name: payments-ai Markdown API
  slug: payments-ai-markdown-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: Partner onboarding and merchant team operations — create sub-merchants and assign active members of your team onto merchants you manage.
  name: payments-ai Merchant API
  slug: payments-ai-merchant-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Orders API from payments-ai — 2 operation(s) for orders.
  name: payments-ai Orders API
  slug: payments-ai-orders-api
- baseURL: https://www.payments.ai
  baseurl_source: declared
  description: HTML pages that also serve Markdown via Accept negotiation
  name: payments-ai Pages API
  slug: payments-ai-pages-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Products API from payments-ai — 6 operation(s) for products.
  name: payments-ai Products API
  slug: payments-ai-products-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Public Api API from payments-ai — 9 operation(s) for public api.
  name: payments-ai Public API
  slug: payments-ai-public-api-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Subscriptions API from payments-ai — 2 operation(s) for subscriptions.
  name: payments-ai Subscriptions API
  slug: payments-ai-subscriptions-api
- baseURL: https://sandbox.mor.payments.ai/api
  baseurl_source: declared
  description: The Transactions API from payments-ai — 2 operation(s) for transactions.
  name: payments-ai Transactions API
  slug: payments-ai-transactions-api
artifact_total: 33
common:
- group: auth
  href: https://artifacts.apis.io/payments-ai/well-known/payments-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payments-ai-status-security.txt
- group: agent
  href: https://artifacts.apis.io/payments-ai/agentic-access/payments-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/payments-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/payments-ai/plans/payments-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/payments-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/payments-ai/rules/payments-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/payments-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/payments-ai/json-ld/payments-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/payments-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/payments-ai/vocabulary/payments-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/payments-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/payments-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/payments-ai/data-model/payments-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/payments-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/payments-ai/errors/payments-ai-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/payments-ai-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/payments-ai/errors/payments-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/payments-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/payments-ai/conformance/payments-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/payments-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/payments-ai/llms/payments-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/payments-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/payments-ai/well-known/payments-ai-mor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payments-ai-mor-security.txt
- group: auth
  href: https://artifacts.apis.io/payments-ai/well-known/payments-ai-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/payments-ai-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/payments-ai/well-known/payments-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/payments-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/payments-ai/hosts/payments-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/payments-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/payments-ai/vendors/payments-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/payments-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payments.ai/
- group: auth
  href: https://artifacts.apis.io/payments-ai/authentication/payments-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/payments-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/payments-ai/security/payments-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/payments-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://payments.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.payments.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.payments.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://www.payments.ai/mor/
- group: operate
  title: ''
  type: Support
  url: mailto:support@payments.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paymentsai
- group: operate
  title: ''
  type: Roadmap
  url: https://www.payments.ai/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.payments.ai/mor/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.payments.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payments.ai/mor/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.payments.ai/mor/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/paymentsai/workspace
created: '2026-10-30'
description: Payments AI is the AI-native Merchant of Record and payment orchestration platform. On the Merchant of Record product, the merchant of record is the seller of record and handles sales tax and VAT registration, filing, and remittance for you. On the orchestration product, you stay the merchant of record and we route payments across your gateways.
image: https://www.payments.ai/pai-og.png
json_schemas:
- name: MorPricing
  property_count: 7
  slug: payments-ai-mor-pricing
- name: PageIndex
  property_count: 3
  slug: payments-ai-page-index
- name: PlatformsPricing
  property_count: 7
  slug: payments-ai-platforms-pricing
- name: PublicApiCreateMerchantRequest
  property_count: 6
  slug: payments-ai-public-api-create-merchant-request
- name: PublicApiOrderResponse
  property_count: 14
  slug: payments-ai-public-api-order-response
- name: PublicApiSubscriptionResponse
  property_count: 12
  slug: payments-ai-public-api-subscription-response
- name: PublicCheckoutByInvoiceResponse
  property_count: 23
  slug: payments-ai-public-checkout-by-invoice-response
- name: PublicCheckoutByPlanResponse
  property_count: 23
  slug: payments-ai-public-checkout-by-plan-response
- name: PublicCheckoutOrderResponse
  property_count: 20
  slug: payments-ai-public-checkout-order-response
- name: Site
  property_count: 12
  slug: payments-ai-site
jsonld:
- class_count: 120
  name: Payments Ai Context
  property_count: 191
  slug: payments-ai-context
layout: provider
modified: '2026-10-30'
name: payments-ai
nav: Providers
network: true
overview: 'payments-ai publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Buyer checkout API, Checkout API, and 11 more. Tagged areas include Company, Payments, Artificial Intelligence, Fintech, and Merchant of Record.


  The payments-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  payments-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Payments Ai Plans Pricing
  plan_count: 1
  slug: payments-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Payments Ai Rate Limits
  slug: payments-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: payments-ai API Rules
  rule_count: 59
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 11
  slug: payments-ai-rules
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 39.8
    discoverability: 73.2
    operational_transparency: 23.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/payments-ai/payments-ai-2026-11-03T141026.png
security:
- kind: authentication
  name: Payments Ai Authentication
  slug: payments-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Payments Ai Domain Security
  slug: payments-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: merchant-management
  slug: payments-ai-merchant-management
- name: public-checkout
  slug: payments-ai-public-checkout
slug: payments-ai
tags:
- Company
- Payments
- Artificial Intelligence
- Fintech
- Merchant of Record
- Payment Orchestration
website: https://payments.ai/
---
