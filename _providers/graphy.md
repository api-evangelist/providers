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
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Graphy Agentic Access
  operation_count: 7
  slug: graphy-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 1
apis:
- description: The Agents API from Graphy — 7 operation(s) for agents.
  name: Graphy Agents API
  slug: graphy-agents-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Graphy AI Agents API
  slug: open-graphy-agents-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/graphy-agents-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/graphy-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://graphy.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://graphy.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.graphy.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.graphy.dev/agents/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.graphy.dev/agents/quickstart
- group: company
  title: ''
  type: Blog
  url: https://graphy.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://graphy.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://graphy.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://graphy.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://graphy.app/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graphy.app/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.graphy.dev/agents/versioning
- group: start
  title: ''
  type: Sandbox
  url: https://playground.graphy.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/graphy-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/graphy-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/graphy-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphy-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/graphy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/graphy-packages.yml
- group: design
  title: ''
  type: Components
  url: components/graphy-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/graphy-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/graphy-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/graphy-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/graphy-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/graphy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/graphy-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Graphy is an AI-powered data visualization platform that turns raw data into presentation-ready charts and interactive data stories. Alongside its no-code chart maker (Google Sheets, CSV and Excel import, AI insights, conversational data chat and 20+ chart types), Graphy ships a developer platform at graphy.dev: an AI Agents API that generates, mutates, annotates, narrates, extracts and deterministically evaluates charts from natural language — streamed as Server-Sent Events — plus a React charting SDK and editor for embedding editable, story-driven data experiences inside your own product. Backed by Seedcamp, Coatue, General Catalyst and Northzone.'
image: https://framerusercontent.com/assets/HQAKsmFxtBCYp0V86Kb4PbbCjx4.png
layout: provider
mcp_servers:
- description: ''
  name: Graphy MCP Server
  slug: graphy-mcp-server
modified: '2026-07-19'
name: Graphy
nav: Providers
network: true
overview: 'Graphy publishes 1 API on the [APIs.io](https://apis.io/) network: Agents API. Tagged areas include Company, Data Visualization, Charts, Charting, and Analytics.


  Graphy''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, sandbox, and 22 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 47.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 59.2
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 47.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphy/refs/heads/main/screenshots/graphy-2026-07-25T220250.png
security:
- kind: authentication
  name: Graphy Authentication
  slug: graphy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Graphy Domain Security
  slug: graphy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: graphy
tags:
- Company
- Data Visualization
- Charts
- Charting
- Analytics
- Artificial Intelligence
- Data Storytelling
- Developer Tools
- SDK
- Agents
website: https://graphy.app
---
