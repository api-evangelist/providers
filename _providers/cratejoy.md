---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'REST interface into most of the data and functionality of interest to Cratejoy merchants and developers: customers, orders, subscriptions, shipments, products, inventory, carts, transactions, addresse'
  name: Cratejoy Merchant API
  slug: cratejoy-merchant-api
- description: 'Front-end API that lets storefront JavaScript read (and sometimes write) data on behalf of the logged-in customer: customer, product, subscription, shipment, address, and survey methods, plus add-to-c'
  name: Cratejoy Store API
  slug: cratejoy-store-api
artifact_total: 5
asyncapis:
- description: ''
  name: Cratejoy Webhooks
  slug: cratejoy-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.cratejoy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cratejoy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cratejoy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cratejoy.com/reference/introduction-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cratejoy.com/reference/quick-start-add-a-tracking-number-to-a-shipment
- group: operate
  title: ''
  type: Support
  url: https://www.cratejoy.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://www.cratejoy.com/blogs/box-insider
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cratejoy
- group: commercial
  title: ''
  type: Pricing
  url: https://sell.cratejoy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sell.cratejoy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cratejoy.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cratejoy.com/pages/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cratejoy.com
- group: agent
  href: https://artifacts.apis.io/cratejoy/llms/cratejoy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cratejoy-llms.txt
- group: auth
  href: https://artifacts.apis.io/cratejoy/authentication/cratejoy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cratejoy-authentication.yml
- group: design
  href: https://artifacts.apis.io/cratejoy/conventions/cratejoy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cratejoy-conventions.yml
- group: design
  href: https://artifacts.apis.io/cratejoy/errors/cratejoy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cratejoy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cratejoy/asyncapi/cratejoy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cratejoy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cratejoy/lifecycle/cratejoy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cratejoy-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/cratejoy/packages/cratejoy-packages.yml
  title: ''
  type: Packages
  url: packages/cratejoy-packages.yml
- group: agent
  href: https://artifacts.apis.io/cratejoy/mcp/cratejoy-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cratejoy-mcp.yml
- group: design
  href: https://artifacts.apis.io/cratejoy/conformance/cratejoy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cratejoy-conformance.yml
- group: design
  href: https://artifacts.apis.io/cratejoy/data-model/cratejoy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cratejoy-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cratejoy/security/cratejoy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cratejoy-domain-security.yml
created: '2026-07-17'
description: 'Cratejoy is a subscription-box commerce platform and marketplace (a CRV and Y Combinator company) that lets independent creators launch, sell, and manage recurring subscription boxes and one-time products. It exposes two public REST APIs: a Merchant API (https://api.cratejoy.com/v1/) covering customers, orders, subscriptions, shipments, products, inventory, carts, transactions, and webhooks; and a front-end Store API for reading and writing customer-scoped data from a storefront theme. Resources are JSON, authenticated with HTTP Basic credentials, paginated, filterable with double-underscore operators, and rate-limited with Retry-After.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cratejoy.png
layout: provider
modified: '2026-07-18'
name: Cratejoy
nav: Providers
network: true
overview: 'Cratejoy is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Subscription, Subscription Boxes, and Marketplace.


  The Cratejoy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cratejoy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 41.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cratejoy/cratejoy-2026-07-25T210648.png
security:
- kind: authentication
  name: Cratejoy Authentication
  slug: cratejoy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cratejoy Domain Security
  slug: cratejoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cratejoy
tags:
- Company
- E-Commerce
- Subscription
- Subscription Boxes
- Marketplace
- Payments
- Order
- Webhook
- REST
website: https://www.cratejoy.com/
---
