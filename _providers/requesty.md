---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Requesty Agentic Access
  operation_count: 10
  slug: requesty-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 4
apis:
- description: OpenAI-compatible chat completions routed across 300+ models from OpenAI, Anthropic, DeepSeek, Together AI, and more, with streaming, tool use, web search, automatic fallbacks, and response caching.
  name: Requesty Chat Completions API
  slug: requesty-chat-completions-api
- description: Lists the 300+ models routable through the Requesty gateway with their identifiers, provider, context length, and per-token pricing.
  name: Requesty Models API
  slug: requesty-models-api
- description: Retrieves per-key and organization-level usage statistics, request cost, and spend reporting for observability and FinOps across the gateway.
  name: Requesty Usage & Analytics API
  slug: requesty-usage-analytics-api
- description: Programmatically create, list, inspect, and delete API keys and manage their spending limits, labels, and expiration for governing gateway access.
  name: Requesty API Keys API
  slug: requesty-api-keys-api
artifact_total: 15
asyncapis:
- description: AsyncAPI 2.6 description of Requesty's **chat completion streaming** surface. Requesty does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.reques
  name: Requesty Chat Completions Streaming (HTTP + SSE)
  slug: requesty-asyncapi
collections:
- collection_type: open
  name: Requesty Router API
  slug: open-requesty
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/requesty-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/requesty-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/requesty-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/requesty-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/requesty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/requesty-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/requestyai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/requesty
- group: company
  title: ''
  type: Website
  url: https://www.requesty.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.requesty.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/requesty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/requesty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/requesty-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.requesty.ai/blog
created: '2026-06-20'
description: Requesty is an LLM routing and gateway platform that exposes a single OpenAI-compatible API across 300+ models from providers like OpenAI, Anthropic, DeepSeek, and Together AI. The Requesty Router adds intelligent routing, automatic fallbacks, response caching, spend controls, and per-request cost observability on top of unified inference.
finops:
- name: Requesty Finops
  service_category: AI and Machine Learning
  slug: requesty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-06-20'
name: Requesty
nav: Providers
network: true
overview: 'Requesty publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat Completions API, Models API, Usage & Analytics API, and 1 more. Tagged areas include AI, LLM, Routing, Gateway, and Observability.


  The Requesty catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Requesty''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Requesty Plans Pricing
  plan_count: 3
  slug: requesty-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Requesty Rate Limits
  slug: requesty-rate-limits
rules:
- name: Requesty API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: requesty-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: -5.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/requesty/refs/heads/main/screenshots/requesty-2026-06-20T192926.png
security:
- kind: authentication
  name: Requesty Authentication
  slug: requesty-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Requesty Domain Security
  slug: requesty-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Requesty Vulnerability Disclosure
  slug: requesty-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Requesty Trust Center
  slug: requesty-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: requesty
tags:
- AI
- LLM
- Routing
- Gateway
- Observability
website: https://www.requesty.ai
---
