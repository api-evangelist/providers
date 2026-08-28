---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Crow agent platform surface — the widget/agent runtime served from api.usecrow.org, configured via the dashboard and consumed through the embed script and the @usecrow/client / @usecrow/ui SDKs. C
  name: Crow Agent Platform
  slug: crow-agent-platform
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usecrow.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.usecrow.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usecrow.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usecrow.ai/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.usecrow.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usecrow
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usecrow.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usecrow.ai/privacy
- group: build
  title: ''
  type: Packages
  url: packages/crow-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crow-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/crow-cli.yml
- group: design
  title: ''
  type: Components
  url: components/crow-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crow-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crow-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crow-llms.txt
created: '2026-07-17'
description: Crow is a Y Combinator (Winter 2026) company building an AI infrastructure platform that makes any web or mobile application AI-native. Instead of a simple chatbot, Crow embeds an agent that connects to a product's own APIs and MCP servers, executes workflows, navigates users between pages, and calls server-side and client-side tools from natural-language commands. Developers add Crow with a single script tag or the React SDK, point it at a REST API via OpenAPI or at an MCP server, and configure the agent in a sandbox. Crow also ships the Envoy CLI, which reads a backend codebase and auto-generates and deploys an MCP server, plus a headless client and React UI component library (Widget and Copilot). Crow is initially positioned for commercial real estate but the platform applies to any software product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crow.png
layout: provider
mcp_servers:
- description: Crow Docs MCP - connects an AI coding agent to Crow's documentation so it can help integrate the Crow widget, set up identity verification, and configure OpenAPI or MCP server integrations with full c
  name: Crow MCP Server
  slug: crow-mcp-server
modified: '2026-07-18'
name: Crow
nav: Providers
network: true
overview: 'Crow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, MCP, and OpenAPI.


  Crow''s developer surface includes documentation, getting-started guide, signup flow, CLI, sandbox, and 11 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 18.3
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crow/refs/heads/main/screenshots/crow-2026-07-25T210812.png
security:
- kind: domain-security
  name: Crow Domain Security
  slug: crow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crow
tags:
- Company
- Artificial Intelligence
- AI Agents
- MCP
- OpenAPI
- Developer Tools
- SDK
- Embeddable Widget
- Commercial Real Estate
website: https://www.usecrow.ai/
---
