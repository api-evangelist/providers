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
- acting_count: 5
  human_in_the_loop: 0
  name: Kubeflow Agentic Access
  operation_count: 13
  slug: kubeflow-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 8
apis:
- description: API for tracking and managing metadata, artifacts, and lineage for ML workflows running on Kubeflow.
  name: Kubeflow Metadata API
  slug: metadata-api
- description: Katib is the Kubeflow component for hyperparameter tuning, neural architecture search, and AutoML, exposing a Kubernetes-native API for defining and running tuning experiments.
  name: Katib API
  slug: katib-api
- description: API for managing Jupyter notebook server instances within a Kubeflow cluster, providing isolated, browser-based development environments.
  name: Kubeflow Notebooks API
  slug: notebooks-api
- description: API supporting the Kubeflow central dashboard and UI components, which provide a unified interface to all installed Kubeflow components.
  name: Kubeflow Central Dashboard API
  slug: central-dashboard
- description: Group runs and recurring jobs into logical experiments
  name: Kubeflow Experiments API
  slug: kubeflow-experiments-api
- description: Health and auth checks
  name: Kubeflow Health API
  slug: kubeflow-health-api
- description: Manage pipeline definitions
  name: Kubeflow Pipelines API
  slug: kubeflow-pipelines-api
- description: Manage versions of pipelines
  name: Kubeflow PipelineVersions API
  slug: kubeflow-pipelineversions-api
artifact_total: 15
collections:
- collection_type: open
  name: Kubeflow Pipelines API
  slug: open-kubeflow
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kubeflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kubeflow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kubeflow-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kubeflow
- group: company
  title: ''
  type: Website
  url: https://www.kubeflow.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.kubeflow.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kubeflow.org/docs/started/
- group: company
  title: ''
  type: Blog
  url: https://blog.kubeflow.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kubeflow
- group: operate
  title: ''
  type: Community
  url: https://www.kubeflow.org/docs/about/community/
created: '2024-01-15'
description: Kubeflow is an open-source machine learning platform for Kubernetes, designed to make deployments of ML workflows on Kubernetes simple, portable, and scalable. It provides tools for training, serving, tuning, and managing ML models across the full lifecycle.
finops:
- name: Kubeflow Finops
  service_category: API
  slug: kubeflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubeflow.png
layout: provider
modified: '2026-04-28'
name: Kubeflow
nav: Providers
network: true
overview: 'Kubeflow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Experiments API, Health API, Pipelines API, and 1 more. Tagged areas include AI, Deep Learning, Kubernetes, Machine Learning, and MLOps.


  Kubeflow''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Kubeflow Plans Pricing
  plan_count: 3
  slug: kubeflow-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Kubeflow Rate Limits
  slug: kubeflow-rate-limits
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.3
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kubeflow/refs/heads/main/screenshots/kubeflow-2026-06-20T184203.png
security:
- kind: authentication
  name: Kubeflow Authentication
  slug: kubeflow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kubeflow Domain Security
  slug: kubeflow-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kubeflow
tags:
- AI
- Deep Learning
- Kubernetes
- Machine Learning
- MLOps
- Model Serving
- Model Training
- Open Source
website: https://www.kubeflow.org
---
