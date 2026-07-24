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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 11.5
  scored_at: '2026-07-23'
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
- description: ''
  name: crow-mcp.yml
  slug: crow-mcpyml
modified: '2026-07-18'
name: Crow
nav: Providers
network: true
overview: 'Crow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, MCP, and Model Context Protocol.


  Crow''s developer surface includes documentation, getting-started guide, signup flow, CLI, sandbox, and 11 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 28.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
- Model Context Protocol
- OpenAPI
- Developer Tools
- SDK
- Embeddable Widget
- Commercial Real Estate
website: https://www.usecrow.ai/
---
