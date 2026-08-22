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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Predibase Agentic Access
  operation_count: 23
  slug: predibase-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 7
apis:
- description: The Adapters API from Predibase — 2 operation(s) for adapters.
  name: Predibase Adapters API
  slug: predibase-adapters-api
- description: The Batch Inference API from Predibase — 2 operation(s) for batch inference.
  name: Predibase Batch Inference API
  slug: predibase-batch-inference-api
- description: The Datasets API from Predibase — 2 operation(s) for datasets.
  name: Predibase Datasets API
  slug: predibase-datasets-api
- description: The Deployments API from Predibase — 2 operation(s) for deployments.
  name: Predibase Deployments API
  slug: predibase-deployments-api
- description: The Fine-Tuning API from Predibase — 3 operation(s) for fine-tuning.
  name: Predibase Fine-Tuning API
  slug: predibase-fine-tuning-api
- description: The Inference API from Predibase — 4 operation(s) for inference.
  name: Predibase Inference API
  slug: predibase-inference-api
- description: The Models API from Predibase — 1 operation(s) for models.
  name: Predibase Models API
  slug: predibase-models-api
artifact_total: 24
asyncapis:
- description: AsyncAPI 2.6 description of Predibase's **inference streaming** surface. Predibase does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.predibase.
  name: Predibase Inference Streaming (HTTP + SSE)
  slug: predibase-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Predibase Adapters API
  slug: open-predibase-adapters-api
- collection_type: open
  name: Predibase Adapters Batch Inference API
  slug: open-predibase-batch-inference-api
- collection_type: open
  name: Predibase Adapters Datasets API
  slug: open-predibase-datasets-api
- collection_type: open
  name: Predibase Adapters Deployments API
  slug: open-predibase-deployments-api
- collection_type: open
  name: Predibase Adapters Fine-Tuning API
  slug: open-predibase-fine-tuning-api
- collection_type: open
  name: Predibase Adapters Inference API
  slug: open-predibase-inference-api
- collection_type: open
  name: Predibase Adapters Models API
  slug: open-predibase-models-api
- collection_type: open
  name: Predibase API
  slug: open-predibase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/predibase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/predibase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/predibase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/predibase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/predibase
- group: company
  title: ''
  type: Website
  url: https://predibase.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.predibase.com
- group: commercial
  title: ''
  type: Plans
  url: plans/predibase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/predibase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/predibase-finops.yml
created: '2026-06-20'
description: Predibase is a platform for fine-tuning and serving open-source LLMs. It pairs efficient LoRA / Turbo LoRA supervised and reinforcement (GRPO) fine-tuning with serverless and dedicated inference powered by LoRAX, the open-source multi-LoRA serving stack that packs hundreds of adapters onto a single GPU. Inference is exposed through an OpenAI-compatible API plus native generate endpoints.
finops:
- name: Predibase Finops
  service_category: AI and Machine Learning
  slug: predibase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/predibase.png
layout: provider
modified: '2026-06-20'
name: Predibase
nav: Providers
network: true
overview: 'Predibase publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Adapters API, Batch Inference API, Datasets API, and 4 more. Tagged areas include AI, LLM, Fine-Tuning, Inference, and LoRA.


  The Predibase catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Predibase''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Predibase Plans Pricing
  plan_count: 4
  slug: predibase-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Predibase Rate Limits
  slug: predibase-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Predibase API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: predibase-asyncapi-spectral-rules
score:
  band: developing
  composite: 40.3
  delta: -4.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 59.6
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/predibase/refs/heads/main/screenshots/predibase-2026-06-20T192044.png
security:
- kind: authentication
  name: Predibase Authentication
  slug: predibase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Predibase Domain Security
  slug: predibase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: predibase
tags:
- AI
- LLM
- Fine-Tuning
- Inference
- LoRA
website: https://predibase.com
---
