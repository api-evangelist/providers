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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Targon Agentic Access
  operation_count: 6
  slug: targon-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.targon.com/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completions.
  name: Targon Chat API
  slug: targon-chat-api
- baseURL: https://api.targon.com/v1
  baseurl_source: declared
  description: OpenAI-compatible legacy text completions.
  name: Targon Completions API
  slug: targon-completions-api
- baseURL: https://api.targon.com/v1
  baseurl_source: declared
  description: Image generation from a text prompt.
  name: Targon Images API
  slug: targon-images-api
- baseURL: https://api.targon.com/v1
  baseurl_source: declared
  description: List models available on Targon.
  name: Targon Models API
  slug: targon-models-api
- baseURL: https://api.targon.com/v1
  baseurl_source: declared
  description: Query-based search/retrieval.
  name: Targon Search API
  slug: targon-search-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of Targon's **chat completion streaming** surface. Targon is a decentralized AI inference platform operated as Bittensor Subnet 4 by Manifold Labs. It does not publish a WebSo
  name: Targon Chat Completions Streaming (HTTP + SSE)
  slug: targon-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Targon Chat API
  slug: open-targon-chat-api
- collection_type: open
  name: Targon Chat Completions API
  slug: open-targon-completions-api
- collection_type: open
  name: Targon Chat Images API
  slug: open-targon-images-api
- collection_type: open
  name: Targon Chat Models API
  slug: open-targon-models-api
- collection_type: open
  name: Targon Chat Search API
  slug: open-targon-search-api
- collection_type: open
  name: Targon API
  slug: open-targon
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/targon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/targon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/targon-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/manifold-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manifold-labs
- group: company
  title: ''
  type: Website
  url: https://targon.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.targon.com
- group: commercial
  title: ''
  type: Plans
  url: plans/targon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/targon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/targon-finops.yml
created: '2026-06-21'
description: Targon is a decentralized AI inference platform operated as Bittensor Subnet 4 by Manifold Labs. It serves popular open models through an OpenAI-compatible REST API at https://api.targon.com/v1, where a marketplace of miners runs the inference and validators verify responses, giving developers chat, completions, image, and search endpoints over confidential, decentralized compute.
finops:
- name: Targon Finops
  service_category: AI and Machine Learning
  slug: targon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/targon.png
layout: provider
modified: '2026-06-21'
name: Targon
nav: Providers
network: true
overview: 'Targon publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Completions API, Images API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Inference, Decentralized, and Bittensor.


  The Targon catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Targon''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Targon Plans Pricing
  plan_count: 2
  slug: targon-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Targon Rate Limits
  slug: targon-rate-limits
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: Targon API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: targon-asyncapi-spectral-rules
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 63.5
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/targon/refs/heads/main/screenshots/targon-2026-09-02T162642.png
security:
- kind: authentication
  name: Targon Authentication
  slug: targon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Targon Domain Security
  slug: targon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: targon
tags:
- Artificial Intelligence
- LLM
- Inference
- Decentralized
- Bittensor
website: https://targon.com
---
