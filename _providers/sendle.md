---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sendle Agentic Access
  operation_count: 17
  slug: sendle-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 5
apis:
- description: Create, view, cancel, and return parcel orders. Supports domestic AU / US / CA orders plus international from AU and US (DAP and DDP Price Guaranteed) and from CA to US. Returns label URLs, tracking U
  name: Sendle Orders API
  slug: sendle-orders-api
- description: Get one quote per shipping product for a given route. GET /products handles domestic and DAP international; POST /products adds DDP Price Guaranteed (duties + taxes included). Each quote includes plan
  name: Sendle Products & Quoting API
  slug: sendle-products-api
- description: 'Retrieve all tracking events for a parcel by Sendle reference, or subscribe a parcel to webhook tracking updates. Webhooks deliver per-event JSON payloads to the account-level callback URL configured '
  name: Sendle Tracking API
  slug: sendle-tracking-api
- description: Create, list, download (PDF), and inspect USPS SCAN Form shipping manifests so a driver can pick up many US Domestic Sendle orders with a single barcode scan. Orders must be created the same day as th
  name: Sendle Shipping Manifests API
  slug: sendle-manifests-api
- description: Connectivity and credential testing
  name: Sendle Utility API
  slug: sendle-utility-api
artifact_total: 30
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
  name: Sendle Shipping Manifests API
  slug: open-sendle-manifests-api
- collection_type: open
  name: Sendle Orders API
  slug: open-sendle-orders-api
- collection_type: open
  name: Sendle Ping API
  slug: open-sendle-ping-api
- collection_type: open
  name: Sendle Products & Quoting API
  slug: open-sendle-products-api
- collection_type: open
  name: Sendle Tracking API
  slug: open-sendle-tracking-api
common:
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
- group: start
  title: ''
  type: Portal
  url: https://developers.sendle.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sendle.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: https://developers.sendle.com/reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.sendle.com/reference/getting-your-api-key
- group: start
  title: ''
  type: Sandbox
  url: https://developers.sendle.com/reference/sendles-sandbox-server
- group: docs
  title: ''
  type: Guide
  url: https://developers.sendle.com/docs/integration-best-practices
- group: docs
  title: ''
  type: Guide
  url: https://developers.sendle.com/docs/regional-api-differences
- group: company
  title: ''
  type: Partnerships
  url: https://developers.sendle.com/docs/becoming-a-partner
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.sendle.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendle.com
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
  type: Pricing
  url: https://try.sendle.com/en-us/pricing
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
description: Sendle is a 100%-carbon-neutral parcel shipping service built for small businesses, offering door-to-door delivery in Australia, the United States, and Canada plus international shipping from AU and US to ~180 countries. The Sendle API exposes quoting, order creation, label retrieval, tracking, USPS SCAN-Form shipping manifests, and per-parcel tracking webhooks via HTTP Basic Authentication.
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
name: Sendle
nav: Providers
network: true
overview: 'Sendle publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Orders API, Products & Quoting API, Tracking API, and 2 more. Tagged areas include Shipping, Logistics, Last Mile, Parcels, and E-commerce.


  The Sendle catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Sendle''s developer surface includes authentication, developer portal, documentation, getting-started guide, sandbox, changelog, GitHub presence, and 16 more developer resources.'
plans:
- name: Sendle Plans Pricing
  plan_count: 3
  slug: sendle-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Sendle Rate Limits
  slug: sendle-rate-limits
rules:
- name: Sendle API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: sendle-asyncapi-spectral-rules
- name: Sendle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sendle-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.3
  delta: -3.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 85.4
    developer_ergonomics: 54.3
    discoverability: 74.1
    governance: 31.3
    operational_transparency: 68.4
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
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
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sendle
tags:
- Shipping
- Logistics
- Last Mile
- Parcels
- E-commerce
- Carbon Neutral
- Small Business
- Australia
- United States
- Canada
website: https://www.sendle.com
---
