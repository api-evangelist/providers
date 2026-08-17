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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Zayo Agentic Access
  operation_count: 26
  slug: zayo-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 8
apis:
- description: Monitor upcoming outages with Maintenance Cases API. The Zayo Maintenance Cases API is composed of a series of API calls that are intended to be leveraged sequentially with each request/response cycle
  name: Zayo Maintenance Cases API
  slug: zayo-maintenance-cases-api
- description: Grow your footprint by analyzing network availability by utilizing our Building, Locations, and Cloud Providers APIs.
  name: Zayo Network Discovery API
  slug: zayo-network-discovery-api
- description: Grow your footprint by reviewing Zayo products in our Product Catalog API, generating quotes with our Quoting API, and automating the ordering process through the Order API.
  name: Zayo Order API
  slug: zayo-order-api
- description: View available Zayo products and product detials to use in the Quoting API.
  name: Zayo Product Catalog API
  slug: zayo-product-catalog-api
- description: Grow your footprint by reviewing Zayo products in our Product Catalog API, generating quotes with our Quoting API, and automating the ordering process through the Order API.
  name: Zayo Quote API
  slug: zayo-quote-api
- description: Monitor your critical services with our Service Inventory API.
  name: Zayo Service Inventory API
  slug: zayo-service-inventory-api
- description: View available tickets and ticket details to use in the Ticketing API.
  name: Zayo Ticket Catalog API
  slug: zayo-ticket-catalog-api
- description: Create various types of tickets, view all tickets, and create ticket comments.
  name: Zayo Ticketing API
  slug: zayo-ticketing-api
artifact_total: 23
asyncapis:
- description: ''
  name: Zayo Notifications Webhooks
  slug: zayo-notifications-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zayo APIs Maintenance Cases API
  slug: open-zayo-maintenance-cases-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Network Discovery API
  slug: open-zayo-network-discovery-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Order API
  slug: open-zayo-order-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Product Catalog API
  slug: open-zayo-product-catalog-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Quote API
  slug: open-zayo-quote-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Service Inventory API
  slug: open-zayo-service-inventory-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Ticket Catalog API
  slug: open-zayo-ticket-catalog-api
- collection_type: open
  name: Zayo APIs Maintenance Cases Ticketing API
  slug: open-zayo-ticketing-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zayo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zayo-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zayo-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zayo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zayo.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.zayo.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zayo.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/zayo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zayo-conventions.yml
- group: operate
  title: ''
  type: Support
  url: https://developer.zayo.com/docs/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.zayo.com/docs/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zayo.com/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zayo.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://developer.zayo.com/docs/contact
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zayo-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zayo-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zayo-llms.txt
created: '2026-07-17'
description: Zayo is a global communications infrastructure provider operating one of the largest independent fiber networks, delivering bandwidth, dark fiber, wavelengths, ethernet, IP, cloud connectivity and network management to carriers, enterprises, and hyperscalers. Zayo publishes a free public developer program at developer.zayo.com exposing REST APIs for network discovery (building validation, location and cloud-site lookup), quote and order management (product catalog, quoting, ordering), and service management (service inventory, ticketing, and maintenance-case notifications). The APIs are OpenAPI 3.1 described, secured with OAuth 2.0 client-credentials bearer tokens, and include a push-notification/callback surface for maintenance and ticket updates.
image: https://developer.zayo.com/img/zayo-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: zayo-mcp.yml
  slug: zayo-mcpyml
modified: '2026-07-21'
name: Zayo
nav: Providers
network: true
overview: 'Zayo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Maintenance Cases API, Network Discovery API, Order API, and 5 more. Tagged areas include Company, Telecommunications, Networking, Connectivity, and Fiber.


  The Zayo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zayo''s developer surface includes documentation, API reference, getting-started guide, authentication, support, signup flow, and 12 more developer resources.'
random_paper: 4
scopes:
- name: Zayo Scopes
  scope_count: 1
  slug: zayo-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 74.6
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 51.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zayo Authentication
  slug: zayo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zayo Domain Security
  slug: zayo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zayo
tags:
- Company
- Telecommunications
- Networking
- Connectivity
- Fiber
- Infrastructure
- Bandwidth
- Cloud Connectivity
- Ordering
- Ticketing
website: https://developer.zayo.com/
---
