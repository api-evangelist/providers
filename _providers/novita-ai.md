---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Novita Ai Agentic Access
  operation_count: 4
  slug: novita-ai-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 2
apis:
- description: On-demand GPU instance management and templates plus serverless GPU endpoints. Create, start, stop, and delete instances; list products and templates; query usage-based and fixed-term billing.
  name: Novita AI GPU API
  slug: gpu
- description: The Openai API from Novita AI — 4 operation(s) for openai.
  name: Novita AI Openai API
  slug: novita-ai-openai-api
artifact_total: 11
asyncapis:
- description: 'AsyncAPI 2.6 description of the asynchronous surfaces of the Novita AI platform: 1. **Server-Sent Events (SSE) streaming** for OpenAI-compatible chat completions (`POST /openai/v1/chat/completions` wi'
  name: Novita AI Streaming & Webhook API
  slug: novita-ai-asyncapi
collections:
- collection_type: open
  name: Novita API
  slug: open-novita-ai
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/novita-ai-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/novita-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novita-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novita.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://novita.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://novita.ai/docs/api-reference/api-reference-overview
- group: docs
  title: ''
  type: Guides
  url: https://novita.ai/docs/guides/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://novita.ai/pricing
- group: start
  title: ''
  type: Signup
  url: https://novita.ai/
- group: company
  title: ''
  type: Blog
  url: https://novita.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.novita.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novita.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://novita.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/novitalabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/novita-ai-labs
- group: company
  title: ''
  type: Twitter
  url: https://x.com/novitalabs
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/Mqx7nWYzDF
- group: agent
  title: ''
  type: LlmsText
  url: https://novita.ai/llms.txt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/novitalabs/python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/novitalabs/javascript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/novitalabs/golang-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/novitalabs/langchain-novita
- group: build
  title: ''
  type: CLI
  url: https://github.com/novitalabs/novita-cli
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/novitalabs/novita-mcp-server
- group: commercial
  title: ''
  type: Plans
  url: plans/novita-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/novita-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/novita-ai-finops.yml
created: '2026-05-08'
description: Novita AI is an AI inference cloud offering serverless LLM, image, video, and audio generation APIs alongside on-demand GPU rentals and serverless GPU endpoints. Hosts open-source models with both native and OpenAI-compatible chat surfaces, plus an agent sandbox and MCP server for tool-using agents.
finops:
- name: Novita Ai Finops
  service_category: AI
  slug: novita-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: novita-mcp-server
  slug: novita-mcp-server
modified: '2026-05-30'
name: Novita AI
nav: Providers
network: true
overview: 'Novita AI publishes 1 API on the [APIs.io](https://apis.io/) network: Openai API. Tagged areas include AI, LLM, Inference, GPU, and OpenAI Compatible.


  The Novita AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Novita AI''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, CLI, and 21 more developer resources.'
plans:
- name: Novita Ai Plans Pricing
  plan_count: 1
  slug: novita-ai-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Novita Ai Rate Limits
  slug: novita-ai-rate-limits
rules:
- name: Novita AI API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: novita-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 52.4
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 57.5
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novita-ai/refs/heads/main/screenshots/novita-ai-2026-06-20T190520.png
security:
- kind: domain-security
  name: Novita Ai Domain Security
  slug: novita-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: novita-ai
tags:
- AI
- LLM
- Inference
- GPU
- OpenAI Compatible
- Image Generation
- Video Generation
- Audio
- Embeddings
- Sandbox
- MCP
website: https://novita.ai/
---
