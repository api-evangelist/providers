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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Uptrain Agentic Access
  operation_count: 11
  slug: uptrain-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 6
apis:
- description: The Auth API from UpTrain — 1 operation(s) for auth.
  name: UpTrain Auth API
  slug: uptrain-auth-api
- description: The Checksets API from UpTrain — 1 operation(s) for checksets.
  name: UpTrain Checksets API
  slug: uptrain-checksets-api
- description: The Datasets API from UpTrain — 1 operation(s) for datasets.
  name: UpTrain Datasets API
  slug: uptrain-datasets-api
- description: The Evaluation API from UpTrain — 3 operation(s) for evaluation.
  name: UpTrain Evaluation API
  slug: uptrain-evaluation-api
- description: The Root Cause Analysis API from UpTrain — 1 operation(s) for root cause analysis.
  name: UpTrain Root Cause Analysis API
  slug: uptrain-root-cause-analysis-api
- description: The Runs API from UpTrain — 3 operation(s) for runs.
  name: UpTrain Runs API
  slug: uptrain-runs-api
artifact_total: 13
collections:
- collection_type: open
  name: UpTrain Managed Evaluation API
  slug: open-uptrain
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uptrain-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uptrain-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uptrain-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uptrain-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uptrain-ai
- group: company
  title: ''
  type: Website
  url: https://uptrain.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.uptrain.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/uptrain-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uptrain-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uptrain-finops.yml
created: '2026-06-20'
description: UpTrain is an open-source (Apache-2.0) unified platform to evaluate and improve generative AI and LLM applications. It ships a Python framework plus a managed evaluation API that grades responses against 20+ preconfigured checks - context relevance, factual accuracy, response completeness, hallucination, tonality, prompt injection and more - and performs root cause analysis on failure cases.
finops:
- name: Uptrain Finops
  service_category: AI and Machine Learning
  slug: uptrain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uptrain.png
layout: provider
modified: '2026-06-20'
name: UpTrain
nav: Providers
network: true
overview: 'UpTrain publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Checksets API, Datasets API, and 3 more. Tagged areas include AI, LLM, Evaluation, LLM Evaluation, and Observability.


  UpTrain''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Uptrain Plans Pricing
  plan_count: 2
  slug: uptrain-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 2
  name: Uptrain Rate Limits
  slug: uptrain-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 59.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uptrain/refs/heads/main/screenshots/uptrain-2026-06-20T200550.png
security:
- kind: authentication
  name: Uptrain Authentication
  slug: uptrain-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uptrain Domain Security
  slug: uptrain-domain-security
  summary_line: TLSv1.3 · HSTS
slug: uptrain
tags:
- AI
- LLM
- Evaluation
- LLM Evaluation
- Observability
- Open Source
website: https://uptrain.ai/
---
