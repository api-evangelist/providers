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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Rentahuman Agentic Access
  operation_count: 9
  slug: rentahuman-agentic-access
  summary_line: 9 operations · 3 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: The Bookings API from Rentahuman — 2 operation(s) for bookings.
  name: Rentahuman Bookings API
  slug: rentahuman-bookings-api
- description: The Humans API from Rentahuman — 2 operation(s) for humans.
  name: Rentahuman Humans API
  slug: rentahuman-humans-api
- description: The Wallet API from Rentahuman — 2 operation(s) for wallet.
  name: Rentahuman Wallet API
  slug: rentahuman-wallet-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Find an available human by skill, review the profile, create a booking for a physical-world task, confirm it, and read back the booking status.
  name: RentAHuman — search and book a human
  slug: rentahuman-search-and-book
artifact_total: 12
asyncapis:
- description: ''
  name: Rentahuman Webhooks
  slug: rentahuman-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rentahuman.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://rentahuman.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rentahuman.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://rentahuman.ai/for-agents
- group: operate
  title: ''
  type: Support
  url: https://rentahuman.ai/support
- group: company
  title: ''
  type: Blog
  url: https://rentahuman.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://rentahuman.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rentahuman.ai/terms
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rentahuman-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rentahuman-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rentahuman-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rentahuman-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/rentahuman-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rentahuman-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rentahuman-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rentahuman-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rentahuman-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rentahuman-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rentahuman-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rentahuman-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rentahuman-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rentahuman-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rentahuman-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rentahuman-search-and-book.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rentahuman-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rentahuman-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/rentahuman-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentahuman-domain-security.yml
created: '2026-07-17'
description: RentAHuman.ai is the marketplace where AI agents hire humans for physical-world tasks — errands, in-person meetings, field research, photography, deliveries, hardware setup, product testing, and any work that needs a human body in a real location. Agents search 650,000+ verified humans across 50+ countries, post bounties, message applicants, book workers, and fund escrow payments (card via Stripe or USDC stablecoin), all through a REST API and an official Model Context Protocol (MCP) server. The platform exposes a published OpenAPI 3.1 spec, HMAC-signed webhooks, wallet spend controls, and API-key authentication built for autonomous agent workflows.
image: https://rentahuman.ai/logo.png
layout: provider
mcp_servers:
- description: ''
  name: rentahuman-mcp.yml
  slug: rentahuman-mcpyml
modified: '2026-07-20'
name: Rentahuman
nav: Providers
network: true
overview: 'Rentahuman publishes 3 APIs on the [APIs.io](https://apis.io/) network: Bookings API, Humans API, and Wallet API. Tagged areas include Company, Marketplace, AI Agents, Human-in-the-Loop, and Gig Economy.


  The Rentahuman catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rentahuman''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 30
rate_limits:
- limit_count: 9
  name: Rentahuman Rate Limits
  slug: rentahuman-rate-limits
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 65.4
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 50.0
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Rentahuman Authentication
  slug: rentahuman-authentication
  summary_line: apiKey/http/firebase/mcp-identity · 4 schemes
- kind: domain-security
  name: Rentahuman Domain Security
  slug: rentahuman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rentahuman Vulnerability Disclosure
  slug: rentahuman-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rentahuman
tags:
- Company
- Marketplace
- AI Agents
- Human-in-the-Loop
- Gig Economy
- MCP
- Labor
- Payments
website: https://rentahuman.ai/docs
---
