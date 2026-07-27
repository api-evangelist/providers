---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 4
apis:
- description: NNabla is Sony's open-source deep-learning framework with Python and C++ bindings, dynamic and static computation graphs, GPU/CUDA acceleration, and a model format for training and inference. Distribu
  name: Sony Neural Network Libraries (NNabla)
  slug: nnabla
- description: Sonyflake is a Go library producing 63-bit unique IDs inspired by Twitter's Snowflake but tuned for longer machine-ID space and longer lifetime. MIT licensed.
  name: Sonyflake Distributed ID Generator
  slug: sonyflake
- description: gobreaker is a Go implementation of the Circuit Breaker pattern, widely used in microservice resilience designs. MIT licensed.
  name: Sony gobreaker Circuit Breaker
  slug: gobreaker
- description: 'Spresense is Sony''s hexa-core Cortex-M4F IoT board powered by the CXD5602 chipset. The Spresense SDK provides NuttX-based C/C++ APIs for multi-GNSS positioning, high-resolution audio, camera capture, '
  name: Sony Spresense SDK
  slug: spresense-sdk
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sony-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sony
- group: company
  title: ''
  type: Website
  url: https://www.sony.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Sony
- group: start
  title: ''
  type: OpenSourcePortal
  url: https://oss.sony.net/
- group: design
  title: ''
  type: SpectralRules
  url: rules/sony-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sony-vocabulary.yml
created: '2026-05-05'
description: Sony Group Corporation is a Japanese multinational spanning electronics, gaming, entertainment, image sensors, and financial services. Sony's developer-facing surface includes the Neural Network Libraries (NNabla) deep-learning framework, the Spresense IoT board SDK, Sonyflake distributed ID service, and a portfolio of Go and embedded-Linux open-source tooling maintained on github.com/Sony.
examples:
- key_count: 5
  name: Sonyflake Id Example
  slug: sonyflake-id-example
features:
- description: NNabla provides dynamic and static computation graphs for training and inference
  name: Deep Learning Framework
- description: Sonyflake mints 63-bit time-ordered unique IDs across distributed nodes
  name: Distributed ID Generation
- description: gobreaker brings circuit-breaker resilience to Go microservice fleets
  name: Circuit Breaker Resilience
- description: Spresense delivers hexa-core Cortex-M4F compute with GNSS, audio, and LTE
  name: Edge IoT Compute
- description: Sony publishes most libraries under Apache 2.0 or MIT
  name: Open Source Licensing
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sony.png
integrations:
- description: NNabla integrates with NumPy, PyTorch comparators, and ONNX export
  name: Python Ecosystem
- description: Sonyflake and gobreaker are widely adopted Go libraries
  name: Go Ecosystem
- description: Spresense ships an Arduino-compatible toolchain in addition to the NuttX SDK
  name: Arduino IDE
- description: NNabla can target NVIDIA CUDA-enabled GPUs for accelerated training
  name: CUDA
json_schemas:
- name: NNabla Network Definition
  property_count: 3
  slug: nnabla-network
- name: Sonyflake ID
  property_count: 4
  slug: sonyflake-id
jsonld:
- class_count: 9
  name: Sony Context
  property_count: 0
  slug: sony-context
layout: provider
modified: '2026-05-16'
name: Sony
nav: Providers
network: true
overview: 'Sony publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Technology, Consumer Electronics, Gaming, Entertainment, and Artificial Intelligence.


  The Sony catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
random_paper: 49
rules:
- name: Sony API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sony-jsonschema-spectral-rules
- name: Sony API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: sony-spectral-rules
score:
  band: emerging
  composite: 26.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 26.4
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 26.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sony/refs/heads/main/screenshots/sony-2026-06-20T194211.png
security:
- kind: domain-security
  name: Sony Domain Security
  slug: sony-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sony
tags:
- Technology
- Consumer Electronics
- Gaming
- Entertainment
- Artificial Intelligence
use_cases:
- description: Train and deploy deep-learning models with NNabla on GPUs and embedded devices
  name: ML Model Training
- description: Generate guaranteed-unique identifiers for events, orders, and records
  name: Globally Unique IDs
- description: Use gobreaker to prevent cascading failures in distributed services
  name: Resilient Microservices
- description: Build asset tracking, agricultural sensing, and infrastructure inspection with Spresense
  name: IoT Sensing and Positioning
- description: Combine NNabla and Spresense to run inference at the edge with low power
  name: Edge AI Inference
website: https://www.sony.com/
---
