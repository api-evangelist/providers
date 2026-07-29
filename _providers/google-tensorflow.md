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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Tensorflow Agentic Access
  operation_count: 5
  slug: google-tensorflow-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
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
artifact_total: 13
collections:
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
overview: 'Google TensorFlow publishes 2 APIs on the [APIs.io](https://apis.io/) network: Model Status API and Prediction API. Tagged areas include AI, Deep Learning, Google, Machine Learning, and Model Serving.


  The Google TensorFlow catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google TensorFlow''s developer surface includes getting-started guide, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Google Tensorflow Plans Pricing
  plan_count: 1
  slug: google-tensorflow-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 2
  name: Google Tensorflow Rate Limits
  slug: google-tensorflow-rate-limits
rules:
- name: Google TensorFlow API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-tensorflow-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.1
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-tensorflow/refs/heads/main/screenshots/google-tensorflow-2026-06-20T182241.png
security:
- kind: domain-security
  name: Google Tensorflow Domain Security
  slug: google-tensorflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: google-tensorflow
tags:
- AI
- Deep Learning
- Google
- Machine Learning
- Model Serving
- Open Source
---
