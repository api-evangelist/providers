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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Consume a deployed Lua agent directly over HTTP — single-shot generation or real-time SSE streaming — with bearer API-key auth.
  name: Lua Agent HTTP API
  slug: lua-agent-http-api
artifact_total: 6
asyncapis:
- description: ''
  name: Lua Global Inc Webhooks
  slug: lua-global-inc-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lua-global-inc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.heylua.ai/policies/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lua-global-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heylua.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.heylua.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.heylua.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.heylua.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.heylua.ai/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/SRPEuwCzaD
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lua-ai-global
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.heylua.ai/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.heylua.ai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lua-global-inc-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/lua-global-inc-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lua-global-inc-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/lua-global-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lua-global-inc-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lua-global-inc-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lua-global-inc-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lua-global-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lua-global-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lua-global-inc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lua-global-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lua-global-inc-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/lua-global-inc-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lua-global-inc-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lua-global-inc-webhooks.yml
created: '2026-07-17'
description: Lua (heylua.ai), operated by Lua Global Inc, is a Y Combinator-backed "Agent OS" platform for building, testing, deploying, and governing enterprise AI agents. People and agents work in shared rooms with shared memory and governance on every action. Developers author agents in TypeScript with the lua-cli SDK (LuaAgent/LuaSkill/LuaTool, plus webhooks, scheduled jobs, and pre/post processors), while non-technical users build support, sales, HR, and research agents no-code. Agents are model-agnostic (OpenAI, Anthropic, Meta, DeepSeek, Gemini, Groq, xAI, Qwen) and deploy across WhatsApp, Slack, Email, Teams, Instagram, voice, an embeddable web chat widget (LuaPop), and a public HTTP chat API at api.heylua.ai. A read-only MCP server exposes agent state to MCP-aware clients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lua-global-inc.png
layout: provider
mcp_servers:
- description: ''
  name: lua-global-inc-mcp.yml
  slug: lua-global-inc-mcpyml
modified: '2026-07-20'
name: Lua Global Inc
nav: Providers
network: true
overview: 'Lua Global Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agent Platform, and Developer Tools.


  The Lua Global Inc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lua Global Inc''s developer surface includes documentation, API reference, getting-started guide, support, changelog, CLI, authentication, and 21 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 37.0
  delta: -5.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 42.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lua-global-inc/refs/heads/main/screenshots/lua-global-inc-2026-07-25T225637.png
security:
- kind: authentication
  name: Lua Global Inc Authentication
  slug: lua-global-inc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lua Global Inc Domain Security
  slug: lua-global-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lua Global Inc Vulnerability Disclosure
  slug: lua-global-inc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lua-global-inc
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agent Platform
- Developer Tools
- Model Context Protocol
- Conversational AI
- Chatbots
- Automation
website: https://heylua.ai
---
