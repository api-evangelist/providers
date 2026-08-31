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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Parade Agentic Access
  operation_count: 13
  slug: parade-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 3
apis:
- description: The Available Trucks API from Parade — 1 operation(s) for available trucks.
  name: Parade Available Trucks API
  slug: parade-available-trucks-api
- description: The Bookings API from Parade — 3 operation(s) for bookings.
  name: Parade Bookings API
  slug: parade-bookings-api
- description: The Carrier Onboarding Status API from Parade — 2 operation(s) for carrier onboarding status.
  name: Parade Carrier Onboarding Status API
  slug: parade-carrier-onboarding-status-api
- description: The Carrier Synchronization API from Parade — 1 operation(s) for carrier synchronization.
  name: Parade Carrier Synchronization API
  slug: parade-carrier-synchronization-api
- description: The Digital Conversion API from Parade — 1 operation(s) for digital conversion.
  name: Parade Digital Conversion API
  slug: parade-digital-conversion-api
- description: The Load Synchronization API from Parade — 1 operation(s) for load synchronization.
  name: Parade Load Synchronization API
  slug: parade-load-synchronization-api
- description: The Quotes API from Parade — 3 operation(s) for quotes.
  name: Parade Quotes API
  slug: parade-quotes-api
- description: The Search API from Parade — 1 operation(s) for search.
  name: Parade Search API
  slug: parade-search-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Parade Transactions Available Trucks API
  slug: open-parade-available-trucks-api
- collection_type: open
  name: Parade Transactions Available Trucks Bookings API
  slug: open-parade-bookings-api
- collection_type: open
  name: Parade Transactions Available Trucks Carrier Onboarding Status API
  slug: open-parade-carrier-onboarding-status-api
- collection_type: open
  name: Parade Transactions Available Trucks Carrier Synchronization API
  slug: open-parade-carrier-synchronization-api
- collection_type: open
  name: Parade Transactions Available Trucks Digital Conversion API
  slug: open-parade-digital-conversion-api
- collection_type: open
  name: Parade Transactions Available Trucks Load Synchronization API
  slug: open-parade-load-synchronization-api
- collection_type: open
  name: Parade Transactions Available Trucks Quotes API
  slug: open-parade-quotes-api
- collection_type: open
  name: Parade Transactions Available Trucks Search API
  slug: open-parade-search-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/parade-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://parade.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.syndication.parade.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syndication.parade.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syndication.parade.ai/
- group: company
  title: ''
  type: Blog
  url: https://blog.parade.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.parade.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iubenda.com/terms-and-conditions/86638042
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parade.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/parade-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parade-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parade-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parade-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parade-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parade-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/parade-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: openapi/_original/parade-partner-webhooks-openapi.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parade-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parade-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/parade-digital-transactions-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parade-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parade-domain-security.yml
created: '2026-07-17'
description: Parade is an AI-powered capacity-management and carrier-access platform for freight brokers. It layers on top of a broker's existing Transportation Management System (TMS) and load boards to surface truck availability, syndicate loads to third-party loadboards and carriers, and digitally transact quotes and bookings. Parade's syndication APIs let integration partners search available loads, submit carrier quotes, book loads (Book Now), post available trucks, check carrier onboarding status, and receive digital-conversion and carrier-sync webhooks. Its CoDriver AI agent handles inbound carrier calls and emails. Parade is backed by Menlo Ventures and serves freight brokerages that have collectively transacted tens of billions of dollars in freight.
image: https://www.parade.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Parade MCP Server
  slug: parade-mcp-server
modified: '2026-07-20'
name: Parade
nav: Providers
network: true
overview: 'Parade publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Available Trucks API, Bookings API, Carrier Onboarding Status API, and 5 more. Tagged areas include Company, Freight, Logistics, Trucking, and Supply Chain.


  Parade''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, sandbox, and 17 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.1
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 36.9
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parade/refs/heads/main/screenshots/parade-2026-08-07T191355.png
security:
- kind: authentication
  name: Parade Authentication
  slug: parade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parade Domain Security
  slug: parade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parade
tags:
- Company
- Freight
- Logistics
- Trucking
- Supply Chain
- Capacity Management
- Freight Brokerage
- Transportation
- Load Board
- Artificial Intelligence
website: https://parade.ai
---
