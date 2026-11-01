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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 27
  human_in_the_loop: 2
  name: Forage Agentic Access
  operation_count: 43
  slug: forage-agentic-access
  summary_line: 43 operations · 27 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: REST API to tokenize EBT cards, run PIN-secured balance inquiries, and create, capture, void, and refund EBT SNAP, EBT Cash, and HSA/FSA payments and orders for online and in-store checkout.
  name: Forage EBT SNAP Payments API
  slug: forage-ebt-snap-payments-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Bearer Tokens API from Forage — 4 operation(s) for bearer tokens.
  name: Forage Bearer Tokens API
  slug: forage-bearer-tokens-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Card Details API from Forage — 1 operation(s) for card details.
  name: Forage Card Details API
  slug: forage-card-details-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Custom Sessions API from Forage — 3 operation(s) for custom sessions.
  name: Forage Custom Sessions API
  slug: forage-custom-sessions-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Deferred Capture API from Forage — 1 operation(s) for deferred capture.
  name: Forage Deferred Capture API
  slug: forage-deferred-capture-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Fully Hosted Sessions API from Forage — 1 operation(s) for fully hosted sessions.
  name: Forage Fully Hosted Sessions API
  slug: forage-fully-hosted-sessions-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Order Payments API from Forage — 3 operation(s) for order payments.
  name: Forage Order Payments API
  slug: forage-order-payments-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Order Refunds API from Forage — 4 operation(s) for order refunds.
  name: Forage Order Refunds API
  slug: forage-order-refunds-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Orders API from Forage — 2 operation(s) for orders.
  name: Forage Orders API
  slug: forage-orders-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Payment Methods API from Forage — 2 operation(s) for payment methods.
  name: Forage Payment Methods API
  slug: forage-payment-methods-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Payment Refunds API from Forage — 3 operation(s) for payment refunds.
  name: Forage Payment Refunds API
  slug: forage-payment-refunds-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Reports API from Forage — 4 operation(s) for reports.
  name: Forage Reports API
  slug: forage-reports-api
- baseURL: https://api.joinforage.app
  baseurl_source: declared
  description: The Sandbox Testing API from Forage — 2 operation(s) for sandbox testing.
  name: Forage Sandbox Testing API
  slug: forage-sandbox-testing-api
artifact_total: 33
asyncapis:
- description: ''
  name: Forage Webhooks
  slug: forage-webhooks
common:
- group: other
  href: https://artifacts.apis.io/forage/capabilities/forage-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/forage-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/forage/plans/forage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/forage-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/forage/agentic-access/forage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/forage-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/forage/rules/forage-rules.yml
  title: ''
  type: Spectral
  url: rules/forage-rules.yml
- group: design
  href: https://artifacts.apis.io/forage/json-ld/forage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/forage-context.jsonld
- group: design
  href: https://artifacts.apis.io/forage/vocabulary/forage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/forage-vocabulary.yml
- group: start
  href: https://artifacts.apis.io/forage/sandbox/forage-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/forage-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/forage/mcp/forage-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/forage-mcp.yml
- group: other
  href: https://artifacts.apis.io/forage/hosts/forage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/forage-hosts.yml
- group: other
  href: https://artifacts.apis.io/forage/vendors/forage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/forage-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.joinforage.com/app/support/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.joinforage.com/newsroom
- group: auth
  href: https://artifacts.apis.io/forage/scopes/forage-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/forage-scopes.yml
- group: auth
  href: https://artifacts.apis.io/forage/security/forage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinforage.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.joinforage.app/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinforage.app/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinforage.app/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinforage.app/docs/setup
- group: operate
  title: ''
  type: Support
  url: https://www.joinforage.com/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://www.joinforage.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teamforage
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joinforage.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.joinforage.com/get-in-touch
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinforage.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinforage.com/pages/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinforage.app
- group: operate
  href: https://artifacts.apis.io/forage/changelog/forage-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/forage-changelog.yml
- group: operate
  href: https://artifacts.apis.io/forage/lifecycle/forage-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/forage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/forage/lifecycle/forage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/forage-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/forage/authentication/forage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/forage-authentication.yml
- group: design
  href: https://artifacts.apis.io/forage/conventions/forage-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/forage-conventions.yml
- group: design
  href: https://artifacts.apis.io/forage/conventions/forage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/forage-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.joinforage.app/reference/request-limits
- group: agent
  href: https://artifacts.apis.io/forage/mcp/forage-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/forage-mcp.yml
- group: agent
  href: https://artifacts.apis.io/forage/llms/forage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/forage-llms.txt
- group: build
  href: https://artifacts.apis.io/forage/packages/forage-packages.yml
  title: ''
  type: Packages
  url: packages/forage-packages.yml
- group: build
  href: https://artifacts.apis.io/forage/packages/forage-packages.yml
  title: ''
  type: SDKs
  url: packages/forage-packages.yml
- group: design
  href: https://artifacts.apis.io/forage/components/forage-components.yml
  title: ''
  type: Components
  url: components/forage-components.yml
- group: design
  href: https://artifacts.apis.io/forage/asyncapi/forage-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/forage-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/forage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/forage/errors/forage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/forage-problem-types.yml
- group: build
  href: https://artifacts.apis.io/forage/errors/forage-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/forage-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/forage/data-model/forage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/forage-data-model.yml
- group: design
  href: https://artifacts.apis.io/forage/conformance/forage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forage-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.joinforage.app/
- group: auth
  href: https://artifacts.apis.io/forage/security/forage-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/forage-trust-center.yml
created: '2026-07-17'
description: Forage is a mission-driven payments company and one of only three payment processors approved by the USDA Food and Nutrition Service (FNS) to accept SNAP EBT and EBT Cash online. Forage gives grocery retailers, marketplaces, and platforms the API, SDKs, and regulatory expertise to add government-benefit tender (SNAP, EBT Cash, and HSA/FSA) to online and in-store checkout. The Forage Payments API tokenizes EBT cards, runs PIN-secured balance inquiries, and creates, captures, voids, and refunds EBT payments and orders, backed by JavaScript, iOS, Android, and POS Terminal SDKs, webhooks for order/payment/refund events, and daily CSV reconciliation reports.
finops:
- has_sources: true
  method: derived
  name: Forage Finops
  primary_unit: processing fee per transaction
  service_category: ''
  slug: forage-finops
  template: false
image: https://framerusercontent.com/assets/ZoPlyiuvY1BwAuHbWMWp7HW8UmE.png
json_schemas:
- name: ErrorResponseObject
  property_count: 2
  slug: forage-error-response-object
- name: OrderAndTaxesReportResponse
  property_count: 0
  slug: forage-order-and-taxes-report-response
- name: OrderPaymentResponse
  property_count: 0
  slug: forage-order-payment-response
- name: OrderRefundResponse
  property_count: 0
  slug: forage-order-refund-response
- name: PaymentRefundResponse
  property_count: 0
  slug: forage-payment-refund-response
- name: PaymentResponse
  property_count: 0
  slug: forage-payment-response
jsonld:
- class_count: 32
  name: Forage Context
  property_count: 96
  slug: forage-context
layout: provider
modified: '2026-07-19'
name: Forage
nav: Providers
network: true
overview: 'Forage publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including EBT SNAP Payments API, Bearer Tokens API, Card Details API, and 10 more. Tagged areas include Company, Payments, EBT, SNAP, and EBT Cash.


  The Forage catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Forage''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 40 more developer resources.'
plans:
- name: Forage Plans Pricing
  plan_count: 2
  slug: forage-plans-pricing
- name: Forage Price Estimates
  plan_count: 0
  slug: forage-price-estimates
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Forage API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: forage-rules
scopes:
- name: Forage Scopes
  scope_count: 6
  slug: forage-scopes
  summary_line: 6 scopes · password/clientCredentials
score:
  band: exemplar
  composite: 73.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 89.5
    contract_governance: 35.6
    contract_quality: 72.5
    developer_ergonomics: 73.2
    discoverability: 66.7
    operational_transparency: 63.2
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/forage/forage-2026-07-25T214925.png
security:
- kind: authentication
  name: Forage Authentication
  slug: forage-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Forage Domain Security
  slug: forage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Forage Trust Center
  slug: forage-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: Accept an EBT SNAP payment (SDK / Custom)
  slug: forage-accept-ebt-payment
- name: Run a Fully Hosted EBT checkout
  slug: forage-fully-hosted-checkout
- name: Refund an EBT SNAP payment
  slug: forage-refund-ebt-payment
slug: forage
tags:
- Company
- Payments
- EBT
- SNAP
- EBT Cash
- HSA/FSA
- Fintech
- Government Benefits
- Grocery
- Checkout
- Financial Services
website: https://www.joinforage.com
---
