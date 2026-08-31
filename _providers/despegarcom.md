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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: Hotel search, live availability, prebook, payment, booking and static content.
  name: Despegar B2B Hotels API
  slug: despegar-b2b-hotels-api
- description: Flight search, prebook, payment, ticket issuing and after-sales.
  name: Despegar B2B Flights API
  slug: despegar-b2b-flights-api
- description: Search and purchase of tours and activities (tickets).
  name: Despegar B2B Activities API
  slug: despegar-b2b-activities-api
- description: Post-sale cancellation, rescheduling and special-request flows.
  name: Despegar After-Sales API
  slug: despegar-after-sales-api
- description: Geographic data and static content (cities, countries, airports, hotel inventory, amenities).
  name: Despegar Common Assets API
  slug: despegar-common-assets-api
artifact_total: 10
asyncapis:
- description: ''
  name: Despegarcom Communication Webhooks
  slug: despegarcom-communication-webhooks
common:
- group: company
  title: ''
  type: Website
  url: http://www.despegar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.despegar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.despegar.com/docs/ecosystem
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.despegar.com/reference/createprebook-1
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.despegar.com/docs/ecosystem
- group: operate
  title: ''
  type: Support
  url: https://api-docs.despegar.com/docs/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/despegar
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/despegarcom-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/despegarcom-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/despegarcom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/despegarcom-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/despegarcom-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/despegarcom-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/despegarcom-communication-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/despegarcom-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/despegarcom-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/despegarcom-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/despegarcom-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/despegarcom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/despegarcom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/despegarcom-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/despegarcom-hotel-search-and-book.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/despegarcom-flight-search-and-book.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/despegarcom-cancel-reservation.md
created: '2026-07-17'
description: 'Despegar.com (NYSE: DESP) is the leading online travel company in Latin America, operating the consumer brands Despegar and Decolar alongside the B2B HotelDo / BestDay distribution network. Its B2B travel API lets partners integrate hotels, flights and activities into their own systems, covering the full search, prebook, payment, booking and after-sales (cancellation, rescheduling, special requests) flows, plus geographic and static-content services, push-based event webhooks, a Rewards loyalty API, and an mTLS Security API for B2B transactions. Despegar also publishes official hosted MCP servers for agent-based flight and hotel search, and an llms.txt index of its developer documentation.'
image: https://files.readme.io/45785f4-brandmark-blue.svg
layout: provider
mcp_servers:
- description: Despegar publishes official hosted MCP (Model Context Protocol) servers for its B2B travel API, exposing flight and hotel search/cart tools over JSON-RPC HTTP. Authentication is handled server-side vi
  name: Despegar.com MCP Server
  slug: despegarcom-mcp-server
modified: '2026-07-18'
name: Despegar.com
nav: Providers
network: true
overview: 'Despegar.com publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Travel, Hotels, and Flights.


  The Despegar.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Despegar.com''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 32.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/despegarcom/refs/heads/main/screenshots/despegarcom-2026-07-25T211800.png
security:
- kind: authentication
  name: Despegarcom Authentication
  slug: despegarcom-authentication
  summary_line: apiKey/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Despegarcom Domain Security
  slug: despegarcom-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Despegarcom Vulnerability Disclosure
  slug: despegarcom-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: despegarcom
tags:
- Company
- Consumer
- Travel
- Hotels
- Flights
- Activities
- Booking
- Latin America
- B2B
- MCP
- Webhook
website: http://www.despegar.com/
---
