---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Klavis Agentic Access
  operation_count: 5
  slug: klavis-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 5
apis:
- description: The Klavis API manages hosted MCP servers, OAuth flows for 50+ integrated services, Strata multi-tool servers, and live sandbox environments. Endpoints cover MCP server CRUD and tool invocation, sandb
  name: Klavis MCP Platform API
  slug: mcp-platform
- description: Create and manage hosted MCP server instances
  name: Klavis AI MCP Servers API
  slug: klavis-mcp-servers-api
- description: Acquire and manage isolated sandbox VMs
  name: Klavis AI Sandbox API
  slug: klavis-sandbox-api
- description: List and invoke MCP server tools
  name: Klavis AI Tools API
  slug: klavis-tools-api
- description: End-user metadata for agent integrations
  name: Klavis AI Users API
  slug: klavis-users-api
artifact_total: 12
collections:
- collection_type: open
  name: Klavis AI MCP Platform API
  slug: open-klavis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/klavis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klavis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klavis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.klavis.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.klavis.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.klavis.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Klavis-AI
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Klavis-AI/klavis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.klavis.ai/pricing
- group: operate
  title: ''
  type: Contact
  url: https://www.klavis.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klavis.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klavis.ai/privacy
created: '2026-05-23'
description: Klavis AI is an open-source MCP integration platform that lets AI agents reliably use external tools at production scale. The product line is organized around Strata (intelligent connectors that compress and route tool context), 100+ prebuilt MCP integrations with OAuth, and an MCP Sandbox for live agent training and evaluation. Target customers are AI agent companies, RL teams, and enterprises that need long-horizon multi-app environments with seeded state, resets, and verifiable outcomes, plus SOC 2 Type II and GDPR posture. SDKs are available for Python and TypeScript/JavaScript, integrations cover Claude, OpenAI, Gemini, Cohere, Mistral, LangChain/LangGraph, LlamaIndex, CrewAI, Mastra, Agno, Fireworks, Together, and Google ADK, and the project is Apache-2.0 on GitHub.
finops:
- name: Klavis Finops
  service_category: API
  slug: klavis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klavis.png
layout: provider
modified: '2026-05-23'
name: Klavis AI
nav: Providers
network: true
overview: 'Klavis AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including MCP Servers API, Sandbox API, Tools API, and 1 more. Tagged areas include MCP, Model Context Protocol, MCP Servers, MCP Hosting, and Connectors.


  Klavis AI''s developer surface includes authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Klavis Plans Pricing
  plan_count: 1
  slug: klavis-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 2
  name: Klavis Rate Limits
  slug: klavis-rate-limits
score:
  band: thin
  composite: 44.9
  delta: 3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klavis/refs/heads/main/screenshots/klavis-2026-06-20T184058.png
security:
- kind: authentication
  name: Klavis Authentication
  slug: klavis-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Klavis Domain Security
  slug: klavis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klavis
tags:
- MCP
- Model Context Protocol
- MCP Servers
- MCP Hosting
- Connectors
- OAuth
- Sandboxes
- Agent Training
- Reinforcement Learning
- White Label
- Open Source
- Strata
website: https://www.klavis.ai
---
