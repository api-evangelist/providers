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
api_count: 1
apis:
- description: The Guildcode REST API for creating workspace-scoped agent sessions, posting events, and reading session events and tasks. HTTP Basic authentication; no public OpenAPI spec.
  name: Guild REST API
  slug: guild-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.guild.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.guild.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.guild.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.guild.ai/platform/triggers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.guild.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://guild.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://guild.ai/community
- group: commercial
  title: ''
  type: Pricing
  url: https://guild.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.guild.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://guild.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://guild.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/guildai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/guildai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/guildai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/guildai-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/guildai-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guildai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/guildai-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guildai-domain-security.yml
created: '2026-07-17'
description: Guild.ai is a control plane for AI agents that lets engineering teams build, deploy, govern, and share agents in production. Agents are authored in TypeScript with the @guildai/agents-sdk (alongside Guild Native and Goose recipe agent types) and run in a governed, sandboxed runtime that mediates all external tool access and enforces least-privilege scoped credentials, with workspaces, versioning, audit logs, and real-time usage and cost tracking. Guild is model-agnostic across OpenAI, Anthropic, and Google, ships a first-party CLI that also runs an MCP server, exposes a Guildcode REST API plus per-trigger API keys for programmatic invocation, offers 40+ integrations (GitHub, Slack, Jira, Linear, Notion, Google Cloud, and more), and provides an Agent Hub for discovering, forking, and publishing agents. Backed by GV, NFX, and Khosla Ventures.
image: https://app.guild.ai/favicons/favicon.png
layout: provider
mcp_servers:
- description: The Guild CLI ships an MCP server that exposes Guild control-plane operations as tools for MCP clients, so client agents can list and inspect workspaces, agents, sessions, triggers, credentials, and i
  name: Guild.ai MCP Server
  slug: guildai-mcp-server
modified: '2026-07-19'
name: Guild.ai
nav: Providers
network: true
overview: 'Guild.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Control Plane, and Agent Runtime.


  Guild.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 12 more developer resources.'
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/guildai/refs/heads/main/screenshots/guildai-2026-07-25T220430.png
security:
- kind: authentication
  name: Guildai Authentication
  slug: guildai-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Guildai Domain Security
  slug: guildai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: guildai
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Control Plane
- Agent Runtime
- Developer Tools
- MCP
- LLM
- Agent Governance
- SDK
- CLI
website: https://www.guild.ai
---
