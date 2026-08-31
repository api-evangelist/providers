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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Cabify Agentic Access
  operation_count: 46
  slug: cabify-agentic-access
  summary_line: 46 operations · 21 acting
api_count: 2
apis:
- description: Operations for managing the delivery lifecycle. Use these endpoints to trigger a shipment, cancel an active delivery, or check whether a pickup location falls within an operating area.
  name: Cabify delivery API
  slug: cabify-delivery-api
- description: This method returns prices, Id's and all the information for products that are available at the origin point. Before requesting a journey as a first step it is necessary to obtain the different produc
  name: Cabify Estimates API
  slug: cabify-estimates-api
- description: A hub is a physical location (such as a warehouse or store) where parcels are stored until they are ready to be picked up by a driver. You can reference a hub in pickup or drop-off information using i
  name: Cabify hubs API
  slug: cabify-hubs-api
- description: This section covers the mobility solution for all companies looking to transport their employees in a simple, safe and comfortable way. We offer different types of vehicles with private drivers and pr
  name: Cabify Journeys API
  slug: cabify-journeys-api
- description: The label API from Cabify — 1 operation(s) for label.
  name: Cabify label API
  slug: cabify-label-api
- description: Cabify offers to its clients a feature where the client’s employees have to input a journey motive or a project or a dynamic cost center associated with the new journey before requesting it. This is u
  name: Cabify Labels API
  slug: cabify-labels-api
- description: A parcel is the package you need to ship. Each parcel is identified by a unique ID and contains a pickup point (where the driver collects the package) and a drop-off point (the destination). Parcels m
  name: Cabify parcels API
  slug: cabify-parcels-api
- description: Sales objects are created once a journey transitions into the terminated state and they are associated with the user who requested the journey (which not necessarily is the rider). <br> <br>The transi
  name: Cabify Sales API
  slug: cabify-sales-api
- description: The shipment API from Cabify — 2 operation(s) for shipment.
  name: Cabify shipment API
  slug: cabify-shipment-api
- description: The shipping_types API from Cabify — 1 operation(s) for shipping_types.
  name: Cabify shipping_types API
  slug: cabify-shipping-types-api
- description: Track the real-time status and location of your parcels at any point during their delivery.
  name: Cabify status API
  slug: cabify-status-api
- description: The users API from Cabify — 4 operation(s) for users.
  name: Cabify users API
  slug: cabify-users-api
- description: Subscribe to event-driven notifications to receive live updates about parcel status changes, location updates, and proof of delivery codes.
  name: Cabify webhooks API
  slug: cabify-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Cabify Webhooks
  slug: cabify-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cabify Logistics delivery API
  slug: open-cabify-delivery-api
- collection_type: open
  name: Cabify Logistics delivery Estimates API
  slug: open-cabify-estimates-api
- collection_type: open
  name: Cabify Logistics delivery hubs API
  slug: open-cabify-hubs-api
- collection_type: open
  name: Cabify Logistics delivery Journeys API
  slug: open-cabify-journeys-api
- collection_type: open
  name: Cabify Logistics delivery label API
  slug: open-cabify-label-api
- collection_type: open
  name: Cabify Logistics delivery Labels API
  slug: open-cabify-labels-api
- collection_type: open
  name: Cabify Logistics delivery parcels API
  slug: open-cabify-parcels-api
- collection_type: open
  name: Cabify Logistics delivery Sales API
  slug: open-cabify-sales-api
- collection_type: open
  name: Cabify Logistics delivery shipment API
  slug: open-cabify-shipment-api
- collection_type: open
  name: Cabify Logistics delivery shipping_types API
  slug: open-cabify-shipping-types-api
- collection_type: open
  name: Cabify Logistics delivery status API
  slug: open-cabify-status-api
- collection_type: open
  name: Cabify Logistics delivery users API
  slug: open-cabify-users-api
- collection_type: open
  name: Cabify Logistics delivery webhooks API
  slug: open-cabify-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cabify-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cabify-logistics-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cabify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cabify.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cabify.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cabify.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cabify.com/reference/createjourney
- group: auth
  title: ''
  type: Authentication
  url: authentication/cabify-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cabify-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cabify-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cabify-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cabify-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://cabify.statuspage.io
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cabify-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cabify-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cabify-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cabify-security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/cabify-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cabify-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cabify-operation-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cabify-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cabify-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cabify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cabify-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cabify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cabify.com/.well-known/security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cabify
- group: operate
  title: ''
  type: Support
  url: https://developers.cabify.com/page/cabify-api-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cabify.com/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cabify.com/en/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://cabify.com/app
created: '2026-07-17'
description: 'Cabify is a Spanish multi-mobility company founded in 2011 and headquartered in Madrid, operating ride-hailing, corporate mobility, and last-mile logistics across Spain and Latin America (6+ countries and 40+ cities). Its public developer platform exposes two authenticated REST APIs: a Ride-Hailing API (v4) for price estimation, journey booking, real-time state tracking, rider and label management, and sales reporting; and a Logistics API (v1) for creating, shipping, tracking, and configuring proof of delivery for parcels, including ecommerce integrations with Shopify, Tiendanube, and VTEX. Both APIs authenticate with OAuth2 client-credentials access tokens (Bearer), publish independent sandbox environments, and deliver asynchronous updates via webhooks.'
image: https://cabify.com/static/head/cover.png
layout: provider
mcp_servers:
- description: ''
  name: Cabify MCP Server
  slug: cabify-mcp-server
modified: '2026-07-18'
name: Cabify
nav: Providers
network: true
overview: 'Cabify publishes 13 APIs on the [APIs.io](https://apis.io/) network, including delivery API, Estimates API, hubs API, and 10 more. Tagged areas include Company, Transportation, Ride Hailing, Mobility, and Logistics.


  The Cabify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cabify''s developer surface includes documentation, getting-started guide, API reference, authentication, sandbox, changelog, support, and 25 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 65.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cabify/refs/heads/main/screenshots/cabify-2026-07-25T204159.png
security:
- kind: authentication
  name: Cabify Authentication
  slug: cabify-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cabify Domain Security
  slug: cabify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cabify Vulnerability Disclosure
  slug: cabify-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cabify
tags:
- Company
- Transportation
- Ride Hailing
- Mobility
- Logistics
- Delivery
- Last Mile Delivery
- Webhook
- Authentication
website: https://cabify.com
---
