---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: Information and updating of collections
  name: Nabis Collection API
  slug: nabis-collection-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: Inventory CSVs
  name: Nabis Inventory API
  slug: nabis-inventory-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The Inventory History API from Nabis — 2 operation(s) for inventory history.
  name: Nabis Inventory History API
  slug: nabis-inventory-history-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The Invoice API from Nabis — 1 operation(s) for invoice.
  name: Nabis Invoice API
  slug: nabis-invoice-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: Invoices/Aging Report CSVs
  name: Nabis Invoices API
  slug: nabis-invoices-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The NabisDaysOff API from Nabis — 1 operation(s) for nabisdaysoff.
  name: Nabis Nabis Days Off API
  slug: nabis-nabisdaysoff-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The NY Inventory API from Nabis — 3 operation(s) for ny inventory.
  name: Nabis NY Inventory API
  slug: nabis-ny-inventory-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The NY Invoice API from Nabis — 1 operation(s) for ny invoice.
  name: Nabis NY Invoice API
  slug: nabis-ny-invoice-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The NY Order API from Nabis — 2 operation(s) for ny order.
  name: Nabis NY Order API
  slug: nabis-ny-order-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The NY Retailer API from Nabis — 2 operation(s) for ny retailer.
  name: Nabis NY Retailer API
  slug: nabis-ny-retailer-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The NYWarehouse API from Nabis — 1 operation(s) for nywarehouse.
  name: Nabis NY Warehouse API
  slug: nabis-nywarehouse-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The Order API from Nabis — 2 operation(s) for order.
  name: Nabis Order API
  slug: nabis-order-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: Order CSVs
  name: Nabis Orders API
  slug: nabis-orders-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The Retailer API from Nabis — 2 operation(s) for retailer.
  name: Nabis Retailer API
  slug: nabis-retailer-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: Information about sku details
  name: Nabis Sku API
  slug: nabis-sku-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: Information and updating skubatches
  name: Nabis Skubatch API
  slug: nabis-skubatch-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The Universal Cannabis Labeling API from Nabis — 3 operation(s) for universal cannabis labeling.
  name: Nabis Universal Cannabis Labeling API
  slug: nabis-universal-cannabis-labeling-api
- baseURL: https://platform-api.nabis.pro
  baseurl_source: declared
  description: The Warehouses API from Nabis — 1 operation(s) for warehouses.
  name: Nabis Warehouses API
  slug: nabis-warehouses-api
artifact_total: 23
collections:
- collection_type: postman
  name: NABIS Platform API v2
  slug: postman-nabis-platform-api-v2
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nabis-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nabis-platform-api-v2-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nabis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nabis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.nabis.com/v2/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.nabis.com/v2/docs/overview/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.nabis.com/v2/docs/category/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.nabis.com/v2/docs/overview/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/nabis-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.nabis.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.nabis.com/newsroom/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.nabis.com/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://www.nabis.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.nabis.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nabis.com/legal/license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nabis.com/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://developers.nabis.com/v2/assets/NABIS-Platform-API-v2.postman_collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nabis.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nabis-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nabis-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nabis-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nabis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nabis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nabis-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nabis-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nabis-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nabis-plans-pricing.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nabis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nabis-llms.txt
- group: build
  title: ''
  type: Examples
  url: examples/nabis-examples.yml
created: '2026-08-26'
description: Nabis is a licensed cannabis wholesale distributor and B2B marketplace founded in 2018 by Vince C. Ning and Jun S. Lee, operating in California, New York and Nevada. It runs distribution and fulfillment warehouses, an ordering marketplace connecting 400+ cannabis brands to licensed retailers, an analytics layer, and Nabis Capital, an invoice-based financing product, plus Nabis BillPay and Nabis Tracker for retailers. The company reports that 99% of retailers in the three states it serves receive product through Nabis and that it fulfills 3,500+ wholesale orders a week. For developers it publishes the Nabis Platform API — a read-only, API-key-authenticated JSON REST API for brands and retailers covering inventory, inventory history, orders, invoices, retailers, warehouses and the Nabis delivery calendar, with separate California and New York route trees, and an implementation of the Universal Cannabis API labeling standard for order manifests and QR-code regulator events.
image: https://cdn.prod.website-files.com/5c253860fd28a73e98ee5416/639cbabbb5d9b23d53a27b01_nabis_ogimage.jpg
layout: provider
modified: '2026-08-26'
name: Nabis
nav: Providers
network: true
overview: 'Nabis publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Collection API, Inventory API, Inventory History API, and 15 more. Tagged areas include Cannabis, Distribution, Wholesale, Marketplace, and Logistics.


  Nabis'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Nabis Plans Pricing
  plan_count: 0
  slug: nabis-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Nabis Rate Limits
  slug: nabis-rate-limits
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 50.0
    developer_ergonomics: 63.7
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 49.9
  provenance:
    conformance: first-party
    contracts:
      callable: 83.3
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nabis/refs/heads/main/screenshots/nabis-2026-09-02T150717.png
security:
- kind: authentication
  name: Nabis Authentication
  slug: nabis-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nabis Domain Security
  slug: nabis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nabis
tags:
- Cannabis
- Distribution
- Wholesale
- Marketplace
- Logistics
- Supply Chain
- Inventory
- Order
- Invoicing
- Retail
- Compliance
- Track and Trace
- California
- New York
website: https://www.nabis.com/
---
