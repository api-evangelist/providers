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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Kurly Agentic Access
  operation_count: 33
  slug: kurly-agentic-access
  summary_line: 33 operations · 22 acting
api_count: 4
apis:
- description: The Authentication API from Kurly — 1 operation(s) for authentication.
  name: Kurly Authentication API
  slug: kurly-authentication-api
- description: The 배송운영 정책 API from Kurly — 26 operation(s) for 배송운영 정책.
  name: Kurly 배송운영 정책 API
  slug: kurly-default-api
- description: The Delivery Tracking (배송추적) API from Kurly — 1 operation(s) for delivery tracking (배송추적).
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
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kurly-capability-edges.yml
- group: other
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
  title: ''
  type: Authentication
  url: authentication/kurly-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kurly-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kurly-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kurly-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kurly-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kurly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kurly-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kurly-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kurly-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kurly-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kurly-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kurly-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.kurly.com/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/kurly-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kurly-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kurly-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kurly-well-known.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kurly-delivery-order-to-tracking.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kurly-inbound-receiving-flow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/kurly-fulfillment-order-flow.yml
created: '2026-07-17'
description: 'Kurly (컬리, operated by The Farmers Front) is a South Korean online grocery and lifestyle commerce company, known for Market Kurly and its overnight "dawn delivery" (샛별배송) model built on a cold-chain fulfillment network. Kurly Logistics Services (KLS) opens that network to contracted shipper clients (화주사) as a B2B Open API spanning three service families: fulfillment (물류대행), where Kurly holds and ships the shipper''s stock, covering goods master, inbound receiving, inventory and ledgers, outbound orders and fulfillment plans; delivery agency (배송대행), where the shipper ships from their own warehouse over Kurly''s Nextmile last-mile network; and shared delivery tracking. Access is contract-gated — clientId and secretKey are issued only after IP allowlist registration — and Kurly states as policy that KLS does not push data to external systems, so integrations poll rather than subscribe to webhooks.'
image: https://res.kurly.com/icons/favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP tool surface (derived, not published by Kurly)
  slug: candidate-mcp-tool-surface-derived-not-published-by-kurly
modified: '2026-07-19'
name: Kurly
nav: Providers
network: true
overview: 'Kurly publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, 배송운영 정책 API, and Delivery Tracking (배송추적) API. Tagged areas include Company, Technology, Logistics, Fulfillment, and Supply Chain.


  Kurly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, developer console, and 26 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 0
  name: Kurly Rate Limits
  slug: kurly-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 19.7
    contract_quality: 50.3
    developer_ergonomics: 31.5
    discoverability: 81.5
    governance: 19.7
    operational_transparency: 18.4
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kurly/refs/heads/main/screenshots/kurly-2026-07-25T224336.png
security:
- kind: authentication
  name: Kurly Authentication
  slug: kurly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kurly Domain Security
  slug: kurly-domain-security
  summary_line: TLSv1.3 · DMARC
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
