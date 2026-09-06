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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-09-05'
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
artifact_total: 28
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
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: Overlay
  url: overlays/komerce-payment-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/komerce/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/komerce-agentic-access.yml
- group: auth
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
  title: ''
  type: Authentication
  url: authentication/komerce-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/komerce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/komerce-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/komerce-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/komerce-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/komerce-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/komerce-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/komerce-plans.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/komerce-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/komerce-packages.yml
- group: design
  title: ''
  type: Components
  url: components/komerce-components.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/komerce-couriers.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/komerce-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/komerce-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/komerce-examples.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/komerce-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/komerce-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Komerce is an Indonesian end-to-end e-commerce enabler serving more than 50,000 online sellers and SMEs with an integrated suite covering fulfilment, logistics, marketplace operations, CRM, advertising and payments — Komship, Kompack, Komplace, Komchat, Komcards, Komtim, Komads and Komclass. Its developer surface is published under the RajaOngkir brand and exposes four APIs: Shipping Cost (Cek Ongkir) for domestic and international rate lookup and airway-bill tracking across 17 Indonesian couriers, Shipping Delivery (Komship) for creating orders, requesting pickup, printing labels and tracking shipments, Payment Service for Virtual Account and QRIS transactions with signed callbacks, and QRISLY for turning a static QRIS into dynamic per-transaction QRIS codes. All four authenticate with a per-product header API key issued from the Collaborator dashboard, and the delivery, payment and QRIS products run a full isolated sandbox.'
image: https://komerce.id/img/komerce.png
layout: provider
modified: '2026-07-19'
name: Komerce
nav: Providers
network: true
overview: 'Komerce publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cost API, Destinations API, Orders API, and 4 more. Tagged areas include Company, Shipping, Logistics, E-Commerce, and Payments.


  The Komerce catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Komerce''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 29 more developer resources.'
plans:
- name: Komerce Plans
  plan_count: 3
  slug: komerce-plans
random_paper: 7
rate_limits:
- limit_count: 3
  name: Komerce Rate Limits
  slug: komerce-rate-limits
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.0
    catalog_earned_first_party: 29.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 19.7
    contract_quality: 23.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 19.7
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 46.6
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
    score: 26.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/komerce/refs/heads/main/screenshots/komerce-2026-07-25T224133.png
security:
- kind: authentication
  name: Komerce Authentication
  slug: komerce-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Komerce Domain Security
  slug: komerce-domain-security
  summary_line: TLSv1.3 · DMARC
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
