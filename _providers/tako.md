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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Tako Agentic Access
  operation_count: 13
  slug: tako-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: The agent API from Tako — 4 operation(s) for agent.
  name: Tako agent API
  slug: tako-agent-api
- description: The tako API from Tako — 7 operation(s) for tako.
  name: Tako tako API
  slug: tako-tako-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Knowledge Search agent API
  slug: open-tako-agent-api
- collection_type: open
  name: Knowledge Search agent tako API
  slug: open-tako-tako-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tako.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tako.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tako.com/api-reference/search-v3
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tako.com/documentation/getting-started/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://tako.com/console/api-keys
- group: commercial
  title: ''
  type: Pricing
  url: https://tako.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://tako.com/blog
- group: other
  title: ''
  type: Playground
  url: https://tako.com/playground
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tako.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tako.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://docs.tako.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tako-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tako-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tako-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tako-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tako-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tako-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tako-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tako-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tako-finops.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tako-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tako-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tako-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tako-openapi-overlay.yaml
- group: design
  title: ''
  type: Components
  url: components/tako-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tako-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/tako-api-catalog.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tako-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tako-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tako is an AI answer-engine API for authoritative, source-grounded data. It serves live financial, macroeconomic, and company data as cited answers, structured knowledge cards (charts, tables, maps), and embeddable visualizations for agents and applications. Developers build with four core APIs — Search (fast structured knowledge cards with no LLM in the loop), Answer (a single written, cited response), Contents (the exact numbers behind a card, as CSV), and Agent (asynchronous deep research runs) — plus a Data Graph for discovering what data exists, and Thin-Viz for turning your own data into embeddable Tako cards. Tako pulls from authoritative government, academic, think-tank, and licensed providers (S&P Global, SimilarWeb, YouGov, NOAA) — not scraped web content. It publishes an OpenAPI 3.1 spec, an official hosted MCP server, Python and TypeScript SDKs, an installable Agent Skill, an llms.txt, a Machine Payments Protocol surface, and emphasizes zero data retention, SOC 2
  compliance, and guaranteed SLAs. Surfaced as a portfolio company of Ribbit Capital.
finops:
- name: Tako Finops
  service_category: ''
  slug: tako-finops
image: https://tako.com/apple-touch-icon
layout: provider
mcp_servers:
- description: ''
  name: Tako MCP Server
  slug: tako-mcp-server
modified: '2026-07-21'
name: Tako
nav: Providers
network: true
overview: 'Tako publishes 2 APIs on the [APIs.io](https://apis.io/) network: agent API and tako API. Tagged areas include Company, Artificial Intelligence, Data, Search, and Answer Engine.


  Tako''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 23 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 1
  name: Tako Rate Limits
  slug: tako-rate-limits
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 21
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 75.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tako/refs/heads/main/screenshots/tako-2026-08-17T082243.png
security:
- kind: authentication
  name: Tako Authentication
  slug: tako-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tako Domain Security
  slug: tako-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tako
tags:
- Company
- Artificial Intelligence
- Data
- Search
- Answer Engine
- Financial Data
- Knowledge Graph
- Agents
- MCP
- Data Visualization
website: https://docs.tako.com
---
