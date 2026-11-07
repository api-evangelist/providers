---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Marketsdk Agentic Access
  operation_count: 85
  slug: marketsdk-agentic-access
  summary_line: 85 operations · 46 acting
api_count: 1
apis:
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Buyers API from MarketSDK — 2 operation(s) for buyers.
  name: MarketSDK Buyers API
  slug: marketsdk-buyers-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Categories API from MarketSDK — 3 operation(s) for categories.
  name: MarketSDK Categories API
  slug: marketsdk-categories-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Listings API from MarketSDK — 9 operation(s) for listings.
  name: MarketSDK Listings API
  slug: marketsdk-listings-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Marketplace API from MarketSDK — 1 operation(s) for marketplace.
  name: MarketSDK Marketplace API
  slug: marketsdk-marketplace-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Moderation API from MarketSDK — 4 operation(s) for moderation.
  name: MarketSDK Moderation API
  slug: marketsdk-moderation-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Orders API from MarketSDK — 10 operation(s) for orders.
  name: MarketSDK Orders API
  slug: marketsdk-orders-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Payments API from MarketSDK — 5 operation(s) for payments.
  name: MarketSDK Payments API
  slug: marketsdk-payments-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Reputation API from MarketSDK — 2 operation(s) for reputation.
  name: MarketSDK Reputation API
  slug: marketsdk-reputation-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Reviews API from MarketSDK — 2 operation(s) for reviews.
  name: MarketSDK Reviews API
  slug: marketsdk-reviews-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Search API from MarketSDK — 1 operation(s) for search.
  name: MarketSDK Search API
  slug: marketsdk-search-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Sellers API from MarketSDK — 5 operation(s) for sellers.
  name: MarketSDK Sellers API
  slug: marketsdk-sellers-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Trust API from MarketSDK — 10 operation(s) for trust.
  name: MarketSDK Trust API
  slug: marketsdk-trust-api
- baseURL: https://api.marketsdk.com
  baseurl_source: declared
  description: The Webhooks API from MarketSDK — 8 operation(s) for webhooks.
  name: MarketSDK Webhooks API
  slug: marketsdk-webhooks-api
artifact_total: 28
common:
- group: agent
  href: https://artifacts.apis.io/marketsdk/agentic-access/marketsdk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/marketsdk-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/marketsdk/plans/marketsdk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/marketsdk-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/rules/marketsdk-rules.yml
  title: ''
  type: Spectral
  url: rules/marketsdk-rules.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/json-ld/marketsdk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/marketsdk-context.jsonld
- group: design
  href: https://artifacts.apis.io/marketsdk/vocabulary/marketsdk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/marketsdk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/marketsdk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/data-model/marketsdk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/marketsdk-data-model.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/conventions/marketsdk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/marketsdk-conventions.yml
- group: start
  href: https://artifacts.apis.io/marketsdk/sandbox/marketsdk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/marketsdk-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/marketsdk/security/marketsdk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/marketsdk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/marketsdk/authentication/marketsdk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/marketsdk-authentication.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/lifecycle/marketsdk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/marketsdk-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/errors/marketsdk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/marketsdk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/marketsdk/conformance/marketsdk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/marketsdk-conformance.yml
- group: other
  href: https://artifacts.apis.io/marketsdk/hosts/marketsdk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/marketsdk-hosts.yml
- group: other
  href: https://artifacts.apis.io/marketsdk/vendors/marketsdk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/marketsdk-vendors.yml
- group: build
  href: https://artifacts.apis.io/marketsdk/packages/marketsdk-packages.yml
  title: ''
  type: SDKs
  url: packages/marketsdk-packages.yml
- group: build
  href: https://artifacts.apis.io/marketsdk/packages/marketsdk-packages.yml
  title: ''
  type: Packages
  url: packages/marketsdk-packages.yml
- group: auth
  href: https://artifacts.apis.io/marketsdk/security/marketsdk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/marketsdk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/marketsdk/security/marketsdk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/marketsdk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marketsdk.com
- group: docs
  title: ''
  type: Documentation
  url: https://marketsdk.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://marketsdk.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://marketsdk.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://marketsdk.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://marketsdk.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marketsdk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marketsdk.com/privacy
created: '2026-10-30'
description: MarketSDK is a headless API for high‑trust peer‑to‑peer marketplaces. It enables SaaS platforms to add a marketplace where users can sell templates, plugins, and extensions to each other without building payments, trust, or moderation infrastructure. Developers can start free in a sandbox, go live instantly, and retain 100 % of sales revenue.
image: https://marketsdk.com/opengraph-image?89c1a0a068026426
json_schemas:
- name: CreateWebhookEndpointDto
  property_count: 4
  slug: marketsdk-create-webhook-endpoint-dto
- name: EventObject
  property_count: 7
  slug: marketsdk-event-object
- name: OrderObject
  property_count: 21
  slug: marketsdk-order-object
- name: PaymentObject
  property_count: 19
  slug: marketsdk-payment-object
- name: RefundObject
  property_count: 15
  slug: marketsdk-refund-object
- name: UpdateWebhookEndpointDto
  property_count: 5
  slug: marketsdk-update-webhook-endpoint-dto
jsonld:
- class_count: 101
  name: Marketsdk Context
  property_count: 211
  slug: marketsdk-context
layout: provider
modified: '2026-10-30'
name: MarketSDK
nav: Providers
network: true
overview: 'MarketSDK publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Buyers API, Categories API, Listings API, and 10 more. Tagged areas include Marketplace, Software-as-a-Service, Payments, and Trust.


  The MarketSDK catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MarketSDK''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, pricing, support, and 21 more developer resources.'
plans:
- name: Marketsdk Plans Pricing
  plan_count: 4
  slug: marketsdk-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Marketsdk Rate Limits
  slug: marketsdk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: MarketSDK API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: marketsdk-rules
scopes:
- name: Marketsdk Scopes
  scope_count: 0
  slug: marketsdk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 61.2
    developer_ergonomics: 49.3
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/marketsdk/marketsdk-2026-11-03T135333.png
security:
- kind: authentication
  name: Marketsdk Authentication
  slug: marketsdk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Marketsdk Domain Security
  slug: marketsdk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Marketsdk Vulnerability Disclosure
  slug: marketsdk-vulnerability-disclosure
  summary_line: no policy recorded
slug: marketsdk
tags:
- Marketplace
- Software-as-a-Service
- Payments
- Trust
website: https://marketsdk.com
---
