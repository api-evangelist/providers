---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Weights And Biases Agentic Access
  operation_count: 29
  slug: weights-and-biases-agentic-access
  summary_line: 29 operations · 27 acting
api_count: 1
apis:
- description: The W&B Public API is a GraphQL endpoint at `https://api.wandb.ai/graphql`. It backs the Python `wandb.Api()` SDK and exposes runs, projects, sweeps, artifacts, reports, registries, and automations. A
  name: W&B GraphQL API
  slug: wandb-graphql-api
- description: The wandb client uses an HTTP file/import endpoint to push run metrics, system stats, and artifacts. Generally accessed through the SDK rather than directly.
  name: W&B Import API (HTTP)
  slug: wandb-import-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Calls API from Weights & Biases — 8 operation(s) for calls.
  name: Weights & Biases Calls API
  slug: weights-and-biases-calls-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Costs API from Weights & Biases — 3 operation(s) for costs.
  name: Weights & Biases Costs API
  slug: weights-and-biases-costs-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Feedback API from Weights & Biases — 4 operation(s) for feedback.
  name: Weights & Biases Feedback API
  slug: weights-and-biases-feedback-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Files API from Weights & Biases — 2 operation(s) for files.
  name: Weights & Biases Files API
  slug: weights-and-biases-files-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Objects API from Weights & Biases — 4 operation(s) for objects.
  name: Weights & Biases Objects API
  slug: weights-and-biases-objects-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Refs API from Weights & Biases — 1 operation(s) for refs.
  name: Weights & Biases Refs API
  slug: weights-and-biases-refs-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Service API from Weights & Biases — 2 operation(s) for service.
  name: Weights & Biases Service API
  slug: weights-and-biases-service-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Table API from Weights & Biases — 1 operation(s) for table.
  name: Weights & Biases Table API
  slug: weights-and-biases-table-api
- baseURL: https://api.wandb.ai/graphql
  baseurl_source: declared
  description: The Tables API from Weights & Biases — 4 operation(s) for tables.
  name: Weights & Biases Tables API
  slug: weights-and-biases-tables-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fast Calls API
  slug: open-weights-and-biases-calls-api
- collection_type: open
  name: Fast Calls Costs API
  slug: open-weights-and-biases-costs-api
- collection_type: open
  name: Fast Calls Feedback API
  slug: open-weights-and-biases-feedback-api
- collection_type: open
  name: Fast Calls Files API
  slug: open-weights-and-biases-files-api
- collection_type: open
  name: Fast Calls Objects API
  slug: open-weights-and-biases-objects-api
- collection_type: open
  name: Fast Calls Refs API
  slug: open-weights-and-biases-refs-api
- collection_type: open
  name: Fast Calls Service API
  slug: open-weights-and-biases-service-api
- collection_type: open
  name: Fast Calls Table API
  slug: open-weights-and-biases-table-api
- collection_type: open
  name: Fast Calls Tables API
  slug: open-weights-and-biases-tables-api
- collection_type: open
  name: FastAPI
  slug: open-weights-and-biases
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/wandb/wandb/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/wandb/wandb/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/wandb/wandb/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/wandb/wandb/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/wandb/wandb/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/wandb/wandb/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weights-and-biases-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weights-and-biases-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weights-and-biases-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weights-and-biases-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wandb.ai/
- group: start
  title: ''
  type: Portal
  url: https://docs.wandb.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://wandb.ai/site/pricing
- group: build
  title: wandb client
  type: SourceCode
  url: https://github.com/wandb/wandb
- group: commercial
  title: ''
  type: Plans
  url: plans/weights-and-biases-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weights-and-biases-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weights-and-biases-finops.yml
created: '2026-05-08'
description: Weights & Biases is the ML developer platform for experiment tracking, model registry, artifact management, sweeps, reports, and (Weave) GenAI evaluation. The W&B API is primarily a GraphQL endpoint, surfaced through a Python `wandb.Api` SDK.
finops:
- name: Weights And Biases Finops
  service_category: ML
  slug: weights-and-biases-finops
graphqls:
- description: The W&B Public API is a GraphQL endpoint at `https://api.wandb.ai/graphql`. It backs the Python `wandb.Api()` SDK and exposes runs, projects, sweeps, artifacts, reports, registries, and automations. A
  name: Weights & Biases GraphQL API
  slug: weights-and-biases-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weights-and-biases.png
layout: provider
modified: '2026-05-08'
name: Weights & Biases
nav: Providers
network: true
overview: 'Weights & Biases publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Costs API, Feedback API, and 6 more. Tagged areas include ML, MLOps, Experiment Tracking, Model Registry, and GenAI.


  Weights & Biases'' developer surface includes authentication, developer portal, pricing, and 14 more developer resources.'
plans:
- name: Weights And Biases Plans Pricing
  plan_count: 1
  slug: weights-and-biases-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Weights And Biases Rate Limits
  slug: weights-and-biases-rate-limits
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weights-and-biases/refs/heads/main/screenshots/weights-and-biases-2026-06-20T201349.png
security:
- kind: authentication
  name: Weights And Biases Authentication
  slug: weights-and-biases-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Weights And Biases Domain Security
  slug: weights-and-biases-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Weights And Biases Vulnerability Disclosure
  slug: weights-and-biases-vulnerability-disclosure
  summary_line: disclosure policy published
slug: weights-and-biases
tags:
- ML
- MLOps
- Experiment Tracking
- Model Registry
- GenAI
website: https://wandb.ai/
---
