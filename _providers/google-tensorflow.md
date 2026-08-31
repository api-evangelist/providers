---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Tensorflow Agentic Access
  operation_count: 5
  slug: google-tensorflow-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: TensorFlow Hub provides a repository of reusable trained machine learning models. The API allows developers to search, discover, and download pre-trained models and model components (SavedModels, TF.j
  name: TensorFlow Hub API
  slug: tensorflow-hub-api
- description: TensorFlow Model Analysis (TFMA) provides tools and APIs for evaluating TensorFlow models. It enables computing metrics over large datasets using Apache Beam, slicing evaluation results across differe
  name: TensorFlow Model Analysis API
  slug: tensorflow-model-analysis-api
- description: Model metadata and status operations
  name: Google TensorFlow Model Status API
  slug: google-tensorflow-model-status-api
- description: Model inference operations
  name: Google TensorFlow Prediction API
  slug: google-tensorflow-prediction-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google TensorFlow TensorFlow Serving REST Model Status API
  slug: open-google-tensorflow-model-status-api
- collection_type: open
  name: Google TensorFlow TensorFlow Serving REST Model Status Prediction API
  slug: open-google-tensorflow-prediction-api
- collection_type: open
  name: Google TensorFlow TensorFlow Serving REST API
  slug: open-tensorflow-serving
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-tensorflow-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-tensorflow-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/tensorflowdev
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tensorflow.org/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tensorflow.org
- group: build
  title: ''
  type: SDKs
  url: https://www.tensorflow.org/install
- group: operate
  title: ''
  type: Support
  url: https://www.tensorflow.org/community
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/tensorflow/tensorflow
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-tensorflow-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.tensorflow.org/feeds/posts/default?alt=rss
created: '2026-03-13'
description: Google TensorFlow is an open-source machine learning framework providing APIs and tools for building, training, and deploying ML models, including TensorFlow Serving for model inference and TensorFlow Hub for reusable model components.
finops:
- name: Google Tensorflow Finops
  service_category: AI Infrastructure
  slug: google-tensorflow-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-tensorflow.png
json_schemas:
- name: TensorFlow Serving Predict Request
  property_count: 3
  slug: google-tensorflow-predict-request
jsonld:
- class_count: 0
  name: Google Tensorflow Context
  property_count: 4
  slug: google-tensorflow-context
layout: provider
modified: '2026-05-19'
name: Google TensorFlow
nav: Providers
network: true
overview: 'Google TensorFlow publishes 2 APIs on the [APIs.io](https://apis.io/) network: Model Status API and Prediction API. Tagged areas include Artificial Intelligence, Deep Learning, Google, Machine-Learning, and Model Serving.


  The Google TensorFlow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google TensorFlow''s developer surface includes getting-started guide, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Google Tensorflow Plans Pricing
  plan_count: 1
  slug: google-tensorflow-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Google Tensorflow Rate Limits
  slug: google-tensorflow-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Google TensorFlow API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-tensorflow-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 9.8
    contract_quality: 54.1
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-tensorflow/refs/heads/main/screenshots/google-tensorflow-2026-06-20T182241.png
security:
- kind: domain-security
  name: Google Tensorflow Domain Security
  slug: google-tensorflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: google-tensorflow
tags:
- Artificial Intelligence
- Deep Learning
- Google
- Machine-Learning
- Model Serving
- Open-Source
---
