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
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.5
  scored_at: '2026-08-19'
api_count: 6
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
- description: The Opportunity Management System — query the organization's own visible sales objects, traverse their relationships, inspect where each value came from, and manage continuous, cost-capped research wa
  name: Salesgraph OMS API
  slug: salesgraph-oms-api
- description: A public, unauthenticated JSON status endpoint at /api/status carrying the platform headline, overall status, active incident count, a seven-component health array with per-component lastCheckedAt tim
  name: Salesgraph Status API
  slug: salesgraph-status-api
- description: The remote MCP streamable-HTTP server at salesgraph.com/api/mcp, authenticated with an sg_live_ API key. It exposes 19 documented tools across three families — GTM commands (research, competitors, gtm
  name: Salesgraph MCP Server
  slug: salesgraph-mcp-server
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesgraph REST Audit API
  slug: open-salesgraph-audit-api
- collection_type: open
  name: Salesgraph REST Audit Commands API
  slug: open-salesgraph-commands-api
- collection_type: open
  name: Salesgraph REST OMS API
  slug: open-salesgraph-oms-api
- collection_type: open
  name: Salesgraph REST Audit Runs API
  slug: open-salesgraph-runs-api
- collection_type: open
  name: Salesgraph Platform Status API
  slug: open-salesgraph-status-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/salesgraph-openapi-overlay.yaml
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/salesgraph-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/salesgraph-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/salesgraph-well-known.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/salesgraph-conventions.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://salesgraph.com/status
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salesgraph-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/salesgraph-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/salesgraph-packages.yml
- group: start
  title: ''
  type: Login
  url: https://salesgraph.com/login
created: '2026-07-17'
description: 'Salesgraph is a Y Combinator-backed revenue automation platform that uses proactive AI agents to accelerate enterprise sales cycles — automating pre-call research, discovery analysis, follow-up communications, and collateral generation (business cases, mutual action plans, ROI calculators) from a shared organizational context graph. Beyond the product, Salesgraph ships a developer surface: a published MCP (Model Context Protocol) streamable-HTTP server at salesgraph.com/api/mcp and an equivalent REST API under /api/v1, both API-key authenticated, exposing 19 tools across GTM research and audit commands (research, competitors, gtm_audit, org_audit) that return cited markdown, and an OMS (Opportunity Management System) family that returns JSON — searching, traversing and tracing the provenance of the organization''s own Accounts and Opportunities, and putting cost-capped continuous research watches on them. OMS write intent always routes through a human approval request rather
  than a direct write. It also serves an A2A agent card and a packaged Agent Skill from its docs host, and a public unauthenticated status API. It integrates with Salesforce, HubSpot, Attio, Outreach, Salesloft, Gong, and others, targeting mid-market and enterprise revenue teams in dev tools, SaaS, and cybersecurity.'
image: https://salesgraph.com/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: salesgraph-mcp.yml
  slug: salesgraph-mcpyml
modified: '2026-08-13'
name: Salesgraph
nav: Providers
network: true
overview: 'Salesgraph publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audit API, Commands API, Runs API, and 2 more. Tagged areas include Company, Sales, Revenue Automation, Go-To-Market, and AI Agents.


  Salesgraph''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 22 more developer resources.'
plans:
- name: Salesgraph Plans Pricing
  plan_count: 0
  slug: salesgraph-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Salesgraph Rate Limits
  slug: salesgraph-rate-limits
score:
  band: thin
  composite: 36.3
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 16.7
    contract_quality: 14.7
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 36.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
