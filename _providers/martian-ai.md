---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Martian Ai Agentic Access
  operation_count: 3
  slug: martian-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: The Chat Completions API from Martian — 1 operation(s) for chat completions.
  name: Martian Chat Completions API
  slug: martian-ai-chat-completions-api
- description: The Messages API from Martian — 1 operation(s) for messages.
  name: Martian Messages API
  slug: martian-ai-messages-api
- description: The Models API from Martian — 1 operation(s) for models.
  name: Martian Models API
  slug: martian-ai-models-api
artifact_total: 17
asyncapis:
- description: AsyncAPI 2.6 description of the Martian Gateway's **chat completion streaming** surface. Martian does not publish a WebSocket API. The Martian Gateway is an OpenAI-compatible model router; its only as
  name: Martian Gateway Chat Completions Streaming (HTTP + SSE)
  slug: martian-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Martian Gateway Chat Completions API
  slug: open-martian-ai-chat-completions-api
- collection_type: open
  name: Martian Gateway Chat Completions Messages API
  slug: open-martian-ai-messages-api
- collection_type: open
  name: Martian Gateway Chat Completions Models API
  slug: open-martian-ai-models-api
- collection_type: open
  name: Martian Gateway API
  slug: open-martian-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/martian-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/martian-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/martian-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmartian
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withmartian
- group: company
  title: ''
  type: Website
  url: https://www.withmartian.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withmartian.com
- group: commercial
  title: ''
  type: Plans
  url: plans/martian-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/martian-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/martian-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.withmartian.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.withmartian.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.withmartian.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.withmartian.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.withmartian.com/resources/support
- group: start
  title: ''
  type: SignUp
  url: https://app.withmartian.com/
- group: start
  title: ''
  type: Login
  url: https://app.withmartian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withmartian.com
- group: build
  title: ''
  type: Packages
  url: packages/martian-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/martian-ai-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/martian-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/martian-ai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/martian-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/martian-ai-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/martian-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/martian-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/martian-ai-llms.txt
created: '2026-06-20'
description: Martian operates an LLM model router and gateway that dynamically routes each request to the best underlying model across providers for the optimal balance of quality, latency, and cost. The Martian Gateway exposes a drop-in, OpenAI-compatible REST API (and an Anthropic Messages-compatible surface) so applications can route across a large catalog of models by changing only the base URL.
finops:
- name: Martian Ai Finops
  service_category: AI and Machine Learning
  slug: martian-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/martian-ai.png
layout: provider
mcp_servers:
- description: ''
  name: martian-ai-mcp.yml
  slug: martian-ai-mcpyml
modified: '2026-08-08'
name: Martian
nav: Providers
network: true
overview: 'Martian publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat Completions API, Messages API, and Models API. Tagged areas include AI, LLM, Model Router, Gateway, and Cost Optimization.


  The Martian catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Martian''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, signup flow, and 20 more developer resources.'
plans:
- name: Martian Ai Plans Pricing
  plan_count: 3
  slug: martian-ai-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 4
  name: Martian Ai Rate Limits
  slug: martian-ai-rate-limits
rules:
- name: Martian API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: martian-ai-asyncapi-spectral-rules
score:
  band: strong
  composite: 59.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 70.1
    developer_ergonomics: 60.9
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 52.6
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/screenshots/martian-ai-2026-07-25T230258.png
security:
- kind: authentication
  name: Martian Ai Authentication
  slug: martian-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Martian Ai Domain Security
  slug: martian-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: martian-ai
tags:
- AI
- LLM
- Model Router
- Gateway
- Cost Optimization
website: https://www.withmartian.com
---
