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
- acting_count: 63
  human_in_the_loop: 0
  name: Bigml Agentic Access
  operation_count: 108
  slug: bigml-agentic-access
  summary_line: 108 operations · 63 acting
api_count: 15
apis:
- description: Detect anomalies in datasets using Isolation Forest
  name: BigML Anomaly Detection API
  slug: bigml-anomaly-detection-api
- description: Run predictions, centroid assignments, and anomaly scoring on full datasets
  name: BigML Batch Operations API
  slug: bigml-batch-operations-api
- description: Create unsupervised cluster models and assign centroids
  name: BigML Clustering API
  slug: bigml-clustering-api
- description: Connect to external databases and data sources
  name: BigML Data Connectors API
  slug: bigml-data-connectors-api
- description: Create and manage training datasets from sources
  name: BigML Datasets API
  slug: bigml-datasets-api
- description: Train and manage ensemble models (random forests, gradient boosted trees)
  name: BigML Ensembles API
  slug: bigml-ensembles-api
- description: Evaluate model performance against a test dataset
  name: BigML Evaluations API
  slug: bigml-evaluations-api
- description: Train and manage decision tree models
  name: BigML Models API
  slug: bigml-models-api
- description: Generate individual predictions from trained models
  name: BigML Predictions API
  slug: bigml-predictions-api
- description: Organize resources into projects
  name: BigML Projects API
  slug: bigml-projects-api
- description: Upload and manage raw data sources (CSV, JSON, Excel, etc.)
  name: BigML Sources API
  slug: bigml-sources-api
- description: Logistic regression, linear regression, and deep neural network models
  name: BigML Supervised Learning API
  slug: bigml-supervised-learning-api
- description: Time series forecasting models and forecasts
  name: BigML Time Series API
  slug: bigml-time-series-api
- description: Topic models, association rules, and PCA
  name: BigML Unsupervised Learning API
  slug: bigml-unsupervised-learning-api
- description: Automate ML workflows with WhizzML scripts and executions
  name: BigML WhizzML Scripting API
  slug: bigml-whizzml-scripting-api
artifact_total: 30
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigml-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigml-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bigml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bigml.com/documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bigmlcom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigml-inc
- group: company
  title: ''
  type: Blog
  url: https://blog.bigml.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://bigml.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigml.com/
- group: other
  title: ''
  type: X
  url: https://x.com/bigmlcom
- group: commercial
  title: ''
  type: Plans
  url: plans/bigml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bigml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bigml-finops.yml
created: '2026-06-13'
description: BigML is a machine learning platform with a comprehensive REST API for creating datasets, training models, making predictions, running batch predictions, and managing ML workflows. The platform supports supervised and unsupervised learning including decision trees, ensembles, deepnets, linear and logistic regression, clustering, anomaly detection, topic models, and time series forecasting.
examples:
- key_count: 4
  name: Create Cluster
  slug: create-cluster
- key_count: 4
  name: Create Dataset
  slug: create-dataset
- key_count: 4
  name: Create Ensemble
  slug: create-ensemble
- key_count: 4
  name: Create Model
  slug: create-model
- key_count: 4
  name: Create Prediction
  slug: create-prediction
- key_count: 4
  name: Create Source
  slug: create-source
finops:
- name: Bigml Finops
  service_category: ''
  slug: bigml-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigml.png
json_schemas:
- name: BigML Resource
  property_count: 7
  slug: bigml-resource
jsonld:
- class_count: 41
  name: Bigml Context
  property_count: 43
  slug: bigml-context
layout: provider
modified: '2026-06-13'
name: BigML
nav: Providers
network: true
overview: 'BigML publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Anomaly Detection API, Batch Operations API, Clustering API, and 12 more. Tagged areas include Machine Learning, Artificial Intelligence, Predictions, Datasets, and Models.


  The BigML catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BigML''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Bigml Plans Pricing
  plan_count: 4
  slug: bigml-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Bigml Rate Limits
  slug: bigml-rate-limits
rules:
- name: BigML API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: bigml-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.1
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigml/refs/heads/main/screenshots/bigml-2026-06-20T173236.png
security:
- kind: authentication
  name: Bigml Authentication
  slug: bigml-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bigml Domain Security
  slug: bigml-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bigml
tags:
- Machine Learning
- Artificial Intelligence
- Predictions
- Datasets
- Models
- Clustering
- Anomaly Detection
- Time Series
- Deep Learning
website: https://bigml.com/
---
