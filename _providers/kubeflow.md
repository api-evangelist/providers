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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.2
  scored_at: '2026-08-19'
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kubeflow Pipelines Experiments API
  slug: open-kubeflow-experiments-api
- collection_type: open
  name: Kubeflow Pipelines Experiments Health API
  slug: open-kubeflow-health-api
- collection_type: open
  name: Kubeflow Experiments Pipelines API
  slug: open-kubeflow-pipelines-api
- collection_type: open
  name: Kubeflow Pipelines Experiments PipelineVersions API
  slug: open-kubeflow-pipelineversions-api
- collection_type: open
  name: Kubeflow Pipelines API
  slug: open-kubeflow
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/kubeflow/mcp-server
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://github.com/kubeflow/mcp-server/blob/main/README.md
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/google/ml-metadata/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/google/ml-metadata/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/google/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/google/ml-metadata/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/google/ml-metadata/blob/master/LICENSE
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
mcp_servers:
- description: ''
  name: Kubeflow MCP Server
  slug: kubeflow-mcp-server
modified: '2026-08-15'
name: Kubeflow
nav: Providers
network: true
overview: 'Kubeflow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Experiments API, Health API, Pipelines API, and 1 more. Tagged areas include AI, Deep Learning, Kubernetes, Machine Learning, and MLOps.


  Kubeflow''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 13 more developer resources.'
plans:
- name: Kubeflow Plans Pricing
  plan_count: 3
  slug: kubeflow-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Kubeflow Rate Limits
  slug: kubeflow-rate-limits
score:
  band: thin
  composite: 33.3
  delta: -2.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
