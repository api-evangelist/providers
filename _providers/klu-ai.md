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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Klu Ai Agentic Access
  operation_count: 14
  slug: klu-ai-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 8
apis:
- description: Run Actions to generate completions.
  name: Klu Actions API
  slug: klu-ai-actions-api
- description: Apps (projects) grouping Actions, context, and experiments.
  name: Klu Apps API
  slug: klu-ai-apps-api
- description: Manage Context libraries and documents for retrieval-augmented generation.
  name: Klu Context API
  slug: klu-ai-context-api
- description: Data points produced by Action generations.
  name: Klu Data API
  slug: klu-ai-data-api
- description: Ratings, corrections, and issues attached to data points.
  name: Klu Feedback API
  slug: klu-ai-feedback-api
- description: LLM providers and models available in the workspace.
  name: Klu Models API
  slug: klu-ai-models-api
- description: Session memory for multi-turn conversations.
  name: Klu Sessions API
  slug: klu-ai-sessions-api
- description: Workspace administration.
  name: Klu Workspaces API
  slug: klu-ai-workspaces-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Klu Actions API
  slug: open-klu-ai-actions-api
- collection_type: open
  name: Klu Actions Apps API
  slug: open-klu-ai-apps-api
- collection_type: open
  name: Klu Actions Context API
  slug: open-klu-ai-context-api
- collection_type: open
  name: Klu Actions Data API
  slug: open-klu-ai-data-api
- collection_type: open
  name: Klu Actions Feedback API
  slug: open-klu-ai-feedback-api
- collection_type: open
  name: Klu Actions Models API
  slug: open-klu-ai-models-api
- collection_type: open
  name: Klu Actions Sessions API
  slug: open-klu-ai-sessions-api
- collection_type: open
  name: Klu Actions Workspaces API
  slug: open-klu-ai-workspaces-api
- collection_type: open
  name: Klu API
  slug: open-klu-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/klu-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klu-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klu-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klu-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klu-ai
- group: company
  title: ''
  type: Website
  url: https://klu.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.klu.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/klu-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/klu-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/klu-ai-finops.yml
created: '2026-06-20'
description: Klu (klu.ai) is an LLM app platform for designing, deploying, evaluating, and observing prompt-driven AI applications. The Klu Engine exposes a REST API at https://api.klu.ai/v1 (Bearer API key) where an Action encapsulates a prompt template, model config, context (RAG), and output parsing, and is invoked to generate completions, with data, feedback, sessions, and models managed alongside it. NOTE - product development appears dormant - the official klu SDK last shipped in March 2025 and the founding team's recent open-source work has shifted toward xAI / Grok tooling - see review.yml for the honest status assessment.
finops:
- name: Klu Ai Finops
  service_category: AI and Machine Learning
  slug: klu-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klu-ai.png
layout: provider
modified: '2026-06-20'
name: Klu
nav: Providers
network: true
overview: 'Klu publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Apps API, Context API, and 5 more. Tagged areas include Artificial Intelligence, LLM, LLM App Platform, Prompt Engineering, and Evaluation.


  Klu''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Klu Ai Plans Pricing
  plan_count: 3
  slug: klu-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Klu Ai Rate Limits
  slug: klu-ai-rate-limits
score:
  band: developing
  composite: 39.9
  delta: 2.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.0
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/klu-ai/refs/heads/main/screenshots/klu-ai-2026-06-20T184105.png
security:
- kind: authentication
  name: Klu Ai Authentication
  slug: klu-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Klu Ai Domain Security
  slug: klu-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: klu-ai
tags:
- Artificial Intelligence
- LLM
- LLM App Platform
- Prompt Engineering
- Evaluation
- Observability
website: https://klu.ai
---
