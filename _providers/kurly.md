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
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Kurly Agentic Access
  operation_count: 33
  slug: kurly-agentic-access
  summary_line: 33 operations · 14 acting
api_count: 4
apis:
- baseURL: https://kls.kurly.com
  baseurl_source: declared
  description: The Authentication API from Kurly — 1 operation(s) for authentication.
  name: Kurly Authentication API
  slug: kurly-authentication-api
- baseURL: https://kls.kurly.com
  baseurl_source: declared
  description: The 배송운영 정책 API from Kurly — 26 operation(s) for 배송운영 정책.
  name: Kurly 배송운영 정책 API
  slug: kurly-default-api
- baseURL: https://kls.kurly.com
  baseurl_source: declared
  description: The Delivery Tracking (배송추적) API from Kurly — 1 operation(s) for delivery tracking (배송추적).
  name: Kurly Delivery Tracking (배송추적) API
  slug: kurly-delivery-tracking-api
arazzos:
- description: Authenticate against KLS, confirm the shipper's contracted delivery services, register a delivery-agency order with a caller-supplied requestKey, read the order back by that key, pull the waybill prin
  name: Kurly delivery-agency order through to delivery tracking
  slug: kurly-delivery-order-to-tracking
- description: 'Map a sales-channel product to a Kurly SKU, verify stock, place a bulk outbound order against Kurly''s centre, read the fulfillment plan and reconcile the order. Grounded in the operations captured in '
  name: Kurly fulfillment outbound order flow
  slug: kurly-fulfillment-order-flow
- description: Register a SKU, book it inbound to a Kurly fulfillment centre with an idempotency key, pull the inbound label and transaction specification, then poll request-level status, item-level status and excep
  name: Kurly fulfillment inbound receiving flow
  slug: kurly-inbound-receiving-flow
artifact_total: 18
collections:
- collection_type: open
  name: Kurly Logistics Services (KLS) Open API Authentication API
  slug: open-kurly-authentication-api
- collection_type: open
  name: Kurly Logistics Services (KLS) Open API Authentication 배송운영 정책 API
  slug: open-kurly-default-api
- collection_type: open
  name: Kurly Logistics Services (KLS) Open API Authentication Delivery Tracking (배송추적) API
  slug: open-kurly-delivery-tracking-api
common:
- group: operate
  href: https://artifacts.apis.io/kurly/rate-limits/kurly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kurly-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/kurly/capabilities/kurly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kurly-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/kurly/overlays/kurly-auth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kurly-auth-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://kurly.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kurly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kurly.com/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kurly.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.kurly.com/docs/intro
- group: operate
  title: ''
  type: Support
  url: https://developers.kurly.com/docs/faq
- group: company
  title: ''
  type: Blog
  url: https://helloworld.kurly.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thefarmersfront
- group: start
  title: ''
  type: SignUp
  url: https://developers.kurly.com/docs/auth
- group: start
  title: ''
  type: Console
  url: https://kls.kurly.com/
- group: auth
  href: https://artifacts.apis.io/kurly/authentication/kurly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kurly-authentication.yml
- group: agent
  href: https://artifacts.apis.io/kurly/agentic-access/kurly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kurly-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/kurly/mcp/kurly-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kurly-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kurly/llms/kurly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kurly-llms.txt
- group: agent
  href: https://artifacts.apis.io/kurly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kurly/conventions/kurly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kurly-conventions.yml
- group: design
  href: https://artifacts.apis.io/kurly/conventions/kurly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kurly-conventions.yml
- group: design
  href: https://artifacts.apis.io/kurly/errors/kurly-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/kurly-error-codes.yml
- group: design
  href: https://artifacts.apis.io/kurly/data-model/kurly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kurly-data-model.yml
- group: design
  href: https://artifacts.apis.io/kurly/vocabulary/kurly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kurly-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/kurly/rate-limits/kurly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kurly-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/kurly/lifecycle/kurly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kurly-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/kurly/changelog/kurly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kurly-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.kurly.com/changelog
- group: design
  href: https://artifacts.apis.io/kurly/conformance/kurly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kurly-conformance.yml
- group: start
  href: https://artifacts.apis.io/kurly/sandbox/kurly-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kurly-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/kurly/security/kurly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kurly-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/kurly/well-known/kurly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kurly-well-known.yml
- group: design
  href: https://artifacts.apis.io/kurly/arazzo/kurly-delivery-order-to-tracking.yml
  title: ''
  type: Arazzo
  url: arazzo/kurly-delivery-order-to-tracking.yml
- group: design
  href: https://artifacts.apis.io/kurly/arazzo/kurly-inbound-receiving-flow.yml
  title: ''
  type: Arazzo
  url: arazzo/kurly-inbound-receiving-flow.yml
- group: design
  href: https://artifacts.apis.io/kurly/arazzo/kurly-fulfillment-order-flow.yml
  title: ''
  type: Arazzo
  url: arazzo/kurly-fulfillment-order-flow.yml
created: '2026-07-17'
description: 'Kurly (컬리, operated by The Farmers Front) is a South Korean online grocery and lifestyle commerce company, known for Market Kurly and its overnight "dawn delivery" (샛별배송) model built on a cold-chain fulfillment network. Kurly Logistics Services (KLS) opens that network to contracted shipper clients (화주사) as a B2B Open API spanning three service families: fulfillment (물류대행), where Kurly holds and ships the shipper''s stock, covering goods master, inbound receiving, inventory and ledgers, outbound orders and fulfillment plans; delivery agency (배송대행), where the shipper ships from their own warehouse over Kurly''s Nextmile last-mile network; and shared delivery tracking. Access is contract-gated — clientId and secretKey are issued only after IP allowlist registration — and Kurly states as policy that KLS does not push data to external systems, so integrations poll rather than subscribe to webhooks.'
image: https://res.kurly.com/icons/favicon-192x192.png
layout: provider
modified: '2026-07-19'
name: Kurly
nav: Providers
network: true
overview: 'Kurly publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Authentication API, 배송운영 정책 API, and Delivery Tracking (배송추적) API. Tagged areas include Company, Technology, Logistics, Fulfillment, and Supply Chain.


  The Kurly catalog on APIs.io includes 1 Spectral governance ruleset.


  Kurly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, developer console, and 27 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Kurly Rate Limits
  slug: kurly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Kurly API Rules
  rule_count: 59
  severity_counts:
    error: 54
    hint: 0
    info: 2
    warn: 3
  slug: kurly-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 49.5
    catalog_earned_first_party: 5.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 33.3
    contract_quality: 46.9
    developer_ergonomics: 31.5
    discoverability: 78.6
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kurly/kurly-2026-07-25T224336.png
security:
- kind: authentication
  name: Kurly Authentication
  slug: kurly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kurly Domain Security
  slug: kurly-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: Send outbound orders to a Kurly fulfillment centre
  slug: kurly-fulfillment-order
- name: Book and track a Kurly inbound receiving request
  slug: kurly-inbound-receiving
- name: Register a Kurly delivery-agency order safely
  slug: kurly-register-delivery-order
- name: Track a Kurly Nextmile shipment
  slug: kurly-track-shipment
slug: kurly
tags:
- Company
- Technology
- Logistics
- Fulfillment
- Supply Chain
- Delivery
- E-Commerce
- Grocery
- Shipping
- Order Management
- Inventory
- Tracking
- South Korea
website: https://kurly.com
---
