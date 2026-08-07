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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 7
apis:
- description: OpenAI-compatible LLM gateway exposing 90+ models from OpenAI, Anthropic, Google, DeepSeek, Mistral, xAI, Moonshot, Alibaba (Qwen), Cohere, and Perplexity behind a single base URL (`https://gateway.gl
  name: Glama AI Gateway
  slug: glama-ai-gateway
- description: 'Reverse-proxy MCP gateway that fronts hosted, remote, and custom MCP servers under a per-user endpoint of the form `https://glama.ai/endpoints/<connection-profile>/mcp`. The gateway appears as an MCP '
  name: Glama MCP Gateway
  slug: glama-mcp-gateway
- description: Comprehensive index of 23,000+ MCP servers, 4,000+ managed connectors, and 169,000+ tools spanning 86 curated categories. Every server is maintainer-verified, continuously rebuilt from source, and sco
  name: Glama MCP Server Registry
  slug: glama-mcp-registry
- description: One-click managed hosting for any MCP server. Submit a GitHub repository and Glama indexes every tool, schema, and annotation, then offers a single click to deploy the server onto Glama's managed infr
  name: Glama MCP Hosting
  slug: glama-mcp-hosting
- description: Browser-based MCP debugger that spins up an ephemeral sandbox from a server URL. Lets developers exercise tools with structured inputs, view raw JSON-RPC traffic, complete OAuth flows, test prompts an
  name: Glama MCP Inspector
  slug: glama-mcp-inspector
- description: All-in-one AI workspace that chats with any MCP server the user owns, routed through the Glama Gateway so every tool call is visible and controllable. Supports file uploads (PDFs), projects, memory, w
  name: Glama Chat and Playground
  slug: glama-chat
- description: Workflow automation primitive on the Glama platform. Composes MCP servers, the AI gateway, and Glama Chat into scheduled or event-triggered jobs (e.g., GitHub pull-request security checks) with full o
  name: Glama Automations
  slug: glama-automations
artifact_total: 29
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glama-ai-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://glama.ai
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://glama.ai/mcp/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://glama.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://glama.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://glama.ai/release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://glama.ai/status
- group: operate
  title: ''
  type: Support
  url: https://glama.ai/support
- group: company
  title: ''
  type: Newsletter
  url: https://glama.ai/newsletter
- group: company
  title: ''
  type: Careers
  url: https://glama.ai/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glama.ai/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glama.ai/policies/privacy-policy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://glama.ai/policies/vulnerability-disclosure
- group: start
  title: ''
  type: Signup
  url: https://glama.ai
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/glama
- group: operate
  title: ''
  type: Forums
  url: https://www.reddit.com/r/glama
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/glama-ai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/glama-ai/lightport
- group: build
  title: ''
  type: Tools
  url: https://github.com/glama-ai/rjsf-validator-cfworker
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/servers
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/connectors
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/tools
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/clients
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/hosting
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/inspector
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/gateway
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/mcp/methodology
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/ai/gateway
- group: other
  title: ''
  type: Models
  url: https://glama.ai/ai/models
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/blog/2026-01-24-quickstart-publishing-a-server
- group: docs
  title: ''
  type: Documentation
  url: https://glama.ai/blog/2026-01-24-official-mcp-registry-serverjson-requirements
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io
- group: commercial
  title: ''
  type: Plans
  url: https://glama.ai/pricing
created: '2026-05-25T00:00:00.000Z'
description: Glama is an all-in-one AI workspace combining an MCP server marketplace and registry, a managed MCP gateway, one-click MCP server hosting, an OpenAI-compatible LLM gateway routing 90+ models across OpenAI, Anthropic, Google, DeepSeek, Mistral, xAI and other providers, and Glama Chat with built-in projects, memory, web tools, and automations. The Glama MCP Registry indexes 23,000+ MCP servers, 4,000+ managed connectors, and 169,000+ tools across 86 categories, and Glama positions itself as a superset of the official MCP Registry, with maintainer verification, continuous rebuilds, and capability-level quality scoring. The Glama MCP Gateway fronts every hosted, remote, or custom MCP server behind a per-user endpoint with full JSON-RPC logging, per-tool access control, managed OAuth 2.1, and audit log export. The Glama AI Gateway is OpenAI-compatible at `https://gateway.glama.ai/v1` and provides prompt caching, load balancing, fallbacks, reasoning effort levels, web search and fetch
  tools, real-time cost analytics, and consolidated billing with no markup.
features:
- MCP server registry indexing 23,000+ servers, 4,000+ connectors, and 169,000+ tools across 86 categories
- Maintainer-verified and continuously rebuilt MCP servers with quality and safety scoring
- Browser-based MCP Inspector with ephemeral sandbox, JSON-RPC trace view, OAuth flow handling, and shareable sessions
- One-click MCP server hosting from any GitHub repository with persistent storage and SSE security
- Free open-source MCP server hosting
- MCP Gateway with per-user endpoint, full JSON-RPC payload logging, per-tool access control, OAuth 2.1 credential management, audit log export, and session lifecycle tracking
- Upstream tool-definition rewriting at the gateway layer
- OpenAI-compatible AI gateway at `https://gateway.glama.ai/v1`
- 90+ models across OpenAI, Anthropic, Google, DeepSeek, Mistral, xAI, Moonshot (Kimi), Alibaba (Qwen), Cohere, and Perplexity
- Drop-in SDK compatibility with OpenAI SDKs and LangChain
- Prompt caching, load balancing, automatic fallbacks, and reasoning-effort presets (low / medium / high)
- Web search and web fetch tools across the gateway
- Real-time cost analytics and consolidated billing with no markup on listed provider prices
- ~40ms median gateway latency and stated 99% uptime
- No rate limits under 1B tokens/day; higher quotas negotiable within 48 hours
- Glama Chat playground with file uploads (PDFs), projects, memory, persistent storage, custom exports, and any MCP server the user owns
- Automations primitive composing MCP servers, the AI gateway, and Chat into scheduled or triggered workflows
- MCP Sampling support (servers can request LLM completions during execution)
- Progress notifications, audio/image responses, and elicitations support in MCP
- Lightport, an open-source lightweight gateway that makes LLM providers OpenAI-compatible
- Three commercial plans (Starter $9, Pro $26, Business $80) bundling AI credits and fast hosted MCP servers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glama-ai.png
layout: provider
modified: '2026-05-25'
name: Glama
nav: Providers
network: true
overview: 'Glama publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Artificial Intelligence, MCP, Model Context Protocol, and LLM Gateway.


  Glama''s developer surface includes developer portal, documentation, getting-started guide, pricing, engineering blog, changelog, support, and 27 more developer resources.'
random_paper: 83
score:
  band: emerging
  composite: 27.2
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 27.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glama-ai/refs/heads/main/screenshots/glama-ai-2026-06-20T181858.png
security:
- kind: domain-security
  name: Glama Ai Domain Security
  slug: glama-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: glama-ai
tags:
- AI
- Artificial Intelligence
- MCP
- Model Context Protocol
- LLM Gateway
- MCP Gateway
- MCP Marketplace
- AI Workspace
- Multi-Provider
- OAuth
- Observability
website: https://glama.ai
---
