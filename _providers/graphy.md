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
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-03'
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
artifact_total: 5
common:
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
  name: graphy-mcp.yml
  slug: graphy-mcpyml
modified: '2026-07-19'
name: Graphy
nav: Providers
network: true
overview: 'Graphy publishes 1 API on the [APIs.io](https://apis.io/) network: Agents API. Tagged areas include Company, Data Visualization, Charts, Charting, and Analytics.


  Graphy''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, sandbox, and 21 more developer resources.'
random_paper: 81
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.1
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 53.4
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
  schema_version: 0.9
  scored_at: '2026-08-03'
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
