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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
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
artifact_total: 15
collections:
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
overview: 'Klu publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Apps API, Context API, and 5 more. Tagged areas include AI, LLM, LLM App Platform, Prompt Engineering, and Evaluation.


  Klu''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Klu Ai Plans Pricing
  plan_count: 3
  slug: klu-ai-plans-pricing
random_paper: 115
rate_limits:
- limit_count: 3
  name: Klu Ai Rate Limits
  slug: klu-ai-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
- AI
- LLM
- LLM App Platform
- Prompt Engineering
- Evaluation
- Observability
website: https://klu.ai
---
