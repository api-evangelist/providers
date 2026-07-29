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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Hosted, OAuth 2.1-secured Model Context Protocol server that lets agents run read-only structured queries against a tenant's endpoint and agent observability data (schema discovery + analytics query),
  name: Origin Analytics MCP Server
  slug: origin-analytics-mcp-server
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.originhq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.originhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.originhq.com
- group: start
  title: ''
  type: GettingStarted
  url: https://support.originhq.com/docs/welcome-to-origin
- group: operate
  title: ''
  type: Support
  url: https://support.originhq.com
- group: company
  title: ''
  type: Blog
  url: https://www.originhq.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.originhq.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.originhq.com/pricing
- group: start
  title: ''
  type: Login
  url: https://dashboard.originhq.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.originhq.com/legal/service-terms
- group: auth
  title: ''
  type: Compliance
  url: https://www.originhq.com/legal/service-terms
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prelude-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prelude-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prelude-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prelude-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prelude-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/prelude-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prelude-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prelude-domain-security.yml
created: '2026-07-17'
description: Prelude Security is now Origin, an endpoint AI observability platform that inventories, observes, and measures the use of AI agents and Model Context Protocol (MCP) servers across an enterprise fleet. Deployed as a lightweight endpoint agent, Origin gives security and IT teams discovery of sanctioned and unsanctioned agents and MCP servers, security visibility into agent prompts, tool calls, file access and network activity, and spend tracking across models and teams. Origin also publishes a hosted, OAuth 2.1-secured MCP server that lets agents query endpoint and agent observability data in natural language. Backed by Insight Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prelude.png
layout: provider
mcp_servers:
- description: ''
  name: prelude-mcp.yml
  slug: prelude-mcpyml
modified: '2026-07-20'
name: Prelude
nav: Providers
network: true
overview: 'Prelude publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, AI Security, AI Observability, and Endpoint Security.


  Prelude''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, pricing, authentication, and 12 more developer resources.'
random_paper: 60
score:
  band: thin
  composite: 31.5
  delta: 0.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 30.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Prelude Authentication
  slug: prelude-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Prelude Domain Security
  slug: prelude-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prelude
tags:
- Company
- Cybersecurity
- AI Security
- AI Observability
- Endpoint Security
- AI Agents
- Model Context Protocol
- MCP
- Insight Partners
website: https://www.originhq.com/
---
