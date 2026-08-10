---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Routerplex Agentic Access
  operation_count: 5
  slug: routerplex-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 5
apis:
- description: The Chat API from RouterPlex — 1 operation(s) for chat.
  name: RouterPlex Chat API
  slug: routerplex-chat-api
- description: The Images API from RouterPlex — 1 operation(s) for images.
  name: RouterPlex Images API
  slug: routerplex-images-api
- description: The Messages API from RouterPlex — 1 operation(s) for messages.
  name: RouterPlex Messages API
  slug: routerplex-messages-api
- description: The Models API from RouterPlex — 1 operation(s) for models.
  name: RouterPlex Models API
  slug: routerplex-models-api
- description: The Responses API from RouterPlex — 1 operation(s) for responses.
  name: RouterPlex Responses API
  slug: routerplex-responses-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/routerplex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/routerplex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/routerplex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://routerplex.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.routerplex.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.routerplex.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.routerplex.com/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.routerplex.com/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@routerplex.com
- group: operate
  title: ''
  type: Support
  url: https://t.me/RouterPlex
- group: company
  title: ''
  type: Blog
  url: https://routerplex.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://routerplex.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RouterPlex
- group: commercial
  title: ''
  type: Pricing
  url: https://routerplex.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://routerplex.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://routerplex.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routerplex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routerplex.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/routerplex-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/routerplex-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/routerplex-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/routerplex-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://routerplex.com/.well-known/api-catalog
- group: other
  title: ''
  type: ContentSignal
  url: https://routerplex.com/robots.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/routerplex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/routerplex-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/routerplex-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/routerplex-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/routerplex-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/routerplex-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/routerplex-packages.yml
- group: other
  title: ''
  type: Playground
  url: https://routerplex.com/dashboard/playground
- group: start
  title: ''
  type: Sandbox
  url: sandbox/routerplex-sandbox.yml
- group: other
  title: ''
  type: Benchmarks
  url: https://routerplex.com/benchmarks.md
- group: commercial
  title: ''
  type: Pricing
  url: https://routerplex.com/pricing.md
created: '2026-07-26'
description: RouterPlex is an OpenAI- and Anthropic-compatible AI gateway that fronts 39 chat and image models from 14 vendors — OpenAI, Anthropic, Google, DeepSeek, Moonshot, Alibaba, MiniMax, Zhipu, xAI and others — behind one API key and one prepaid balance, at vendor list prices with no markup and no top-up fee. It exposes OpenAI Chat Completions, the OpenAI Responses route for Codex, Anthropic Messages, image generation and a model catalog on a single v1 REST surface, so the official OpenAI and Anthropic SDKs work unmodified with only a base URL change. Per-key hard spend budgets, model allowlists and optional RPM/TPM limits are the containment model for autonomous agents. RouterPlex also runs an anonymous read-only MCP server for model discovery and publishes an RFC 9727 API catalog, an OpenAPI 3.1 description, llms.txt and Markdown pricing and benchmark companions.
image: https://routerplex.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: RouterPlex Public Catalog
  slug: routerplex-public-catalog
modified: '2026-08-09'
name: RouterPlex
nav: Providers
network: true
overview: 'RouterPlex publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Images API, Messages API, and 2 more. Tagged areas include llm, ai, ai-gateway, inference, and model-router.


  RouterPlex''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Routerplex Plans
  plan_count: 4
  slug: routerplex-plans
random_paper: 70
rate_limits:
- limit_count: 3
  name: Routerplex Rate Limits
  slug: routerplex-rate-limits
score:
  band: strong
  composite: 60.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 53.6
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 36.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: authentication
  name: Routerplex Authentication
  slug: routerplex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Routerplex Domain Security
  slug: routerplex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: routerplex
tags:
- llm
- ai
- ai-gateway
- inference
- model-router
- openai-compatible
- anthropic-compatible
- claude
- gpt
- gemini
- api-gateway
- agent-infrastructure
- developer-tools
- mcp
- llmops
website: https://routerplex.com
---
