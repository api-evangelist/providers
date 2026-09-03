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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Deepseek Agentic Access
  operation_count: 4
  slug: deepseek-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- baseURL: https://api.deepseek.com
  baseurl_source: declared
  description: The Chat API from DeepSeek — 1 operation(s) for chat.
  name: DeepSeek Chat API
  slug: deepseek-chat-api
- baseURL: https://api.deepseek.com
  baseurl_source: declared
  description: The Completions API from DeepSeek — 1 operation(s) for completions.
  name: DeepSeek Completions API
  slug: deepseek-completions-api
- baseURL: https://api.deepseek.com
  baseurl_source: declared
  description: The Models API from DeepSeek — 1 operation(s) for models.
  name: DeepSeek Models API
  slug: deepseek-models-api
- baseURL: https://api.deepseek.com
  baseurl_source: declared
  description: The User API from DeepSeek — 1 operation(s) for user.
  name: DeepSeek User API
  slug: deepseek-user-api
artifact_total: 26
asyncapis:
- description: AsyncAPI definition for the streaming surface of the DeepSeek API. DeepSeek exposes an OpenAI-compatible HTTP API. When the `stream` request parameter is set to `true`, the server upgrades the respons
  name: DeepSeek Streaming API (HTTP + SSE)
  slug: deepseek-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DeepSeek Completion Chat API
  slug: open-deepseek-chat-api
- collection_type: open
  name: DeepSeek Chat Completion API
  slug: open-deepseek-chat-completion-api
- collection_type: open
  name: DeepSeek Completion Chat Completions API
  slug: open-deepseek-completions-api
- collection_type: open
  name: DeepSeek FIM Completion
  slug: open-deepseek-fim-completion
- collection_type: open
  name: DeepSeek Models API
  slug: open-deepseek-lists-models-api
- collection_type: open
  name: DeepSeek Completion Chat Models API
  slug: open-deepseek-models-api
- collection_type: open
  name: DeepSeek Completion Chat User API
  slug: open-deepseek-user-api
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
overview: 'DeepSeek publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Models API, and 1 more. Tagged areas include Artificial Intelligence, Chat, Chat Completion, LLM, and Large Language Models.


  The DeepSeek catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 5 Spectral governance rulesets.


  DeepSeek''s developer surface includes authentication, documentation, pricing, FAQ, changelog, and 13 more developer resources.'
plans:
- name: Deepseek Plans Pricing
  plan_count: 2
  slug: deepseek-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Deepseek Rate Limits
  slug: deepseek-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: DeepSeek API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: deepseek-asyncapi-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: DeepSeek API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: deepseek-chat-completion-api-rules
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: DeepSeek API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: deepseek-fim-completion-rules
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: DeepSeek API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: deepseek-lists-models-api-rules
- effective_rule_count: 44
  extends:
  - spectral:oas
  name: DeepSeek API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: deepseek-user-balance-api-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 51.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 26.5
    contract_quality: 60.7
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 26.5
    operational_transparency: 23.7
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Artificial Intelligence
- Chat
- Chat Completion
- LLM
- Large Language Models
- Reasoning
- Code Completion
website: https://www.deepseek.com/
---
