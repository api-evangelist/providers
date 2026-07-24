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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 75.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Tickitto Agentic Access
  operation_count: 22
  slug: tickitto-agentic-access
  summary_line: 22 operations · 12 acting
api_count: 8
apis:
- description: The Authentication API from Tickitto — 1 operation(s) for authentication.
  name: Tickitto Authentication API
  slug: tickitto-authentication-api
- description: The Availability API from Tickitto — 1 operation(s) for availability.
  name: Tickitto Availability API
  slug: tickitto-availability-api
- description: The Basket API from Tickitto — 10 operation(s) for basket.
  name: Tickitto Basket API
  slug: tickitto-basket-api
- description: The Events API from Tickitto — 2 operation(s) for events.
  name: Tickitto Events API
  slug: tickitto-events-api
- description: The Metadata API from Tickitto — 1 operation(s) for metadata.
  name: Tickitto Metadata API
  slug: tickitto-metadata-api
- description: The Search API from Tickitto — 2 operation(s) for search.
  name: Tickitto Search API
  slug: tickitto-search-api
- description: The System Status API from Tickitto — 1 operation(s) for system status.
  name: Tickitto System Status API
  slug: tickitto-system-status-api
- description: The Webhooks API from Tickitto — 2 operation(s) for webhooks.
  name: Tickitto Webhooks API
  slug: tickitto-webhooks-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a basket, search inventory, fetch availability, add a ticket, and check out.
  name: Tickitto — Search to Checkout
  slug: tickitto-search-to-checkout
artifact_total: 15
asyncapis:
- description: ''
  name: Tickitto Webhooks
  slug: tickitto-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tickitto.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tickitto.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tickitto.com/key-principles/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/tickitto-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tickitto-agentic-access.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tickitto-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tickitto-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tickitto-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tickitto-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tickitto-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/tickitto-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tickitto-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tickitto-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tickitto-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tickitto-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tickitto-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tickitto-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tickitto-search-to-checkout.yml
- group: company
  title: ''
  type: Blog
  url: https://tickitto.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tickitto.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tickitto.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://tickitto.com
created: '2026-07-17'
description: 'Tickitto is a London-based B2B ticketing marketplace that lets brands and platforms sell event tickets to their own customers through a single, fully transactional REST API. Its curated inventory spans 90,000+ events globally, mixing one-off sporting and music events with ongoing experiences, attractions, and tours. Tickitto positions itself as a marketplace rather than a channel manager: distributors keep their customer relationship and data while Tickitto tracks commission through a real-time dashboard. The API is availability-aware, organised around events, availability instances, and baskets, and ships an embeddable, white-labelable Ticket Selection Widget that renders event-specific UI (interactive seating maps, calendar dates, and time slots) so integrators avoid orchestrating multiple calls or building bespoke selection front-ends. Tickitto is backed by Seedcamp.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tickitto.png
layout: provider
mcp_servers:
- description: ''
  name: tickitto-mcp.yml
  slug: tickitto-mcpyml
modified: '2026-07-21'
name: Tickitto
nav: Providers
network: true
overview: 'Tickitto publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Availability API, Basket API, and 5 more. Tagged areas include Company, Ticketing, Events, Marketplace, and Travel & Experiences.


  The Tickitto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tickitto''s developer surface includes documentation, API reference, authentication, sandbox, engineering blog, and 18 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 44.5
  delta: 1.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 63.2
    developer_ergonomics: 58.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 42.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Tickitto Authentication
  slug: tickitto-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tickitto Domain Security
  slug: tickitto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tickitto
tags:
- Company
- Ticketing
- Events
- Marketplace
- Travel & Experiences
- Entertainment
- Payments
- Commerce
website: https://tickitto.com
---
