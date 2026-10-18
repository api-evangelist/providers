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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing addresses for customers and organizations
  name: Phasio Addresses API
  slug: phasio-addresses-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Read storefront carts, a single cart, and a cart's pre-order (quote and purchasability).
  name: Phasio Cart Resource API
  slug: phasio-cart-resource-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturer activities and conversations
  name: Phasio Manufacturer Activity Controller API
  slug: phasio-manufacturer-activity-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Programmatic analytics endpoints for retrieving manufacturer dashboard metrics, funnel performance, revenue, production, customer and material insights.
  name: Phasio Manufacturer Analytics Controller API
  slug: phasio-manufacturer-analytics-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing assemblies
  name: Phasio Manufacturer Assembly Controller API
  slug: phasio-manufacturer-assembly-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for exporting CAMSPEC files and managing manifest mappings
  name: Phasio Manufacturer CAMSPEC Controller API
  slug: phasio-manufacturer-camspec-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing cart items
  name: Phasio Manufacturer Cart Item Controller API
  slug: phasio-manufacturer-cart-item-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturer catalog items
  name: Phasio Manufacturer Catalog Controller API
  slug: phasio-manufacturer-catalog-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for retrieving color options for manufactured parts
  name: Phasio Manufacturer Color Controller API
  slug: phasio-manufacturer-color-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing customer records and operations
  name: Phasio Manufacturer Customer Controller API
  slug: phasio-manufacturer-customer-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing customer organizations
  name: Phasio Manufacturer Customer Organisation Controller API
  slug: phasio-manufacturer-customer-organisation-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for generating and downloading various document types
  name: Phasio Manufacturer Document Controller API
  slug: phasio-manufacturer-document-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing document templates for invoices, orders, and consignment labels
  name: Phasio Manufacturer Document Template Controller API
  slug: phasio-manufacturer-document-template-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing 3D printing infill options and configurations
  name: Phasio Manufacturer Infill Controller API
  slug: phasio-manufacturer-infill-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing Kanban board columns for order processing workflow
  name: Phasio Manufacturer Kanban Column Controller API
  slug: phasio-manufacturer-kanban-column-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturing materials
  name: Phasio Manufacturer Material Controller API
  slug: phasio-manufacturer-material-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing part geometry revisions and 3D file analysis
  name: Phasio Manufacturer Part Revision Controller API
  slug: phasio-manufacturer-part-revision-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing part specifications and customer article references
  name: Phasio Manufacturer Part Specification Controller API
  slug: phasio-manufacturer-part-specification-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing post-processing options for manufactured parts
  name: Phasio Manufacturer Post Processing Controller API
  slug: phasio-manufacturer-post-processing-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing precision prices for manufacturing operations
  name: Phasio Manufacturer Precision Prices Controller API
  slug: phasio-manufacturer-precision-prices-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturing process pricing configurations
  name: Phasio Manufacturer Process Prices Controller API
  slug: phasio-manufacturer-process-prices-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing production steps in the manufacturing workflow
  name: Phasio Manufacturer Production Step Controller API
  slug: phasio-manufacturer-production-step-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing part requisitions and production batches
  name: Phasio Manufacturer Requisition Controller API
  slug: phasio-manufacturer-requisition-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Manage routing templates on a part specification
  name: Phasio Manufacturer Routing Template Controller API
  slug: phasio-manufacturer-routing-template-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing files attached to threads
  name: Phasio Manufacturer Thread File Controller API
  slug: phasio-manufacturer-thread-file-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Manage individual work orders, including downstream routing mutations
  name: Phasio Manufacturer Work Order Controller API
  slug: phasio-manufacturer-work-order-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing webhooks
  name: Phasio Webhooks API
  slug: phasio-webhooks-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing manufacturer operator addresses
  name: Phasio Operator Addresses API
  slug: phasio-operator-addresses-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing orders and their lifecycle
  name: Phasio Orders API
  slug: phasio-orders-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Manage payments for orders
  name: Phasio Payments API
  slug: phasio-payments-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Create, replace, and progress shipments on an order
  name: Phasio Shipments API
  slug: phasio-shipments-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for retrieving shipping rates for parts
  name: Phasio Shipping Rates API
  slug: phasio-shipping-rates-api
artifact_total: 71
asyncapis:
- description: ''
  name: Phasio Webhooks
  slug: phasio-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Phasio Addresses API
  slug: open-phasio-addresses-api
- collection_type: open
  name: Phasio Cart Resource API
  slug: open-phasio-cart-resource-api
- collection_type: open
  name: Phasio Manufacturer Activity Controller API
  slug: open-phasio-manufacturer-activity-controller-api
- collection_type: open
  name: Phasio Manufacturer Analytics Controller API
  slug: open-phasio-manufacturer-analytics-controller-api
- collection_type: open
  name: Phasio Manufacturer Assembly Controller API
  slug: open-phasio-manufacturer-assembly-controller-api
- collection_type: open
  name: Phasio Manufacturer CAMSPEC Controller API
  slug: open-phasio-manufacturer-camspec-controller-api
- collection_type: open
  name: Phasio Manufacturer Cart Item Controller API
  slug: open-phasio-manufacturer-cart-item-controller-api
- collection_type: open
  name: Phasio Manufacturer Catalog Controller API
  slug: open-phasio-manufacturer-catalog-controller-api
- collection_type: open
  name: Phasio Manufacturer Color Controller API
  slug: open-phasio-manufacturer-color-controller-api
- collection_type: open
  name: Phasio Manufacturer Customer Controller API
  slug: open-phasio-manufacturer-customer-controller-api
- collection_type: open
  name: Phasio Manufacturer Customer Organisation Controller API
  slug: open-phasio-manufacturer-customer-organisation-controller-api
- collection_type: open
  name: Phasio Manufacturer Document Controller API
  slug: open-phasio-manufacturer-document-controller-api
- collection_type: open
  name: Phasio Manufacturer Document Template Controller API
  slug: open-phasio-manufacturer-document-template-controller-api
- collection_type: open
  name: Phasio Manufacturer Infill Controller API
  slug: open-phasio-manufacturer-infill-controller-api
- collection_type: open
  name: Phasio Manufacturer Kanban Column Controller API
  slug: open-phasio-manufacturer-kanban-column-controller-api
- collection_type: open
  name: Phasio Manufacturer Material Controller API
  slug: open-phasio-manufacturer-material-controller-api
- collection_type: open
  name: Phasio Manufacturer Part Revision Controller API
  slug: open-phasio-manufacturer-part-revision-controller-api
- collection_type: open
  name: Phasio Manufacturer Part Specification Controller API
  slug: open-phasio-manufacturer-part-specification-controller-api
- collection_type: open
  name: Phasio Manufacturer Post Processing Controller API
  slug: open-phasio-manufacturer-post-processing-controller-api
- collection_type: open
  name: Phasio Manufacturer Precision Prices Controller API
  slug: open-phasio-manufacturer-precision-prices-controller-api
- collection_type: open
  name: Phasio Manufacturer Process Prices Controller API
  slug: open-phasio-manufacturer-process-prices-controller-api
- collection_type: open
  name: Phasio Manufacturer Production Step Controller API
  slug: open-phasio-manufacturer-production-step-controller-api
- collection_type: open
  name: Phasio Manufacturer Requisition Controller API
  slug: open-phasio-manufacturer-requisition-controller-api
- collection_type: open
  name: Phasio Manufacturer Routing Template Controller API
  slug: open-phasio-manufacturer-routing-template-controller-api
- collection_type: open
  name: Phasio Manufacturer Thread File Controller API
  slug: open-phasio-manufacturer-thread-file-controller-api
- collection_type: open
  name: Phasio Manufacturer Work Order Controller API
  slug: open-phasio-manufacturer-work-order-controller-api
- collection_type: open
  name: Phasio Operator Addresses API
  slug: open-phasio-operator-addresses-api
- collection_type: open
  name: Phasio Orders API
  slug: open-phasio-orders-api
- collection_type: open
  name: Phasio Payments API
  slug: open-phasio-payments-api
- collection_type: open
  name: Phasio Shipments API
  slug: open-phasio-shipments-api
- collection_type: open
  name: Phasio Shipping Rates API
  slug: open-phasio-shipping-rates-api
- collection_type: open
  name: Phasio Webhooks API
  slug: open-phasio-webhooks-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/plans/phasio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/phasio-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/capabilities/phasio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/phasio-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/overlays/phasio-manufacturer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/phasio-manufacturer-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://phas.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.phas.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phas.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.phas.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phas.io/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://phas.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://phas.io/post
- group: start
  title: ''
  type: SignUp
  url: https://auth.phas.io/create
- group: start
  title: ''
  type: Login
  url: https://app.phas.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phas.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phas.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://phas.io/contact
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/authentication/phasio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/phasio-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/well-known/phasio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/phasio-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/conventions/phasio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/phasio-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/conventions/phasio-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/phasio-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/errors/phasio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/phasio-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/lifecycle/phasio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/phasio-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/data-model/phasio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/phasio-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/conformance/phasio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/phasio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://phas.io/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/security/phasio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/phasio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/security/phasio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/phasio-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/asyncapi/phasio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/phasio-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/mcp/phasio-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/phasio-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/llms/phasio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/phasio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/skills/phasio-create-and-track-order.md
  title: ''
  type: AgentSkill
  url: skills/phasio-create-and-track-order.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/skills/phasio-subscribe-to-webhooks.md
  title: ''
  type: AgentSkill
  url: skills/phasio-subscribe-to-webhooks.md
created: '2026-07-17'
description: Phasio is an operating platform for manufacturing service providers that unifies intelligent quoting, production operations, connected back-office/ERP integration, part intelligence, and white-labeled customer storefronts. It serves contract manufacturers across additive manufacturing, CNC machining, and injection molding, generating CAD-based quotes in seconds and managing shop-floor routing and scheduling. The Phasio Manufacturer REST API (v1, base /api/manufacturer/v1) is published as an OpenAPI 3.2 contract of 130 operations across 32 resource groups covering orders, carts, customers and customer organisations, addresses, part revisions and specifications, requisitions and work orders, production steps and routing templates, documents, payments, shipments and shipping rates, and webhooks, authenticated with a Bearer API key created under Settings > API Keys.
image: https://phas.io/icon.svg
layout: provider
modified: '2026-10-06'
name: Phasio
nav: Providers
network: true
overview: 'Phasio publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Cart Resource API, Manufacturer Activity Controller API, and 29 more. Tagged areas include Company, Manufacturing, 3D Printing, CNC Machining, and Quoting.


  The Phasio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Phasio''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, support, and 24 more developer resources.'
plans:
- name: Phasio Plans Pricing
  plan_count: 2
  slug: phasio-plans-pricing
- name: Phasio Price Estimates
  plan_count: 0
  slug: phasio-price-estimates
random_paper: 6
score:
  band: strong
  composite: 58.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 58.7
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 57.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 32
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/screenshots/phasio-2026-08-17T081204.png
security:
- kind: authentication
  name: Phasio Authentication
  slug: phasio-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Phasio Domain Security
  slug: phasio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Phasio Trust Center
  slug: phasio-trust-center
  summary_line: SOC 2, GDPR
slug: phasio
tags:
- Company
- Manufacturing
- 3D Printing
- CNC Machining
- Quoting
- Production Operations
- Manufacturing Execution
website: https://phas.io
---
