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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 74.0
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trucksmarter Agentic Access
  operation_count: 2
  slug: trucksmarter-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Post, update, and remove freight loads on the TruckSmarter load board.
  name: TruckSmarter Loads API
  slug: trucksmarter-loads-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Post a batch of freight loads to the TruckSmarter load board via the partner Load Posting API, then remove them by loadId once they are covered or cancelled.
  name: Post loads to TruckSmarter and remove them once covered
  slug: trucksmarter-post-and-remove-loads
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.trucksmarter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://trucksmarter.notion.site/TruckSmarter-API-Load-Posting-Documentation-2014aa4e9bc580fe80cfe87e18516dea
- group: docs
  title: ''
  type: APIReference
  url: https://trucksmarter.notion.site/TruckSmarter-API-Load-Posting-Documentation-2014aa4e9bc580fe80cfe87e18516dea
- group: operate
  title: ''
  type: Support
  url: https://help.trucksmarter.com/
- group: company
  title: ''
  type: Blog
  url: https://www.trucksmarter.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trucksmarter.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trucksmarter.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trucksmarter.com/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.trucksmarter.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.trucksmarter.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TruckSmarter
- group: auth
  title: ''
  type: Authentication
  url: authentication/trucksmarter-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trucksmarter-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trucksmarter-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trucksmarter-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/trucksmarter-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trucksmarter-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trucksmarter-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trucksmarter-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trucksmarter-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/trucksmarter-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/trucksmarter-post-and-remove-loads.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trucksmarter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trucksmarter-domain-security.yml
created: '2026-07-17'
description: TruckSmarter is a free load board and AI dispatch platform for truck drivers and owner operators, surfacing 100K+ daily available loads with no subscription fees, alongside fuel savings and factoring services and a chat-based AI dispatcher (Dispatch). Brokers post loads and book carriers through a broker portal, CSV/Excel upload, or the partner Load Posting API, which lets partners programmatically create, update, and remove freight loads using a Bearer API key.
image: https://framerusercontent.com/images/NWzlselGeh333d7PEqt7C8Ap9Mg.png
layout: provider
mcp_servers:
- description: ''
  name: TruckSmarter MCP server (candidate, derived — none published)
  slug: trucksmarter-mcp-server-candidate-derived-none-published
modified: '2026-07-21'
name: TruckSmarter
nav: Providers
network: true
overview: 'TruckSmarter publishes 1 API on the [APIs.io](https://apis.io/) network: Loads API. Tagged areas include Trucking, Freight, Logistics, Load Board, and Transportation.


  TruckSmarter''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 43.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.9
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 43.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Trucksmarter Authentication
  slug: trucksmarter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trucksmarter Domain Security
  slug: trucksmarter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trucksmarter
tags:
- Trucking
- Freight
- Logistics
- Load Board
- Transportation
- Dispatch
- Fuel
- Factoring
website: https://www.trucksmarter.com/
---
