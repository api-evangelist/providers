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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Keywordsai Agentic Access
  operation_count: 20
  slug: keywordsai-agentic-access
  summary_line: 20 operations · 15 acting
api_count: 9
apis:
- description: Datasets and dataset logs.
  name: Keywords AI Datasets API
  slug: keywordsai-datasets-api
- description: Output-scoring evaluators.
  name: Keywords AI Evaluators API
  slug: keywordsai-evaluators-api
- description: Prompt / model experiments.
  name: Keywords AI Experiments API
  slug: keywordsai-experiments-api
- description: OpenAI-compatible LLM proxy (chat completions).
  name: Keywords AI Gateway API
  slug: keywordsai-gateway-api
- description: Asynchronous request / span logging.
  name: Keywords AI Logging API
  slug: keywordsai-logging-api
- description: Prompt and prompt-version management.
  name: Keywords AI Prompts API
  slug: keywordsai-prompts-api
- description: Multi-turn conversation threads.
  name: Keywords AI Threads API
  slug: keywordsai-threads-api
- description: OpenTelemetry-aligned distributed traces.
  name: Keywords AI Traces API
  slug: keywordsai-traces-api
- description: End-user (customer) analytics.
  name: Keywords AI Users API
  slug: keywordsai-users-api
artifact_total: 19
asyncapis:
- description: AsyncAPI 2.6 description of Keywords AI's **chat completion streaming** surface on the OpenAI-compatible gateway. Keywords AI does not publish a WebSocket API. The only asynchronous / event-style tran
  name: Keywords AI Chat Completions Streaming (HTTP + SSE)
  slug: keywordsai-asyncapi
collections:
- collection_type: open
  name: Keywords AI API
  slug: open-keywordsai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keywordsai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/keywordsai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keywordsai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keywordsai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Keywords-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keywordsai
- group: company
  title: ''
  type: Website
  url: https://www.keywordsai.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.keywordsai.co
- group: commercial
  title: ''
  type: Plans
  url: plans/keywordsai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keywordsai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/keywordsai-finops.yml
created: '2026-06-20'
description: Keywords AI is an LLM observability and gateway platform. It exposes an OpenAI-compatible proxy (chat completions across 250+ models) plus REST APIs for request logging, prompt management, threads, evaluations, and traces - all under a single Bearer-authenticated API at https://api.keywordsai.co/api. (The company is rebranding to Respan; the keywordsai.co host and API remain active.)
finops:
- name: Keywordsai Finops
  service_category: AI and Machine Learning
  slug: keywordsai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keywordsai.png
layout: provider
modified: '2026-06-20'
name: Keywords AI
nav: Providers
network: true
overview: 'Keywords AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Evaluators API, Experiments API, and 6 more. Tagged areas include AI, LLM, Observability, Gateway, and Monitoring.


  The Keywords AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Keywords AI''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Keywordsai Plans Pricing
  plan_count: 3
  slug: keywordsai-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 4
  name: Keywordsai Rate Limits
  slug: keywordsai-rate-limits
rules:
- name: Keywords AI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: keywordsai-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.0
  delta: -3.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 65.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keywordsai/refs/heads/main/screenshots/keywordsai-2026-06-20T184016.png
security:
- kind: authentication
  name: Keywordsai Authentication
  slug: keywordsai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Keywordsai Domain Security
  slug: keywordsai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Keywordsai Trust Center
  slug: keywordsai-trust-center
  summary_line: HIPAA, GDPR
slug: keywordsai
tags:
- AI
- LLM
- Observability
- Gateway
- Monitoring
website: https://www.keywordsai.co
---
