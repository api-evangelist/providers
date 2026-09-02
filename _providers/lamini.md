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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Lamini Agentic Access
  operation_count: 12
  slug: lamini-agentic-access
  summary_line: 12 operations · 9 acting
api_count: 1
apis:
- description: LLM classifier classification and prediction endpoints.
  name: Lamini Classify API
  slug: lamini-classify-api
- description: Text embedding generation.
  name: Lamini Embeddings API
  slug: lamini-embeddings-api
- description: Tuning and Memory Tuning job submission and management.
  name: Lamini Fine-Tuning API
  slug: lamini-fine-tuning-api
- description: Text completion and streaming generation endpoints.
  name: Lamini Inference API
  slug: lamini-inference-api
- description: Version and platform metadata endpoints.
  name: Lamini Platform API
  slug: lamini-platform-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lamini Platform Classify API
  slug: open-lamini-classify-api
- collection_type: open
  name: Lamini Platform Classify Embeddings API
  slug: open-lamini-embeddings-api
- collection_type: open
  name: Lamini Platform Classify Fine-Tuning API
  slug: open-lamini-fine-tuning-api
- collection_type: open
  name: Lamini Platform Classify Inference API
  slug: open-lamini-inference-api
- collection_type: open
  name: Lamini Classify Platform API
  slug: open-lamini-platform-api
- collection_type: open
  name: Lamini Platform API
  slug: open-lamini
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lamini-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lamini-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lamini-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lamini-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lamini-ai
- group: company
  title: ''
  type: Website
  url: https://www.lamini.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lamini.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/lamini-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lamini-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lamini-finops.yml
created: '2026-06-20'
description: Lamini is an enterprise LLM platform for fine-tuning, tuning, and serving custom open models. Its Memory Tuning approach embeds factual recall into models to reduce hallucination, and the platform exposes a REST API for inference (completions), fine-tuning jobs, classification, and embeddings over open base models, deployable in Lamini's cloud, on-demand GPU cluster, or on-premises.
finops:
- name: Lamini Finops
  service_category: AI and Machine Learning
  slug: lamini-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lamini.png
layout: provider
modified: '2026-06-20'
name: Lamini
nav: Providers
network: true
overview: 'Lamini publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Classify API, Embeddings API, Fine-Tuning API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Fine-Tuning, Memory Tuning, and Inference.


  Lamini''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Lamini Plans Pricing
  plan_count: 2
  slug: lamini-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Lamini Rate Limits
  slug: lamini-rate-limits
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lamini/refs/heads/main/screenshots/lamini-2026-06-20T184254.png
security:
- kind: authentication
  name: Lamini Authentication
  slug: lamini-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lamini Domain Security
  slug: lamini-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lamini
tags:
- Artificial Intelligence
- LLM
- Fine-Tuning
- Memory Tuning
- Inference
website: https://www.lamini.ai
---
