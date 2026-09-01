---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 227
  human_in_the_loop: 2
  name: Fireworks Ai Agentic Access
  operation_count: 411
  slug: fireworks-ai-agentic-access
  summary_line: 411 operations · 227 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: The anthropic-messages.openapi_other API from Fireworks AI — 1 operation(s) for anthropic-messages.openapi_other.
  name: Fireworks AI anthropic-messages.openapi_other API
  slug: fireworks-ai-anthropic-messages-openapi-other-api
- description: The Chat API from Fireworks AI — 1 operation(s) for chat.
  name: Fireworks AI Chat API
  slug: fireworks-ai-chat-api
- description: The Completions API from Fireworks AI — 1 operation(s) for completions.
  name: Fireworks AI Completions API
  slug: fireworks-ai-completions-api
- description: The Gateway API from Fireworks AI — 126 operation(s) for gateway.
  name: Fireworks AI Gateway API
  slug: fireworks-ai-gateway-api
- description: The gateway-extra.openapi_Gateway API from Fireworks AI — 1 operation(s) for gateway-extra.openapi_gateway.
  name: Fireworks AI gateway-extra.openapi_Gateway API
  slug: fireworks-ai-gateway-extra-openapi-gateway-api
- description: The gateway.openapi_Gateway API from Fireworks AI — 126 operation(s) for gateway.openapi_gateway.
  name: Fireworks AI gateway.openapi_Gateway API
  slug: fireworks-ai-gateway-openapi-gateway-api
- description: The Messages API from Fireworks AI — 1 operation(s) for messages.
  name: Fireworks AI Messages API
  slug: fireworks-ai-messages-api
- description: The Responses API from Fireworks AI — 2 operation(s) for responses.
  name: Fireworks AI Responses API
  slug: fireworks-ai-responses-api
- description: The responses.openapi_other API from Fireworks AI — 2 operation(s) for responses.openapi_other.
  name: Fireworks AI responses.openapi_other API
  slug: fireworks-ai-responses-openapi-other-api
- description: The text-completion.openapi_other API from Fireworks AI — 2 operation(s) for text-completion.openapi_other.
  name: Fireworks AI text-completion.openapi_other API
  slug: fireworks-ai-text-completion-openapi-other-api
artifact_total: 35
asyncapis:
- description: AsyncAPI description of the Fireworks AI streaming inference surface. Fireworks streams generation deltas over HTTP using Server-Sent Events (SSE) on a single `text/event-stream` response when `stream
  name: Fireworks AI Streaming Inference API
  slug: fireworks-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other API
  slug: open-fireworks-ai-anthropic-messages-openapi-other-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages API
  slug: open-fireworks-ai-anthropic-messages
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other Chat API
  slug: open-fireworks-ai-chat-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other Completions API
  slug: open-fireworks-ai-completions-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other Gateway API
  slug: open-fireworks-ai-gateway-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other gateway-extra.openapi_Gateway API
  slug: open-fireworks-ai-gateway-extra-openapi-gateway-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other gateway.openapi_Gateway API
  slug: open-fireworks-ai-gateway-openapi-gateway-api
- collection_type: open
  name: Gateway REST API
  slug: open-fireworks-ai-gateway
- collection_type: open
  name: Gateway REST API
  slug: open-fireworks-ai-merged
- collection_type: open
  name: Fireworks AI Anthropic Compatible anthropic-.openapi_other Messages API
  slug: open-fireworks-ai-messages-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other Responses API
  slug: open-fireworks-ai-responses-api
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other responses.openapi_other API
  slug: open-fireworks-ai-responses-openapi-other-api
- collection_type: open
  name: Fireworks Responses API
  slug: open-fireworks-ai-responses
- collection_type: open
  name: Fireworks AI Anthropic Compatible Messages anthropic-messages.openapi_other text-completion.openapi_other API
  slug: open-fireworks-ai-text-completion-openapi-other-api
- collection_type: open
  name: Fireworks Text Completion API
  slug: open-fireworks-ai-text-completion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fireworks-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fireworks-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fireworks-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fw-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fireworks-ai
- group: company
  title: ''
  type: Website
  url: https://fireworks.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fireworks.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/fireworks-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fireworks-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fireworks-ai-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.fireworks.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://fireworks.ai/blog
created: '2026-05-08'
description: Fireworks AI is a production-grade inference platform for open-source and proprietary generative models. The Fireworks API hosts Llama, DeepSeek, Qwen, Mixtral, Stable Diffusion, and other models with serverless pay-per-token, on-demand dedicated GPU, and batch deployment options, plus managed fine-tuning.
finops:
- name: Fireworks Ai Finops
  service_category: AI and Machine Learning
  slug: fireworks-ai-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Fireworks AI fast inference platform. The schema is derived from the public Fireworks AI REST API surface documented at https://docs.firewor
  name: Fireworks AI GraphQL Schema
  slug: fireworks-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fireworks-ai.png
layout: provider
modified: '2026-05-29'
name: Fireworks AI
nav: Providers
network: true
overview: 'Fireworks AI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including anthropic-messages.openapi_other API, Chat API, Completions API, and 7 more. Tagged areas include Artificial Intelligence, LLM, Inference, Multi-Modal, and Fine-Tuning.


  The Fireworks AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fireworks AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Fireworks Ai Plans Pricing
  plan_count: 5
  slug: fireworks-ai-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Fireworks Ai Rate Limits
  slug: fireworks-ai-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Fireworks AI API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: fireworks-ai-asyncapi-spectral-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 62.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 57.0
    developer_ergonomics: 31.0
    discoverability: 81.5
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 20.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fireworks-ai/refs/heads/main/screenshots/fireworks-ai-2026-06-20T181235.png
security:
- kind: authentication
  name: Fireworks Ai Authentication
  slug: fireworks-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fireworks Ai Domain Security
  slug: fireworks-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fireworks-ai
tags:
- Artificial Intelligence
- LLM
- Inference
- Multi-Modal
- Fine-Tuning
- GPU
website: https://fireworks.ai/
---
