---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sendle Agentic Access
  operation_count: 17
  slug: sendle-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.sendle.com/api
  baseurl_source: declared
  description: Create, view, cancel, and return parcel orders. Supports domestic AU / US / CA orders plus international from AU and US (DAP and DDP Price Guaranteed) and from CA to US. Returns label URLs, tracking U
  name: Sendle Orders API
  slug: sendle-orders-api
- baseURL: https://api.sendle.com/api
  baseurl_source: declared
  description: Get one quote per shipping product for a given route. GET /products handles domestic and DAP international; POST /products adds DDP Price Guaranteed (duties + taxes included). Each quote includes plan
  name: Sendle Products & Quoting API
  slug: sendle-products-api
- baseURL: https://api.sendle.com/api
  baseurl_source: declared
  description: 'Retrieve all tracking events for a parcel by Sendle reference, or subscribe a parcel to webhook tracking updates. Webhooks deliver per-event JSON payloads to the account-level callback URL configured '
  name: Sendle Tracking API
  slug: sendle-tracking-api
- baseURL: https://api.sendle.com/api
  baseurl_source: declared
  description: Create, list, download (PDF), and inspect USPS SCAN Form shipping manifests so a driver can pick up many US Domestic Sendle orders with a single barcode scan. Orders must be created the same day as th
  name: Sendle Shipping Manifests API
  slug: sendle-manifests-api
- baseURL: https://api.sendle.com/api
  baseurl_source: declared
  description: Connectivity and credential testing
  name: Sendle Utility API
  slug: sendle-utility-api
artifact_total: 32
asyncapis:
- description: Sendle pushes parcel tracking events to a callback URL configured in the account Settings -> API page. Subscriptions are created per parcel via the Tracking API. Sendle expects 2xx responses; failed d
  name: Sendle Tracking Webhooks
  slug: sendle-tracking-asyncapi
collections:
- collection_type: postman
  name: Sendle Shipping Manifests API
  slug: postman-sendle-manifests-api
- collection_type: postman
  name: Sendle Shipping Manifests Orders API
  slug: postman-sendle-orders-api
- collection_type: postman
  name: Sendle Shipping Manifests Products API
  slug: postman-sendle-products-api
- collection_type: postman
  name: Sendle Shipping Manifests Tracking API
  slug: postman-sendle-tracking-api
- collection_type: postman
  name: Sendle Shipping Manifests Utility API
  slug: postman-sendle-utility-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sendle Shipping Manifests API
  slug: open-sendle-manifests-api
- collection_type: open
  name: Sendle Shipping Manifests Orders API
  slug: open-sendle-orders-api
- collection_type: open
  name: Sendle Ping API
  slug: open-sendle-ping-api
- collection_type: open
  name: Sendle Shipping Manifests Products API
  slug: open-sendle-products-api
- collection_type: open
  name: Sendle Shipping Manifests Tracking API
  slug: open-sendle-tracking-api
- collection_type: open
  name: Sendle Shipping Manifests Utility API
  slug: open-sendle-utility-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/sendle-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendle/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendle-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendle.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sendle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendle
- group: commercial
  title: ''
  type: Plans
  url: plans/sendle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sendle-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sendle-vocabulary.yml
- group: operate
  title: ''
  type: Support
  url: mailto:api@sendle.com
- group: build
  title: ''
  type: Packages
  url: packages/sendle-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendle-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/sendle-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sendle-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendle-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendle-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sendle-conformance.yml
coverage:
  checked: '2026-08-26'
  detail: Sendle ceased operations on 2026-01-11 and entered liquidation; api.sendle.com, developers.sendle.com, sandbox.sendle.com, status.sendle.com and try.sendle.com all return NXDOMAIN from the sendle.com authoritative nameserver, leaving only a client-rendered marketing shell on www.sendle.com that answers every /.well-known/ path with the same 18,276-byte HTML body.
  evidence:
  - status: 0
    url: https://api.sendle.com/api/ping
  - status: 0
    url: https://developers.sendle.com/reference/welcome
  - status: 0
    url: https://status.sendle.com
  - status: 200
    url: https://www.sendle.com/.well-known/security.txt
  - status: 200
    url: https://www.sendle.com
  reason: defunct
  state: none
created: '2026-05-25'
description: RETIRED — Sendle ceased operations on 11 January 2026 and the company entered liquidation; the API host, developer hub, sandbox and status page have all been withdrawn from DNS and returned NXDOMAIN when probed on 26 August 2026. Sendle was a 100%-carbon-neutral parcel shipping service built for small businesses, offering door-to-door delivery in Australia, the United States and Canada plus international shipping from AU and US to ~180 countries. Its API exposed quoting, order creation, label retrieval, tracking, USPS SCAN-Form shipping manifests and per-parcel tracking webhooks over HTTP Basic Authentication, with an Idempotency-Key header on order creation. The five OpenAPI definitions in this repository are retained as an archival record of a contract that can no longer be called.
examples:
- key_count: 2
  name: Sendle Create Order Example
  slug: sendle-create-order-example
- key_count: 2
  name: Sendle Track Parcel Example
  slug: sendle-track-parcel-example
- key_count: 3
  name: Sendle Tracking Webhook Example
  slug: sendle-tracking-webhook-example
finops:
- name: Sendle Finops
  service_category: ''
  slug: sendle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendle.png
json_schemas:
- name: Sendle Order
  property_count: 17
  slug: sendle-order
- name: Sendle Tracking Event
  property_count: 13
  slug: sendle-tracking-event
jsonld:
- class_count: 5
  name: Sendle Context
  property_count: 23
  slug: sendle-context
layout: provider
modified: '2026-08-26'
name: Sendle
nav: Providers
network: true
overview: 'Sendle publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Products & Quoting API, Tracking API, and 2 more. Tagged areas include Shipping, Logistics, Last Mile, Parcels, and E-Commerce.


  The Sendle catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Sendle''s developer surface includes authentication, GitHub presence, support, and 18 more developer resources.'
plans:
- name: Sendle Plans Pricing
  plan_count: 3
  slug: sendle-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Sendle Rate Limits
  slug: sendle-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Sendle API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: sendle-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Sendle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sendle-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 90.5
    catalog_earned_first_party: 24.0
    catalog_gap: 24.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 33.3
    contract_quality: 72.4
    developer_ergonomics: 17.9
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - canada
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
    - north-america
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendle/refs/heads/main/screenshots/sendle-2026-06-20T193655.png
security:
- kind: authentication
  name: Sendle Authentication
  slug: sendle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendle Domain Security
  slug: sendle-domain-security
  summary_line: TLSv1.3
slug: sendle
tags:
- Shipping
- Logistics
- Last Mile
- Parcels
- E-Commerce
- Carbon Neutral
- Small Business
- Australia
- United States
- Canada
website: https://www.sendle.com
---
