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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The org audit shortcut.
  name: Salesgraph Audit API
  slug: salesgraph-audit-api
- description: The command catalog and synchronous/asynchronous command execution.
  name: Salesgraph Commands API
  slug: salesgraph-commands-api
- description: Polling asynchronous audit runs.
  name: Salesgraph Runs API
  slug: salesgraph-runs-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesgraph-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.salesgraph.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.salesgraph.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.salesgraph.com/reference/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.salesgraph.com/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesgraph-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/salesgraph-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/salesgraph-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/salesgraph-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/salesgraph-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/salesgraph-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/salesgraph-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/salesgraph-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/salesgraph-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://salesgraph.com/support
- group: company
  title: ''
  type: Blog
  url: https://salesgraph.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://salesgraph.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://salesgraph.com/privacy
created: '2026-07-17'
description: 'Salesgraph is a Y Combinator-backed revenue automation platform that uses proactive AI agents to accelerate enterprise sales cycles — automating pre-call research, discovery analysis, follow-up communications, and collateral generation (business cases, mutual action plans, ROI calculators) from a shared organizational context graph. Beyond the product, Salesgraph ships a developer surface: a published MCP (Model Context Protocol) streamable-HTTP server at salesgraph.com/api/mcp and an equivalent REST API under /api/v1, both API-key authenticated, exposing GTM research and audit tools (research, competitors, gtm_audit, org_audit) that return cited markdown. It integrates with Salesforce, HubSpot, Attio, Outreach, Salesloft, Gong, and others, targeting mid-market and enterprise revenue teams in dev tools, SaaS, and cybersecurity.'
image: https://salesgraph.com/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: salesgraph-mcp.yml
  slug: salesgraph-mcpyml
modified: '2026-07-21'
name: Salesgraph
nav: Providers
network: true
overview: 'Salesgraph publishes 3 APIs on the [APIs.io](https://apis.io/) network: Audit API, Commands API, and Runs API. Tagged areas include Company, Sales, Revenue Automation, Go-To-Market, and AI Agents.


  Salesgraph''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 12 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 16.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 33.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Salesgraph Authentication
  slug: salesgraph-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Salesgraph Domain Security
  slug: salesgraph-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: salesgraph
tags:
- Company
- Sales
- Revenue Automation
- Go-To-Market
- AI Agents
- MCP
- Sales Intelligence
- Competitive Intelligence
- Research
- Enterprise Sales
website: https://docs.salesgraph.com
---
