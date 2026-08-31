---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Requesty Agentic Access
  operation_count: 10
  slug: requesty-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: Programmatic management of Requesty API keys.
  name: Requesty API Keys API
  slug: requesty-api-keys-api
- description: OpenAI-compatible chat completions routed across providers.
  name: Requesty Chat API
  slug: requesty-chat-api
- description: Vector embedding generation.
  name: Requesty Embeddings API
  slug: requesty-embeddings-api
- description: Catalog of routable models.
  name: Requesty Models API
  slug: requesty-models-api
- description: Usage statistics and spend reporting.
  name: Requesty Usage API
  slug: requesty-usage-api
artifact_total: 22
asyncapis:
- description: AsyncAPI 2.6 description of Requesty's **chat completion streaming** surface. Requesty does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.reques
  name: Requesty Chat Completions Streaming (HTTP + SSE)
  slug: requesty-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Requesty Router API Keys API
  slug: open-requesty-api-keys-api
- collection_type: open
  name: Requesty Router API Keys Chat API
  slug: open-requesty-chat-api
- collection_type: open
  name: Requesty Router API Keys Embeddings API
  slug: open-requesty-embeddings-api
- collection_type: open
  name: Requesty Router API Keys Models API
  slug: open-requesty-models-api
- collection_type: open
  name: Requesty Router API Keys Usage API
  slug: open-requesty-usage-api
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
overview: 'Requesty publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Chat API, Embeddings API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Routing, Gateway, and Observability.


  The Requesty catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Requesty''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Requesty Plans Pricing
  plan_count: 3
  slug: requesty-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Requesty Rate Limits
  slug: requesty-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Requesty API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: requesty-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 11.4
    contract_quality: 61.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
- Artificial Intelligence
- LLM
- Routing
- Gateway
- Observability
website: https://www.requesty.ai
---
