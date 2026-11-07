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
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: JWT-authenticated API for partner vendors (drop-off locations, scan events) to exchange an API key for a 24-hour access token and query shipment tracking status and event history.
  name: UniUni Partner API
  slug: uniuni-partner-api
- description: Legacy enterprise integration API documented as a public Postman collection — token-based authorization, freight estimation, sorting information, batch management, shipment creation/cancellation, labe
  name: UniUni Integration API
  slug: uniuni-integration-api
- baseURL: https://api.ship.uniuni.com/prod/client/
  baseurl_source: declared
  description: Group purchased shipments into batches for drop-off or pickup.
  name: UniUni Batches API
  slug: uniuni-batches-api
- baseURL: https://api.ship.uniuni.com/prod/client/
  baseurl_source: declared
  description: Retrieve shipping and batch labels as Base64-encoded PDFs.
  name: UniUni Labels API
  slug: uniuni-labels-api
- baseURL: https://api.ship.uniuni.com/prod/client/
  baseurl_source: declared
  description: Create, retrieve, list, purchase, refund, and delete shipments.
  name: UniUni Shipments API
  slug: uniuni-shipments-api
- baseURL: https://api.ship.uniuni.com/prod/client/
  baseurl_source: declared
  description: Track shipment status and scan events.
  name: UniUni Tracking API
  slug: uniuni-tracking-api
- baseURL: https://api.ship.uniuni.com/prod/client/
  baseurl_source: declared
  description: Receive real-time shipment status updates.
  name: UniUni Webhooks API
  slug: uniuni-webhooks-api
artifact_total: 21
asyncapis:
- description: ''
  name: Uniuni Webhooks
  slug: uniuni-webhooks
collections:
- collection_type: open
  name: UniUni Platform Client Batches API
  slug: open-uniuni-batches-api
- collection_type: open
  name: UniUni Platform Client Batches Labels API
  slug: open-uniuni-labels-api
- collection_type: open
  name: UniUni Platform Client Batches Shipments API
  slug: open-uniuni-shipments-api
- collection_type: open
  name: UniUni Platform Client Batches Tracking API
  slug: open-uniuni-tracking-api
- collection_type: open
  name: UniUni Platform Client Batches Webhooks API
  slug: open-uniuni-webhooks-api
common:
- group: commercial
  href: https://artifacts.apis.io/uniuni/plans/uniuni-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uniuni-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/uniuni/capabilities/uniuni-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/uniuni-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/uniuni/overlays/uniuni-platform-client-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uniuni-platform-client-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.uniuni.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ship.uniuni.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.ship.uniuni.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.ship.uniuni.com/en/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://help.ship.uniuni.com/en/getting-started/welcome
- group: operate
  title: ''
  type: Support
  url: https://www.uniuni.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.uniuni.com/news/
- group: start
  title: ''
  type: SignUp
  url: https://ship.uniuni.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.ship.uniuni.com/en/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uniuni.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://docs.uniuni.com/
- group: agent
  href: https://artifacts.apis.io/uniuni/llms/uniuni-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uniuni-llms.txt
- group: agent
  href: https://artifacts.apis.io/uniuni/mcp/uniuni-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uniuni-mcp.yml
- group: auth
  href: https://artifacts.apis.io/uniuni/authentication/uniuni-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uniuni-authentication.yml
- group: start
  href: https://artifacts.apis.io/uniuni/sandbox/uniuni-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/uniuni-sandbox.yml
- group: design
  href: https://artifacts.apis.io/uniuni/conventions/uniuni-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uniuni-conventions.yml
- group: design
  href: https://artifacts.apis.io/uniuni/errors/uniuni-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uniuni-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uniuni/lifecycle/uniuni-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uniuni-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/uniuni/conformance/uniuni-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uniuni-conformance.yml
- group: design
  href: https://artifacts.apis.io/uniuni/data-model/uniuni-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uniuni-data-model.yml
- group: design
  href: https://artifacts.apis.io/uniuni/asyncapi/uniuni-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/uniuni-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/uniuni/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/uniuni/security/uniuni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uniuni-domain-security.yml
created: '2026-07-17'
description: UniUni is a Canadian last-mile delivery carrier serving ecommerce businesses across Canada and the United States, delivering parcels through a crowdsourced driver network with hubs, stores, and partner drop-off locations. The UniUni Platform gives merchants shipment creation, label purchase, batching, wallet billing, tracking, and Shopify/ShipStation/WooCommerce integrations, alongside a REST Client API, a Partner API for vendor tracking updates, and a legacy Integration API for enterprise shippers.
finops:
- has_sources: true
  method: derived
  name: Uniuni Finops
  primary_unit: delivery
  service_category: ''
  slug: uniuni-finops
  template: false
image: https://mintcdn.com/uniexpressinc/YvoYth8Wg7rezp7U/logo/light.svg
layout: provider
modified: '2026-07-21'
name: UniUni
nav: Providers
network: true
overview: 'UniUni publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batches API, Labels API, Shipments API, and 4 more. Tagged areas include Company, Logistics, Shipping, Last Mile Delivery, and E-Commerce.


  The UniUni catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  UniUni''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Uniuni Plans Pricing
  plan_count: 2
  slug: uniuni-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: UniUni API Rules
  rule_count: 57
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 3
  slug: uniuni-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 59.9
    developer_ergonomics: 70.8
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 53.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/uniuni/uniuni-2026-08-17T082619.png
security:
- kind: authentication
  name: Uniuni Authentication
  slug: uniuni-authentication
  summary_line: http-bearer/apiKey · 3 schemes
- kind: domain-security
  name: Uniuni Domain Security
  slug: uniuni-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Batch UniUni shipments for drop-off or pickup
  slug: uniuni-batch-shipments
- name: Quote, create, purchase, and label a UniUni shipment
  slug: uniuni-quote-create-purchase-label
- name: Track UniUni shipments and receive webhook updates
  slug: uniuni-track-and-notify
slug: uniuni
tags:
- Company
- Logistics
- Shipping
- Last Mile Delivery
- E-Commerce
- Tracking
- Delivery
website: https://www.uniuni.com/
---
