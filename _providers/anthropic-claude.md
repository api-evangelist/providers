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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Anthropic Claude Agentic Access
  operation_count: 9
  slug: anthropic-claude-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 4
apis:
- description: Submit and manage asynchronous Message Batches.
  name: Anthropic Claude Message Batches API
  slug: anthropic-claude-message-batches-api
- description: Create messages with Claude models.
  name: Anthropic Claude Messages API
  slug: anthropic-claude-messages-api
- description: List and inspect available Claude models.
  name: Anthropic Claude Models API
  slug: anthropic-claude-models-api
- description: Count tokens for a prospective Messages request.
  name: Anthropic Claude Token Counting API
  slug: anthropic-claude-token-counting-api
artifact_total: 12
asyncapis:
- description: 'AsyncAPI specification modeling the Server-Sent Events (SSE) stream produced by Anthropic''s Claude Messages API when `"stream": true` is set on a POST to `/v1/messages`. Transport: HTTP/1.1 with `Cont'
  name: Anthropic Claude Messages Streaming API
  slug: anthropic-claude-asyncapi
collections:
- collection_type: open
  name: Anthropic Claude Messages API
  slug: open-anthropic-claude
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anthropic-claude-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anthropic-claude-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anthropic-claude-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anthropic-claude-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.anthropic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.anthropic.com/en/api/getting-started
- group: start
  title: ''
  type: Console
  url: https://console.anthropic.com
- group: start
  title: ''
  type: Signup
  url: https://console.anthropic.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anthropic.com/pricing
- group: other
  title: ''
  type: Models
  url: https://docs.anthropic.com/en/docs/about-claude/models
- group: auth
  title: ''
  type: Authentication
  url: https://docs.anthropic.com/en/api/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.anthropic.com/en/api/rate-limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.anthropic.com/en/api/errors
- group: design
  title: ''
  type: Versioning
  url: https://docs.anthropic.com/en/api/versioning
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anthropic.com
- group: operate
  title: ''
  type: Support
  url: https://support.anthropic.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anthropic.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anthropic.com/legal/commercial-terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anthropics
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/anthropics/anthropic-sdk-python
- group: build
  title: ''
  type: TypeScript SDK
  url: https://github.com/anthropics/anthropic-sdk-typescript
- group: learn
  title: ''
  type: Cookbook
  url: https://github.com/anthropics/anthropic-cookbook
- group: build
  title: ''
  type: Claude Code
  url: https://www.anthropic.com/claude-code
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://modelcontextprotocol.io
- group: company
  title: ''
  type: Blog
  url: https://www.anthropic.com/news
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/AnthropicAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anthropicresearch
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@anthropic-ai
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/anthropics/claude-ai-mcp
created: '2026-05-11'
description: Anthropic Claude is a family of frontier large language models (Opus, Sonnet, Haiku) accessible via the Anthropic API for building AI assistants, agents, and integrations. The API supports streaming chat completions, tool use, vision, prompt caching, batch processing, the Files API, computer use, and the Model Context Protocol, with authentication via x-api-key headers and a base URL at api.anthropic.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anthropic-claude.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Anthropic Claude
nav: Providers
network: true
overview: 'Anthropic Claude publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Message Batches API, Messages API, Models API, and 1 more. Tagged areas include Artificial Intelligence, Large Language Models, LLM, Generative AI, and Chat.


  The Anthropic Claude catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Anthropic Claude''s developer surface includes authentication, documentation, API reference, developer console, signup flow, pricing, support, and 23 more developer resources.'
random_paper: 11
rules:
- name: Anthropic Claude API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: anthropic-claude-asyncapi-spectral-rules
score:
  band: developing
  composite: 54.0
  delta: 2.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 67.9
    developer_ergonomics: 54.3
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anthropic-claude/refs/heads/main/screenshots/anthropic-claude-2026-06-20T172031.png
security:
- kind: authentication
  name: Anthropic Claude Authentication
  slug: anthropic-claude-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anthropic Claude Domain Security
  slug: anthropic-claude-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anthropic Claude Vulnerability Disclosure
  slug: anthropic-claude-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: anthropic-claude
tags:
- Artificial Intelligence
- Large Language Models
- LLM
- Generative AI
- Chat
- Agents
- Claude
website: https://www.anthropic.com
---
