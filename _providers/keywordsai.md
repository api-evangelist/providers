---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.keywordsai.co'', ''status'': 301, ''note'': ''declared website redirects to https://www.respan.ai/ — a different registrable domain (keywordsai.co -> respan.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Keywordsai Agentic Access
  operation_count: 20
  slug: keywordsai-agentic-access
  summary_line: 20 operations · 15 acting
api_count: 1
apis:
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: Datasets and dataset logs.
  name: Keywords AI Datasets API
  slug: keywordsai-datasets-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: Output-scoring evaluators.
  name: Keywords AI Evaluators API
  slug: keywordsai-evaluators-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: Prompt / model experiments.
  name: Keywords AI Experiments API
  slug: keywordsai-experiments-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: OpenAI-compatible LLM proxy (chat completions).
  name: Keywords AI Gateway API
  slug: keywordsai-gateway-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: Asynchronous request / span logging.
  name: Keywords AI Logging API
  slug: keywordsai-logging-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: Prompt and prompt-version management.
  name: Keywords AI Prompts API
  slug: keywordsai-prompts-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: Multi-turn conversation threads.
  name: Keywords AI Threads API
  slug: keywordsai-threads-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: OpenTelemetry-aligned distributed traces.
  name: Keywords AI Traces API
  slug: keywordsai-traces-api
- baseURL: https://api.keywordsai.co/api
  baseurl_source: declared
  description: End-user (customer) analytics.
  name: Keywords AI Users API
  slug: keywordsai-users-api
artifact_total: 29
asyncapis:
- description: AsyncAPI 2.6 description of Keywords AI's **chat completion streaming** surface on the OpenAI-compatible gateway. Keywords AI does not publish a WebSocket API. The only asynchronous / event-style tran
  name: Keywords AI Chat Completions Streaming (HTTP + SSE)
  slug: keywordsai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Keywords AI Datasets API
  slug: open-keywordsai-datasets-api
- collection_type: open
  name: Keywords AI Datasets Evaluators API
  slug: open-keywordsai-evaluators-api
- collection_type: open
  name: Keywords AI Datasets Experiments API
  slug: open-keywordsai-experiments-api
- collection_type: open
  name: Keywords AI Datasets Gateway API
  slug: open-keywordsai-gateway-api
- collection_type: open
  name: Keywords AI Datasets Logging API
  slug: open-keywordsai-logging-api
- collection_type: open
  name: Keywords AI Datasets Prompts API
  slug: open-keywordsai-prompts-api
- collection_type: open
  name: Keywords AI Datasets Threads API
  slug: open-keywordsai-threads-api
- collection_type: open
  name: Keywords AI Datasets Traces API
  slug: open-keywordsai-traces-api
- collection_type: open
  name: Keywords AI Datasets Users API
  slug: open-keywordsai-users-api
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
overview: 'Keywords AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Evaluators API, Experiments API, and 6 more. Tagged areas include Artificial Intelligence, LLM, Observability, Gateway, and Monitoring.


  The Keywords AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Keywords AI''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Keywordsai Plans Pricing
  plan_count: 3
  slug: keywordsai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Keywordsai Rate Limits
  slug: keywordsai-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Keywords AI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: keywordsai-asyncapi-spectral-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 67.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 11.4
    contract_quality: 60.7
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
- LLM
- Observability
- Gateway
- Monitoring
website: https://www.keywordsai.co
---
