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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Machine Learning Agentic Access
  operation_count: 7
  slug: microsoft-azure-machine-learning-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: Azure Machine Learning Operations API
  slug: microsoft-azure-machine-learning-operations-api
- description: Workspaces operations
  name: Azure Machine Learning Workspaces API
  slug: microsoft-azure-machine-learning-workspaces-api
artifact_total: 25
collections:
- collection_type: open
  name: Azure Machine Learning REST API
  slug: open-microsoft-azure-machine-learning
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-machine-learning-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-machine-learning-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-machine-learning-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-machine-learning-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/machine-learning/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/machine-learning/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Machine Learning is an enterprise-grade cloud service for building, training, deploying, and managing machine learning models. It supports the full ML lifecycle including data preparation, model training, evaluation, deployment, and monitoring with MLOps capabilities.
features:
- description: Create and manage Azure ML workspaces as the top-level resource for ML assets and experiments.
  name: Workspace Management
- description: Provision and manage compute clusters, compute instances, and Kubernetes-attached compute targets.
  name: Compute Resources
- description: Run training jobs at scale with automated ML, distributed training, and hyperparameter tuning.
  name: Model Training
- description: Deploy models as managed online endpoints, batch endpoints, or to Kubernetes for real-time and batch inference.
  name: Model Deployment
- description: Build reproducible ML pipelines with versioning, CI/CD integration, and model registry capabilities.
  name: MLOps and Pipelines
- description: Use built-in tools for fairness assessment, interpretability, and model monitoring across the lifecycle.
  name: Responsible AI
finops:
- name: Microsoft Azure Machine Learning Finops
  service_category: API
  slug: microsoft-azure-machine-learning-finops
image: https://azure.microsoft.com/svghandler/machine-learning/
integrations:
- description: Store training data, models, and experiment artifacts in Azure Blob Storage and Data Lake.
  name: Azure Storage
- description: Deploy ML models to AKS for production-grade inference at scale.
  name: Azure Kubernetes Service
- description: Integrate ML pipelines with Azure DevOps for continuous integration and deployment.
  name: Azure DevOps
- description: Automate ML workflows with GitHub Actions for training and deployment automation.
  name: GitHub Actions
- description: Consume ML model predictions in Power BI dashboards and reports.
  name: Power BI
layout: provider
modified: '2026-05-19'
name: Azure Machine Learning
nav: Providers
network: true
overview: 'Azure Machine Learning publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Workspaces API. Tagged areas include AI, Azure, Machine Learning, MLOps, and Model Deployment.


  Azure Machine Learning''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Microsoft Azure Machine Learning Plans Pricing
  plan_count: 3
  slug: microsoft-azure-machine-learning-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 5
  name: Microsoft Azure Machine Learning Rate Limits
  slug: microsoft-azure-machine-learning-rate-limits
scopes:
- name: Microsoft Azure Machine Learning Scopes
  scope_count: 1
  slug: microsoft-azure-machine-learning-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 49.4
  delta: -1.1
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.1
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-machine-learning/refs/heads/main/screenshots/microsoft-azure-machine-learning-2026-06-20T185423.png
security:
- kind: authentication
  name: Microsoft Azure Machine Learning Authentication
  slug: microsoft-azure-machine-learning-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Machine Learning Domain Security
  slug: microsoft-azure-machine-learning-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-machine-learning
tags:
- AI
- Azure
- Machine Learning
- MLOps
- Model Deployment
- Model Training
use_cases:
- description: Build and deploy predictive models for forecasting, classification, and regression scenarios.
  name: Predictive Analytics
- description: Train and deploy image classification, object detection, and segmentation models.
  name: Computer Vision
- description: Build NLP models for text classification, entity recognition, and sentiment analysis.
  name: Natural Language Processing
- description: Operationalize ML models with automated training pipelines, deployment, and monitoring.
  name: MLOps and Production ML
website: https://portal.azure.com/
---
