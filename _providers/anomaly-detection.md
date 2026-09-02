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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Anomaly Detection Agentic Access
  operation_count: 9
  slug: anomaly-detection-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- description: Azure AI Anomaly Detector is a managed REST API service that enables monitoring and detection of anomalies in time series data without requiring machine learning expertise. Supports univariate batch a
  name: Azure AI Anomaly Detector
  slug: azure-ai-anomaly-detector
- description: Elasticsearch Machine Learning APIs provide a comprehensive suite of anomaly detection capabilities for time series data stored in Elasticsearch indices. Supports creating and managing anomaly detecti
  name: Elasticsearch Anomaly Detection API
  slug: elasticsearch-anomaly-detection-api
- description: Datadog's Monitors API supports anomaly detection monitors that identify unusual metric behavior using historical pattern analysis including trends, day-of-week, and time-of-day seasonality. Offers th
  name: Datadog Anomaly Monitor API
  slug: datadog-anomaly-monitor-api
- description: Amazon Lookout for Metrics is a fully managed ML service that automatically detects anomalies in business and operational data. It connects to data sources including Amazon S3, Amazon Redshift, Amazon
  name: AWS Lookout for Metrics
  slug: aws-lookout-for-metrics
- description: PyOD is a comprehensive and scalable Python library for detecting outliers/anomalies in multivariate data. It includes more than 40 detection algorithms including deep learning approaches (AutoEncoder
  name: PyOD (Python Outlier Detection)
  slug: pyod-python-outlier-detection
- description: Trend change-point detection.
  name: Anomaly Detection ChangePoint API
  slug: anomaly-detection-changepoint-api
- description: Multivariate anomaly detection across correlated signals.
  name: Anomaly Detection Multivariate API
  slug: anomaly-detection-multivariate-api
- description: Anomaly detection on a single time series.
  name: Anomaly Detection Univariate API
  slug: anomaly-detection-univariate-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure AI Anomaly Detector ChangePoint API
  slug: open-anomaly-detection-changepoint-api
- collection_type: open
  name: Azure AI Anomaly Detector ChangePoint Multivariate API
  slug: open-anomaly-detection-multivariate-api
- collection_type: open
  name: Azure AI Anomaly Detector ChangePoint Univariate API
  slug: open-anomaly-detection-univariate-api
- collection_type: open
  name: Azure AI Anomaly Detector API
  slug: open-anomaly-detection
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/microsoft/anomaly-detector/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/microsoft/anomaly-detector/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/anomaly-detector/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/anomaly-detector/blob/main/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/microsoft/anomaly-detector/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anomaly-detection-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anomaly-detection-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anomaly-detection-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anomaly-detection-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist/anomaly-detection
- group: other
  title: ''
  type: BestPractices
  url: https://pyod.readthedocs.io/en/latest/faq.html
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/AI-Customer-Engineering-Team/Introducing-Azure-Anomaly-Detector-API/ba-p/490162
- group: docs
  title: Anomaly Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/json-schema/anomaly-detection-anomaly-schema.json
- group: docs
  title: Time Series Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/json-schema/anomaly-detection-time-series-schema.json
- group: docs
  title: Detection Job Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/json-schema/anomaly-detection-detection-job-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/vocabulary/anomaly-detection-vocabulary.yaml
created: 2024-01-15 00:00:00+00:00
description: A curated collection of APIs, tools, and platforms for detecting anomalies in data streams, time series, and multivariate metrics. Covers cloud ML services, observability platforms, and open-source frameworks used for fraud detection, predictive maintenance, IoT monitoring, and security analytics.
examples:
- key_count: 13
  name: Anomaly Detection Anomaly Example
  slug: anomaly-detection-anomaly-example
- key_count: 11
  name: Anomaly Detection Detection Job Example
  slug: anomaly-detection-detection-job-example
- key_count: 10
  name: Anomaly Detection Time Series Example
  slug: anomaly-detection-time-series-example
features:
- description: Detect anomalies in a single time series metric using statistical algorithms, SARIMA models, and SR-CNN approaches for both batch and real-time streaming use cases.
  name: Univariate Time Series Detection
- description: Identify anomalies across multiple correlated metrics simultaneously using graph attention networks and correlation analysis, capturing system-level failures invisible in individual metrics.
  name: Multivariate Detection
- description: Support for both real-time streaming anomaly detection on incoming data points and batch retrospective analysis across historical datasets.
  name: Streaming and Batch Modes
- description: Identify structural breaks and trend changes in time series data beyond point anomalies, enabling detection of regime shifts and concept drift.
  name: Change Point Detection
- description: Group related anomalies and surface likely contributing factors to accelerate diagnosis and response.
  name: Root Cause Analysis
- description: Access to a wide range of detection algorithms from statistical methods to deep learning, including IForest, LOF, OCSVM, AutoEncoder, VAE, and SARIMA.
  name: Algorithm Diversity
finops:
- name: Anomaly Detection Finops
  service_category: API
  slug: anomaly-detection-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anomaly-detection.png
integrations:
- description: Connect anomaly detection pipelines to S3 data lakes for batch analysis of historical metric data.
  name: Amazon S3
- description: Use Elasticsearch ML datafeeds to continuously analyze indices for anomalous patterns using built-in anomaly detection jobs.
  name: Elasticsearch / OpenSearch
- description: Pipe CloudWatch metrics into AWS Lookout for Metrics for automated operational anomaly alerting.
  name: Amazon CloudWatch
- description: Migration target for Azure Anomaly Detector users, providing integrated real-time anomaly detection within the Microsoft Fabric analytics platform.
  name: Microsoft Fabric / Real-Time Intelligence
- description: Visualize anomaly scores and detected anomalies from Elasticsearch ML and Datadog within Grafana dashboards.
  name: Grafana
json_schemas:
- name: Anomaly
  property_count: 13
  slug: anomaly-detection-anomaly
- name: DetectionJob
  property_count: 11
  slug: anomaly-detection-detection-job
- name: TimeSeries
  property_count: 10
  slug: anomaly-detection-time-series
json_structures:
- name: Anomaly Detection Anomaly Structure
  property_count: 13
  slug: anomaly-detection-anomaly-structure
- name: Anomaly Detection Detection Job Structure
  property_count: 11
  slug: anomaly-detection-detection-job-structure
- name: Anomaly Detection Time Series Structure
  property_count: 10
  slug: anomaly-detection-time-series-structure
jsonld:
- class_count: 6
  name: Anomaly Detection Context
  property_count: 23
  slug: anomaly-detection-context
layout: provider
modified: 2026-04-19 00:00:00+00:00
name: Anomaly Detection
nav: Providers
network: true
overview: 'Anomaly Detection publishes 3 APIs on the [APIs.io](https://apis.io/) network: ChangePoint API, Multivariate API, and Univariate API. Tagged areas include Anomaly Detection, Artificial Intelligence, Data Science, Fraud Detection, and Machine-Learning.


  The Anomaly Detection catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anomaly Detection''s developer surface includes authentication, engineering blog, and 14 more developer resources.'
plans:
- name: Anomaly Detection Plans Pricing
  plan_count: 3
  slug: anomaly-detection-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Anomaly Detection Rate Limits
  slug: anomaly-detection-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Anomaly Detection API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: anomaly-detection-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 62.1
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anomaly-detection/refs/heads/main/screenshots/anomaly-detection-2026-06-20T172012.png
security:
- kind: authentication
  name: Anomaly Detection Authentication
  slug: anomaly-detection-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Anomaly Detection Domain Security
  slug: anomaly-detection-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anomaly Detection Vulnerability Disclosure
  slug: anomaly-detection-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: anomaly-detection
tags:
- Anomaly Detection
- Artificial Intelligence
- Data Science
- Fraud Detection
- Machine-Learning
- Monitoring
- Observability
- Outlier Detection
- Pattern Recognition
- Security
- Time Series
use_cases:
- description: Identify fraudulent transactions, account takeovers, and suspicious behavioral patterns in financial and e-commerce systems.
  name: Fraud Detection
- description: Detect early signs of equipment failure in industrial IoT systems by identifying anomalous sensor readings before breakdowns occur.
  name: Predictive Maintenance
- description: Detect unusual network traffic, unauthorized access patterns, and security incidents in real time using behavioral baselines.
  name: IT and Security Operations
- description: Alert on unexpected drops or spikes in KPIs such as revenue, conversion rates, user engagement, or API error rates.
  name: Business Metrics Monitoring
- description: Monitor patient vitals, lab values, and medical device readings for out-of-range or clinically significant anomalies.
  name: Healthcare Monitoring
---
