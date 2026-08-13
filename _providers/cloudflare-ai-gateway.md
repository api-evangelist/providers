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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cloudflare Ai Gateway Agentic Access
  operation_count: 8
  slug: cloudflare-ai-gateway-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 7
apis:
- description: The AI Gateway proxy endpoint accepts requests in each provider's native API format and forwards them through Cloudflare's edge with analytics, caching, retries, rate limiting, fallback, and guardrail
  name: Cloudflare AI Gateway Proxy
  slug: cloudflare-ai-gateway-proxy
- description: Unified REST API launched May 21, 2026 that lets developers call any supported model through a single endpoint instead of formatting requests for each provider individually. Sits alongside the provide
  name: Cloudflare AI Gateway Unified REST API
  slug: cloudflare-ai-gateway-unified-api
- description: The Cloudflare API surface for managing AI Gateway resources — creating gateways, listing them, retrieving request logs, and configuring caching, rate limiting, and authentication. Exposed under the s
  name: Cloudflare AI Gateway Management API
  slug: cloudflare-ai-gateway-management-api
- description: Cloudflare-hosted remote MCP server that exposes AI Gateway control-plane operations to MCP-compatible AI agents.
  name: AI Gateway MCP Server
  slug: ai-gateway-mcp
- description: The Gateways API from Cloudflare AI Gateway — 2 operation(s) for gateways.
  name: Cloudflare AI Gateway Gateways API
  slug: cloudflare-ai-gateway-gateways-api
- description: The Logs API from Cloudflare AI Gateway — 1 operation(s) for logs.
  name: Cloudflare AI Gateway Logs API
  slug: cloudflare-ai-gateway-logs-api
- description: The Proxy API from Cloudflare AI Gateway — 2 operation(s) for proxy.
  name: Cloudflare AI Gateway Proxy API
  slug: cloudflare-ai-gateway-proxy-api
artifact_total: 37
collections:
- collection_type: open
  name: Cloudflare AI Gateway API
  slug: open-cloudflare-ai-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-ai-gateway-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-ai-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-ai-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudflare-ai-gateway-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.cloudflare.com/ai-gateway/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/ai-gateway/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cloudflare.com/ai-gateway/get-started/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudflare.com/ai-gateway/usage/providers/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cloudflare.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/
- group: start
  title: ''
  type: Signup
  url: https://dash.cloudflare.com/sign-up
- group: start
  title: ''
  type: Console
  url: https://dash.cloudflare.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudflare.com/plans/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-go
- group: build
  title: ''
  type: CLI
  url: https://developers.cloudflare.com/workers/wrangler/
- group: agent
  title: ''
  type: MCPServer
  url: https://ai-gateway.mcp.cloudflare.com/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudflare
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudflarestatus.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudflare.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cloudflare.com/llms.txt
created: '2026-05-23'
description: Cloudflare AI Gateway is a managed LLM proxy that sits in front of 23+ AI providers (OpenAI, Anthropic, Google AI Studio, Google Vertex AI, Amazon Bedrock, Azure OpenAI, Workers AI, Mistral, Cohere, Groq, DeepSeek, Cerebras, xAI, Perplexity, Replicate, HuggingFace, OpenRouter, ElevenLabs, Deepgram, Cartesia, Ideogram, Fal AI, Baseten, Parallel) and provides analytics, request and error logging, response caching, rate limiting, request retries, model fallback, guardrails, and evaluations. A unified REST API launched May 21, 2026 lets developers call any model through a single endpoint. The gateway integrates with Workers AI, the Secrets Store, and Cloudflare CASB's Claude Compliance API support. This is a standalone product profile; the broader Cloudflare provider profile lives at github.com/api-evangelist/cloudflare.
features:
- description: OpenAI, Anthropic, Google AI Studio, Google Vertex AI, Amazon Bedrock, Azure OpenAI, Workers AI, Mistral, Cohere, Groq, DeepSeek, Cerebras, xAI, Perplexity, Replicate, HuggingFace, OpenRouter, ElevenLabs, Deepgram, Cartesia, Ideogram, Fal AI, Baseten, Parallel.
  name: 23+ Provider Coverage
- description: Single endpoint that can call any supported model (launched May 21, 2026), alongside provider-native pass-through mode.
  name: Unified REST API
- description: Per-request analytics for tokens, cost, latency, and error rates with full request and response logging.
  name: Analytics and Logging
- description: Cache LLM responses at Cloudflare's edge to cut latency and provider spend.
  name: Edge Caching
- description: Enforce request and token rate limits per gateway, per application.
  name: Rate Limiting
- description: Automatically retry failing calls and fall back to alternate models or providers.
  name: Retries and Model Fallback
- description: Apply guardrails to prompts and responses and run evaluations against captured traffic.
  name: Guardrails and Evaluations
- description: Bring your own provider keys per gateway or route spend through Cloudflare's Unified Billing.
  name: BYOK and Unified Billing
- description: Native integration with Cloudflare Workers AI models via the cf-aig-gateway-id header.
  name: Workers AI Integration
- description: Provider keys can be sourced from Cloudflare's Secrets Store rather than embedded in client code.
  name: Secrets Store Integration
finops:
- name: Cloudflare Ai Gateway Finops
  service_category: API
  slug: cloudflare-ai-gateway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-ai-gateway.png
integrations:
- description: First-class integration with Cloudflare Workers AI inference catalog.
  name: Workers AI
- description: Call AI Gateway directly from Workers using AI bindings configured in wrangler.jsonc.
  name: Cloudflare Workers
- description: Store and rotate provider API keys without redeploying.
  name: Cloudflare Secrets Store
- description: CASB support for Anthropic's Claude Compliance API announced May 2026.
  name: Cloudflare CASB - Claude Compliance API
- description: Partnership offering announced May 19, 2026 that runs Anthropic-managed Claude agents on Cloudflare with AI Gateway in the path.
  name: Claude Managed Agents on Cloudflare
- description: Remote MCP server at ai-gateway.mcp.cloudflare.com/mcp for AI agent access to AI Gateway control plane.
  name: MCP Server
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
modified: '2026-05-23'
name: Cloudflare AI Gateway
nav: Providers
network: true
overview: 'Cloudflare AI Gateway publishes 3 APIs on the [APIs.io](https://apis.io/) network: Gateways API, Logs API, and Proxy API. Tagged areas include AI Gateway, LLM, Observability, Caching, and Rate Limiting.


  Cloudflare AI Gateway''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, changelog, engineering blog, and 16 more developer resources.'
plans:
- name: Cloudflare Ai Gateway Plans Pricing
  plan_count: 1
  slug: cloudflare-ai-gateway-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Cloudflare Ai Gateway Rate Limits
  slug: cloudflare-ai-gateway-rate-limits
score:
  band: strong
  composite: 57.3
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 56.7
    developer_ergonomics: 89.1
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-ai-gateway/refs/heads/main/screenshots/cloudflare-ai-gateway-2026-06-20T174550.png
security:
- kind: authentication
  name: Cloudflare Ai Gateway Authentication
  slug: cloudflare-ai-gateway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudflare Ai Gateway Domain Security
  slug: cloudflare-ai-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Ai Gateway Vulnerability Disclosure
  slug: cloudflare-ai-gateway-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-ai-gateway
tags:
- AI Gateway
- LLM
- Observability
- Caching
- Rate Limiting
- Workers AI
- Cloudflare
use_cases:
- description: Capture per-request tokens, latency, and cost across every provider in one place.
  name: Observe LLM Traffic
- description: Cache repeated responses at the edge and rate limit runaway workloads.
  name: Cut LLM Costs
- description: Configure retries and model fallback so a single provider outage does not take down the app.
  name: Fail Over Between Providers
- description: Apply guardrails and run evaluations against production AI traffic.
  name: Govern Prompts and Responses
- description: Use a single REST endpoint to address any supported model from any provider.
  name: Unify Multi-Provider Access
website: https://developers.cloudflare.com/ai-gateway/
---
