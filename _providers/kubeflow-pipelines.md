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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kubeflow Pipelines Agentic Access
  operation_count: 13
  slug: kubeflow-pipelines-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 8
apis:
- description: Python SDK for building, compiling, and submitting ML pipelines. Provides decorators and utilities to define pipeline components and workflows using Python.
  name: Kubeflow Pipelines Python SDK
  slug: python-sdk
- description: Go client library for interacting with the Kubeflow Pipelines API programmatically from Go applications.
  name: Kubeflow Pipelines Go Client
  slug: go-client
- description: API for tracking and managing metadata about ML artifacts, executions, and lineage information throughout the ML pipeline lifecycle, backed by ML Metadata (MLMD).
  name: Kubeflow Pipelines Metadata API
  slug: metadata-api
- description: Group runs and recurring jobs into experiments
  name: Kubeflow Pipelines Experiments API
  slug: kubeflow-pipelines-experiments-api
- description: Health and auth checks
  name: Kubeflow Pipelines Health API
  slug: kubeflow-pipelines-health-api
- description: Manage pipeline definitions
  name: Kubeflow Pipelines Pipelines API
  slug: kubeflow-pipelines-pipelines-api
- description: Manage versions of pipelines
  name: Kubeflow Pipelines PipelineVersions API
  slug: kubeflow-pipelines-pipelineversions-api
- description: Pipeline runs
  name: Kubeflow Pipelines Runs API
  slug: kubeflow-pipelines-runs-api
artifact_total: 15
collections:
- collection_type: open
  name: Kubeflow Pipelines REST API
  slug: open-kubeflow-pipelines
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubeflow-pipelines-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubeflow-pipelines-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubeflow-pipelines-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kubeflow
- group: company
  title: ''
  type: Website
  url: https://www.kubeflow.org/docs/components/pipelines/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kubeflow.org/docs/components/pipelines/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kubeflow.org/docs/components/pipelines/getting-started/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kubeflow
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubeflow/pipelines
- group: company
  title: ''
  type: Blog
  url: https://blog.kubeflow.org/
- group: operate
  title: ''
  type: Community
  url: https://www.kubeflow.org/docs/about/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/kubeflow/pipelines/releases
created: '2024-01-01'
description: Kubeflow Pipelines is a platform for building and deploying portable, scalable machine learning workflows based on Docker containers. It provides a way to orchestrate complex ML workflows with dependencies, enabling data scientists and ML engineers to deploy production-ready ML systems on Kubernetes.
finops:
- name: Kubeflow Pipelines Finops
  service_category: API
  slug: kubeflow-pipelines-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubeflow-pipelines.png
layout: provider
modified: '2026-04-28'
name: Kubeflow Pipelines
nav: Providers
network: true
overview: 'Kubeflow Pipelines publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Experiments API, Health API, Pipelines API, and 2 more. Tagged areas include Data Science, Kubernetes, Machine Learning, MLOps, and Orchestration.


  Kubeflow Pipelines'' developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 7 more developer resources.'
plans:
- name: Kubeflow Pipelines Plans Pricing
  plan_count: 3
  slug: kubeflow-pipelines-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 5
  name: Kubeflow Pipelines Rate Limits
  slug: kubeflow-pipelines-rate-limits
score:
  band: developing
  composite: 42.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.5
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubeflow-pipelines/refs/heads/main/screenshots/kubeflow-pipelines-2026-06-20T184205.png
security:
- kind: authentication
  name: Kubeflow Pipelines Authentication
  slug: kubeflow-pipelines-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kubeflow Pipelines Domain Security
  slug: kubeflow-pipelines-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: kubeflow-pipelines
tags:
- Data Science
- Kubernetes
- Machine Learning
- MLOps
- Orchestration
- Pipelines
- Workflows
website: https://www.kubeflow.org/docs/components/pipelines/
---
