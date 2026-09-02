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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Forecast Agentic Access
  operation_count: 12
  slug: amazon-forecast-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: Logical groupings of related datasets
  name: Amazon Forecast Dataset Groups API
  slug: amazon-forecast-dataset-groups-api
- description: Dataset management for training data
  name: Amazon Forecast Datasets API
  slug: amazon-forecast-datasets-api
- description: Forecast data export to S3
  name: Amazon Forecast Export Jobs API
  slug: amazon-forecast-export-jobs-api
- description: Generated forecast outputs
  name: Amazon Forecast Forecasts API
  slug: amazon-forecast-forecasts-api
- description: ML models trained on dataset groups
  name: Amazon Forecast Predictors API
  slug: amazon-forecast-predictors-api
- description: Resource metadata labels
  name: Amazon Forecast Tags API
  slug: amazon-forecast-tags-api
arazzos:
- description: Create a dataset, dataset group, predictor, and forecast in a single chained pass.
  name: Amazon Forecast End to End Pipeline
  slug: amazon-forecast-end-to-end-pipeline-workflow
- description: Create a forecast, wait until ACTIVE, export it to S3, and read its tags.
  name: Amazon Forecast Export Forecast
  slug: amazon-forecast-export-forecast-workflow
- description: Create a forecast from a predictor, poll until ACTIVE, and tag it.
  name: Amazon Forecast Generate Forecast
  slug: amazon-forecast-generate-forecast-workflow
- description: Create a dataset group, wait until ACTIVE, then train a predictor on it.
  name: Amazon Forecast Group Then Train
  slug: amazon-forecast-group-then-train-workflow
- description: Train a predictor, wait until ACTIVE, then create a forecast and wait until ACTIVE.
  name: Amazon Forecast Predict and Forecast
  slug: amazon-forecast-predict-and-forecast-workflow
- description: Create a dataset group, poll the listing until it is ACTIVE, and tag it.
  name: Amazon Forecast Provision Dataset Group
  slug: amazon-forecast-provision-dataset-group-workflow
- description: Create a dataset, poll until it becomes ACTIVE, and tag it.
  name: Amazon Forecast Provision Dataset
  slug: amazon-forecast-provision-dataset-workflow
- description: Create a dataset, wait until ACTIVE, then create a dataset group containing it.
  name: Amazon Forecast Register Dataset to Group
  slug: amazon-forecast-register-dataset-to-group-workflow
- description: Create a predictor, poll the listing until it is ACTIVE, and tag it.
  name: Amazon Forecast Train Predictor
  slug: amazon-forecast-train-predictor-workflow
artifact_total: 63
collections:
- collection_type: postman
  name: Amazon Forecast API
  slug: postman-amazon-forecast
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Forecast Dataset Groups API
  slug: open-amazon-forecast-dataset-groups-api
- collection_type: open
  name: Amazon Forecast Dataset Groups Datasets API
  slug: open-amazon-forecast-datasets-api
- collection_type: open
  name: Amazon Forecast Dataset Groups Export Jobs API
  slug: open-amazon-forecast-export-jobs-api
- collection_type: open
  name: Amazon Forecast Dataset Groups Forecasts API
  slug: open-amazon-forecast-forecasts-api
- collection_type: open
  name: Amazon Forecast Dataset Groups Predictors API
  slug: open-amazon-forecast-predictors-api
- collection_type: open
  name: Amazon Forecast Dataset Groups Tags API
  slug: open-amazon-forecast-tags-api
- collection_type: open
  name: Amazon Forecast API
  slug: open-amazon-forecast
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-forecast-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-forecast-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-forecast-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-forecast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-forecast-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-forecast/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-end-to-end-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-export-forecast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-generate-forecast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-group-then-train-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-predict-and-forecast-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-provision-dataset-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-provision-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-register-dataset-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-forecast-train-predictor-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/forecast/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/forecast/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/forecast/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/forecast/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-forecast
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-forecast-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-forecast-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-forecast-context.jsonld
created: '2026-03-16'
description: Amazon Forecast is a fully managed service that uses machine learning to deliver highly accurate forecasts. It analyzes your historical time-series data and automatically selects the right machine learning algorithms to generate accurate forecasts with no machine learning expertise required.
examples:
- key_count: 8
  name: Amazon Forecast Dataset Example
  slug: amazon-forecast-dataset-example
- key_count: 7
  name: Amazon Forecast Dataset Group Example
  slug: amazon-forecast-dataset-group-example
- key_count: 7
  name: Amazon Forecast Forecast Example
  slug: amazon-forecast-forecast-example
- key_count: 10
  name: Amazon Forecast Predictor Example
  slug: amazon-forecast-predictor-example
- key_count: 2
  name: Amazon Forecast Tag Example
  slug: amazon-forecast-tag-example
features:
- description: Automatically evaluates and selects from over 60 ML algorithms to find the best fit for your time-series data.
  name: AutoML
- description: Generates quantile forecasts (p10, p50, p90) to estimate demand uncertainty and plan inventory buffers.
  name: Probabilistic Forecasts
- description: Pre-built domain configurations for retail, workforce, traffic, and cloud capacity forecasting.
  name: Domain-Specific Models
- description: Incorporate external factors (price, promotions, holidays) as related time-series data to improve accuracy.
  name: Related Time Series
- description: Automatic tuning of model hyperparameters to maximize forecast accuracy.
  name: HPO (Hyperparameter Optimization)
- description: Forecast Explainability reports show which features most impact each individual forecast.
  name: Explainability
- description: Export forecast results to Amazon S3 in CSV format for downstream consumption.
  name: S3 Export
finops:
- name: Amazon Forecast Finops
  service_category: API
  slug: amazon-forecast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-forecast.png
json_schemas:
- name: DatasetGroup
  property_count: 7
  slug: amazon-forecast-dataset-group
- name: Dataset
  property_count: 8
  slug: amazon-forecast-dataset
- name: Forecast
  property_count: 7
  slug: amazon-forecast-forecast
- name: Predictor
  property_count: 10
  slug: amazon-forecast-predictor
- name: Tag
  property_count: 2
  slug: amazon-forecast-tag
json_structures:
- name: Amazon Forecast Dataset Group Structure
  property_count: 0
  slug: amazon-forecast-dataset-group-structure
- name: Amazon Forecast Dataset Structure
  property_count: 0
  slug: amazon-forecast-dataset-structure
- name: Amazon Forecast Forecast Structure
  property_count: 0
  slug: amazon-forecast-forecast-structure
- name: Amazon Forecast Predictor Structure
  property_count: 0
  slug: amazon-forecast-predictor-structure
- name: Amazon Forecast Tag Structure
  property_count: 0
  slug: amazon-forecast-tag-structure
jsonld:
- class_count: 5
  name: Amazon Forecast Context
  property_count: 15
  slug: amazon-forecast-context
layout: provider
modified: '2026-05-19'
name: Amazon Forecast
nav: Providers
network: true
overview: 'Amazon Forecast publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Dataset Groups API, Datasets API, Export Jobs API, and 3 more. Tagged areas include Forecasting, Machine-Learning, Predictive Analytics, and Time Series.


  The Amazon Forecast catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Forecast''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 24 more developer resources.'
plans:
- name: Amazon Forecast Plans Pricing
  plan_count: 3
  slug: amazon-forecast-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Amazon Forecast Rate Limits
  slug: amazon-forecast-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Forecast API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-forecast-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  name: Amazon Forecast API Rules
  rule_count: 35
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 25
  slug: amazon-forecast-spectral-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 77.0
    developer_ergonomics: 57.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-forecast/refs/heads/main/screenshots/amazon-forecast-2026-06-20T171651.png
security:
- kind: authentication
  name: Amazon Forecast Authentication
  slug: amazon-forecast-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Forecast Domain Security
  slug: amazon-forecast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Forecast Vulnerability Disclosure
  slug: amazon-forecast-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Forecast Trust Center
  slug: amazon-forecast-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-forecast
tags:
- Forecasting
- Machine-Learning
- Predictive Analytics
- Time Series
use_cases:
- description: Predict item-level sales for inventory planning and replenishment across stores.
  name: Retail Demand Forecasting
- description: Forecast staffing needs for contact centers and seasonal workforce management.
  name: Workforce Capacity Planning
- description: Predict EC2 capacity requirements to optimize reserved instance purchases.
  name: Cloud Resource Forecasting
- description: Forecast component and raw material demand to reduce stockouts and carrying costs.
  name: Supply Chain Optimization
- description: Project revenue by product, region, and channel for financial planning.
  name: Financial Revenue Forecasting
- description: Predict electricity load and generation requirements for grid balancing.
  name: Energy Load Forecasting
website: https://aws.amazon.com/forecast/
---
