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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Deepseek Agentic Access
  operation_count: 4
  slug: deepseek-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- description: The Chat API from DeepSeek — 1 operation(s) for chat.
  name: DeepSeek Chat API
  slug: deepseek-chat-api
- description: The Completions API from DeepSeek — 1 operation(s) for completions.
  name: DeepSeek Completions API
  slug: deepseek-completions-api
- description: The Models API from DeepSeek — 1 operation(s) for models.
  name: DeepSeek Models API
  slug: deepseek-models-api
- description: The User API from DeepSeek — 1 operation(s) for user.
  name: DeepSeek User API
  slug: deepseek-user-api
artifact_total: 21
asyncapis:
- description: AsyncAPI definition for the streaming surface of the DeepSeek API. DeepSeek exposes an OpenAI-compatible HTTP API. When the `stream` request parameter is set to `true`, the server upgrades the respons
  name: DeepSeek Streaming API (HTTP + SSE)
  slug: deepseek-asyncapi
collections:
- collection_type: open
  name: DeepSeek Chat Completion API
  slug: open-deepseek-chat-completion-api
- collection_type: open
  name: DeepSeek FIM Completion
  slug: open-deepseek-fim-completion
- collection_type: open
  name: DeepSeek Models API
  slug: open-deepseek-lists-models-api
- collection_type: open
  name: DeepSeek User Balance API
  slug: open-deepseek-user-balance-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepseek-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepseek-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepseek-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepseek-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepseek-ai
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.deepseek.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://api-docs.deepseek.com/quick_start/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://api-docs.deepseek.com/quick_start/token_usage
- group: operate
  title: ''
  type: RateLimits
  url: https://api-docs.deepseek.com/quick_start/rate_limit
- group: design
  title: ''
  type: ErrorCodes
  url: https://api-docs.deepseek.com/quick_start/error_codes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deepseek.com/
- group: operate
  title: ''
  type: FAQ
  url: https://api-docs.deepseek.com/faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-docs.deepseek.com/updates
- group: company
  title: ''
  type: Website
  url: https://www.deepseek.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chat.deepseek.com/downloads/DeepSeek%20Privacy%20Policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chat.deepseek.com/downloads/DeepSeek%20Terms%20of%20Use.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/deepseek-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/deepseek-vocabulary.yml
created: '2025-01-27'
description: DeepSeek is an artificial intelligence company that provides advanced large language models accessible through an API that is compatible with the OpenAI and Anthropic SDKs. The DeepSeek API offers chat completions, fill-in-the-middle completions, function calling, JSON output, streaming, multi-turn conversations, context caching, and a thinking/reasoning mode for complex problem solving.
finops:
- name: Deepseek Finops
  service_category: AI Infrastructure
  slug: deepseek-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepseek.png
jsonld:
- class_count: 6
  name: Deepseek Context
  property_count: 9
  slug: deepseek-context
layout: provider
modified: '2026-05-29'
name: DeepSeek
nav: Providers
network: true
overview: 'DeepSeek publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Models API, and 1 more. Tagged areas include AI, Artificial Intelligence, Chat, Chat Completion, and LLM.


  The DeepSeek catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 5 Spectral governance rulesets.


  DeepSeek''s developer surface includes authentication, documentation, pricing, FAQ, changelog, and 13 more developer resources.'
plans:
- name: Deepseek Plans Pricing
  plan_count: 2
  slug: deepseek-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Deepseek Rate Limits
  slug: deepseek-rate-limits
rules:
- name: DeepSeek API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: deepseek-asyncapi-spectral-rules
- name: DeepSeek API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: deepseek-chat-completion-api-rules
- name: DeepSeek API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: deepseek-fim-completion-rules
- name: DeepSeek API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: deepseek-lists-models-api-rules
- name: DeepSeek API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: deepseek-user-balance-api-rules
score:
  band: developing
  composite: 54.1
  delta: -3.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 57.9
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepseek/refs/heads/main/screenshots/deepseek-2026-06-20T175812.png
security:
- kind: authentication
  name: Deepseek Authentication
  slug: deepseek-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepseek Domain Security
  slug: deepseek-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deepseek
tags:
- AI
- Artificial Intelligence
- Chat
- Chat Completion
- LLM
- Large Language Models
- Reasoning
- Code Completion
website: https://www.deepseek.com/
---
