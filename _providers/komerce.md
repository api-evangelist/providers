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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Komerce Agentic Access
  operation_count: 25
  slug: komerce-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 4
apis:
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: Shipping cost calculation
  name: Komerce Cost API
  slug: komerce-cost-api
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: Destination and administrative-region lookup
  name: Komerce Destinations API
  slug: komerce-destinations-api
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: The Orders API from Komerce — 4 operation(s) for orders.
  name: Komerce Orders API
  slug: komerce-orders-api
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: The Payments API from Komerce — 4 operation(s) for payments.
  name: Komerce Payments API
  slug: komerce-payments-api
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: The Pickup API from Komerce — 1 operation(s) for pickup.
  name: Komerce Pickup API
  slug: komerce-pickup-api
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: The QRIS API from Komerce — 3 operation(s) for qris.
  name: Komerce QRIS API
  slug: komerce-qris-api
- baseURL: https://rajaongkir.komerce.id/api/v1
  baseurl_source: declared
  description: Airway bill tracking
  name: Komerce Tracking API
  slug: komerce-tracking-api
artifact_total: 34
asyncapis:
- description: ''
  name: Komerce Webhooks
  slug: komerce-webhooks
collections:
- collection_type: postman
  name: Komerce Payment Service Cost API
  slug: postman-komerce-cost-api
- collection_type: postman
  name: Komerce Payment Service Cost Destinations API
  slug: postman-komerce-destinations-api
- collection_type: postman
  name: Komerce Payment Service Cost Orders API
  slug: postman-komerce-orders-api
- collection_type: postman
  name: Komerce Payment Service Cost Payments API
  slug: postman-komerce-payments-api
- collection_type: postman
  name: Komerce Payment Service Cost Pickup API
  slug: postman-komerce-pickup-api
- collection_type: postman
  name: Komerce Payment Service Cost QRIS API
  slug: postman-komerce-qris-api
- collection_type: postman
  name: Komerce Payment Service Cost Tracking API
  slug: postman-komerce-tracking-api
- collection_type: open
  name: Komerce Payment Service Cost API
  slug: open-komerce-cost-api
- collection_type: open
  name: Komerce Payment Service Cost Destinations API
  slug: open-komerce-destinations-api
- collection_type: open
  name: Komerce Payment Service Cost Orders API
  slug: open-komerce-orders-api
- collection_type: open
  name: Komerce Payment Service Cost Payments API
  slug: open-komerce-payments-api
- collection_type: open
  name: Komerce Payment Service Cost Pickup API
  slug: open-komerce-pickup-api
- collection_type: open
  name: Komerce Payment Service Cost QRIS API
  slug: open-komerce-qris-api
- collection_type: open
  name: Komerce Payment Service Cost Tracking API
  slug: open-komerce-tracking-api
common:
- group: company
  title: ''
  type: Blog
  url: https://komerce.id/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://komerce.id/blog/feed/
- group: other
  href: https://artifacts.apis.io/komerce/overlays/komerce-payment-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/komerce-payment-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/komerce/overview
- group: agent
  href: https://artifacts.apis.io/komerce/agentic-access/komerce-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/komerce-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/komerce/security/komerce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/komerce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://komerce.id
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rajaongkir.com
- group: docs
  title: ''
  type: Documentation
  url: https://rajaongkir.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rajaongkir.com/docs/shipping-cost/getting_started/endpoint
- group: start
  title: ''
  type: GettingStarted
  url: https://rajaongkir.com/docs/introduction/register
- group: start
  title: ''
  type: SignUp
  url: https://collaborator.komerce.id/registration
- group: start
  title: ''
  type: Login
  url: https://collaborator.komerce.id/login
- group: commercial
  title: ''
  type: Pricing
  url: https://rajaongkir.com/pricing
- group: operate
  title: ''
  type: Support
  url: mailto:support@rajaongkir.com
- group: company
  title: ''
  type: Blog
  url: https://komerce.id/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://komerce.id/syarat-ketentuan
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://komerce.id/kebijakan-privasi
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rajaongkir.com
- group: build
  title: ''
  type: Postman
  url: https://rajaongkir.com/docs/shipping-cost/getting_started/postman_collection
- group: auth
  href: https://artifacts.apis.io/komerce/authentication/komerce-authentication.yml
  title: ''
  type: Authentication
  url: authentication/komerce-authentication.yml
- group: design
  href: https://artifacts.apis.io/komerce/conventions/komerce-conventions.yml
  title: ''
  type: Conventions
  url: conventions/komerce-conventions.yml
- group: design
  href: https://artifacts.apis.io/komerce/errors/komerce-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/komerce-problem-types.yml
- group: design
  href: https://artifacts.apis.io/komerce/errors/komerce-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/komerce-error-codes.yml
- group: design
  href: https://artifacts.apis.io/komerce/lifecycle/komerce-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/komerce-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/komerce/sandbox/komerce-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/komerce-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/komerce/rate-limits/komerce-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/komerce-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/komerce/plans/komerce-plans.yml
  title: ''
  type: Plans
  url: plans/komerce-plans.yml
- group: design
  href: https://artifacts.apis.io/komerce/asyncapi/komerce-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/komerce-webhooks.yml
- group: build
  href: https://artifacts.apis.io/komerce/packages/komerce-packages.yml
  title: ''
  type: Packages
  url: packages/komerce-packages.yml
- group: design
  href: https://artifacts.apis.io/komerce/components/komerce-components.yml
  title: ''
  type: Components
  url: components/komerce-components.yml
- group: design
  href: https://artifacts.apis.io/komerce/vocabulary/komerce-couriers.yml
  title: ''
  type: Vocabulary
  url: vocabulary/komerce-couriers.yml
- group: design
  href: https://artifacts.apis.io/komerce/data-model/komerce-data-model.yml
  title: ''
  type: DataModel
  url: data-model/komerce-data-model.yml
- group: design
  href: https://artifacts.apis.io/komerce/conformance/komerce-conformance.yml
  title: ''
  type: Conformance
  url: conformance/komerce-conformance.yml
- group: build
  href: https://artifacts.apis.io/komerce/examples/komerce-examples.yml
  title: ''
  type: Examples
  url: examples/komerce-examples.yml
- group: agent
  href: https://artifacts.apis.io/komerce/mcp/komerce-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/komerce-mcp.yml
- group: agent
  href: https://artifacts.apis.io/komerce/llms/komerce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/komerce-llms.txt
- group: agent
  href: https://artifacts.apis.io/komerce/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Komerce is an Indonesian end-to-end e-commerce enabler serving more than 50,000 online sellers and SMEs with an integrated suite covering fulfilment, logistics, marketplace operations, CRM, advertising and payments — Komship, Kompack, Komplace, Komchat, Komcards, Komtim, Komads and Komclass. Its developer surface is published under the RajaOngkir brand and exposes four APIs: Shipping Cost (Cek Ongkir) for domestic and international rate lookup and airway-bill tracking across 17 Indonesian couriers, Shipping Delivery (Komship) for creating orders, requesting pickup, printing labels and tracking shipments, Payment Service for Virtual Account and QRIS transactions with signed callbacks, and QRISLY for turning a static QRIS into dynamic per-transaction QRIS codes. All four authenticate with a per-product header API key issued from the Collaborator dashboard, and the delivery, payment and QRIS products run a full isolated sandbox.'
finops:
- has_sources: true
  method: derived
  name: Komerce Finops
  primary_unit: transaction amount
  service_category: ''
  slug: komerce-finops
  template: false
image: https://komerce.id/img/komerce.png
layout: provider
modified: '2026-10-06'
name: Komerce
nav: Providers
network: true
overview: 'Komerce publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cost API, Destinations API, Orders API, and 4 more. Tagged areas include Company, Shipping, Logistics, E-Commerce, and Payments.


  The Komerce catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Komerce''s developer surface includes engineering blog, documentation, API reference, getting-started guide, signup flow, pricing, support, and 31 more developer resources.'
plans:
- name: Komerce Plans
  plan_count: 4
  slug: komerce-plans
- name: Komerce Price Estimates
  plan_count: 0
  slug: komerce-price-estimates
random_paper: 22
rate_limits:
- limit_count: 3
  name: Komerce Rate Limits
  slug: komerce-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Komerce API Rules
  rule_count: 61
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 4
  slug: komerce-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 76.5
    catalog_earned_first_party: 29.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 56.6
    contract_governance: 33.3
    contract_quality: 23.7
    developer_ergonomics: 70.8
    discoverability: 78.6
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/komerce/komerce-2026-07-25T224133.png
security:
- kind: authentication
  name: Komerce Authentication
  slug: komerce-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Komerce Domain Security
  slug: komerce-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Collect a payment with the Komerce Payment Service
  slug: komerce-collect-payment
- name: Create a Komship delivery order and ship it
  slug: komerce-create-and-ship-order
- name: Generate a dynamic QRIS with QRISLY
  slug: komerce-generate-dynamic-qris
- name: Quote domestic shipping with RajaOngkir
  slug: komerce-quote-domestic-shipping
slug: komerce
tags:
- Company
- Shipping
- Logistics
- E-Commerce
- Payments
- QRIS
- Indonesia
- Couriers
- Tracking
- Fulfillment
website: https://komerce.id
---
