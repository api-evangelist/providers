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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Mlflow Agentic Access
  operation_count: 23
  slug: mlflow-agentic-access
  summary_line: 23 operations · 17 acting
api_count: 8
apis:
- description: The MLflow tracking server exposes a REST API for experiments, runs, parameters, metrics, tags, registered models, model versions, model aliases, and artifacts, plus newer endpoints for traces, prompt
  name: MLflow REST API
  slug: mlflow-tracking-rest-api
- description: The MLflow AI Gateway provides a unified HTTP interface to LLM providers with routing, rate-limiting, and secret management features.
  name: MLflow AI Gateway API
  slug: mlflow-gateway-api
- description: List and obtain presigned URLs for run artifacts.
  name: MLflow Artifacts API
  slug: mlflow-artifacts-api
- description: Manage MLflow experiments.
  name: MLflow Experiments API
  slug: mlflow-experiments-api
- description: Log and retrieve metric history for runs.
  name: MLflow Metrics API
  slug: mlflow-metrics-api
- description: Manage versions of registered models.
  name: MLflow Model Versions API
  slug: mlflow-model-versions-api
- description: Manage registered models in the MLflow Model Registry.
  name: MLflow Registered Models API
  slug: mlflow-registered-models-api
- description: Create and manage runs within an experiment.
  name: MLflow Runs API
  slug: mlflow-runs-api
artifact_total: 15
collections:
- collection_type: open
  name: MLflow Tracking REST API
  slug: open-mlflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mlflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mlflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mlflow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mlflow-org
- group: company
  title: ''
  type: Website
  url: https://mlflow.org/
- group: start
  title: ''
  type: Portal
  url: https://mlflow.org/docs/latest/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mlflow/mlflow
- group: commercial
  title: ''
  type: License
  url: https://github.com/mlflow/mlflow/blob/master/LICENSE.txt
- group: other
  title: Databricks Managed MLflow
  type: CommercialOffering
  url: https://www.databricks.com/product/managed-mlflow
- group: commercial
  title: ''
  type: Plans
  url: plans/mlflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mlflow-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mlflow-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://mlflow.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://mlflow.org/blog/rss.xml
created: '2026-05-08'
description: 'MLflow is an Apache 2.0 open-source platform for the end-to-end ML and GenAI lifecycle: tracking, model registry, deployment, evaluation, traces, prompts, and GenAI gateway. The tracking server exposes a REST API under `/api/2.0/mlflow`.'
finops:
- name: Mlflow Finops
  service_category: ML
  slug: mlflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mlflow.png
layout: provider
modified: '2026-05-08'
name: MLflow
nav: Providers
network: true
overview: 'MLflow publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Experiments API, Metrics API, and 3 more. Tagged areas include ML, MLOps, GenAI, Experiment Tracking, and Open Source.


  MLflow''s developer surface includes authentication, developer portal, engineering blog, and 11 more developer resources.'
plans:
- name: Mlflow Plans Pricing
  plan_count: 1
  slug: mlflow-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 1
  name: Mlflow Rate Limits
  slug: mlflow-rate-limits
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mlflow/refs/heads/main/screenshots/mlflow-2026-06-20T185626.png
security:
- kind: authentication
  name: Mlflow Authentication
  slug: mlflow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mlflow Domain Security
  slug: mlflow-domain-security
  summary_line: TLSv1.3
slug: mlflow
tags:
- ML
- MLOps
- GenAI
- Experiment Tracking
- Open Source
website: https://mlflow.org/
---
