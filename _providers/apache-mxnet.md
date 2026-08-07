---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'MXNet provides APIs in Python, Scala, Java, C++, R, Julia, and Perl for deep learning model development, with the Gluon high-level API for imperative model building, Symbol/NDArray low-level APIs for '
  name: Apache MXNet
  slug: apache-mxnet
artifact_total: 26
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-mxnet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-mxnet-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-mxnet
- group: start
  title: ''
  type: Portal
  url: https://mxnet.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/mxnet
- group: other
  title: ''
  type: Wiki
  url: https://cwiki.apache.org/confluence/display/MXNET/Apache+MXNet+Home
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/projects/MXNET/issues
- group: other
  title: ''
  type: MailingList
  url: mailto:dev@mxnet.apache.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache MXNet is a retired deep learning framework (now in the Apache Attic) designed for both efficiency and flexibility. It provided a multi-language API for building and training deep neural networks with support for distributed training, the Gluon high-level API, and deployment on edge devices. MXNet supported Python, Scala, Java, C++, R, Julia, and Perl.
features:
- description: Seamlessly transitions between Gluon eager imperative mode and symbolic execution for research flexibility and production efficiency.
  name: Hybrid Front-End
- description: Supports Parameter Server and Horovod for scalable distributed training across multiple GPUs and nodes.
  name: Distributed Training
- description: Native APIs in Python, Scala, Java, C++, R, Julia, Clojure, and Perl for broad developer accessibility.
  name: Multi-Language Bindings
- description: Intuitive Gluon API for imperative model building with automatic differentiation and dynamic computation graphs.
  name: Gluon High-Level API
- description: NumPy-like array operations for GPU-accelerated numerical computing as the foundation of MXNet computations.
  name: NDArray API
- description: Symbolic computation graph API for efficient inference and production deployment.
  name: Symbol API
- description: Pre-trained models for computer vision, NLP, and other tasks accessible via the Gluon model zoo.
  name: Model Zoo
- description: Lightweight deployment support for edge devices and mobile platforms via TVM and ONNX export.
  name: Edge Deployment
finops:
- name: Apache Mxnet Finops
  service_category: API
  slug: apache-mxnet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-mxnet.png
integrations:
- description: Computer vision toolkit built on MXNet providing pre-trained models and training utilities for vision tasks.
  name: GluonCV
- description: NLP toolkit built on MXNet with pre-trained language models and text processing utilities.
  name: GluonNLP
- description: Time series modeling toolkit built on MXNet for probabilistic forecasting.
  name: GluonTS
- description: ONNX model format support for importing and exporting models to/from other frameworks.
  name: ONNX
- description: Apache TVM deep learning compiler for optimizing MXNet model deployment on diverse hardware targets.
  name: TVM
- description: Horovod distributed training framework integration for efficient multi-GPU and multi-node training.
  name: Horovod
- description: Dive into Deep Learning interactive textbook using MXNet for teaching deep learning concepts.
  name: D2L.ai
layout: provider
modified: '2026-04-19'
name: Apache MXNet
nav: Providers
network: true
overview: 'Apache MXNet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Deep Learning, Machine Learning, Neural Networks, and Python.


  Apache MXNet''s developer surface includes developer portal and 9 more developer resources.'
plans:
- name: Apache Mxnet Plans Pricing
  plan_count: 3
  slug: apache-mxnet-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Apache Mxnet Rate Limits
  slug: apache-mxnet-rate-limits
score:
  band: emerging
  composite: 22.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-mxnet/refs/heads/main/screenshots/apache-mxnet-2026-06-20T172124.png
security:
- kind: domain-security
  name: Apache Mxnet Domain Security
  slug: apache-mxnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Mxnet Vulnerability Disclosure
  slug: apache-mxnet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-mxnet
tags:
- AI
- Deep Learning
- Machine Learning
- Neural Networks
- Python
- Retired
use_cases:
- description: Build and train image classification, object detection, and segmentation models using GluonCV toolkit.
  name: Computer Vision
- description: Develop NLP models for text classification, sentiment analysis, and language modeling using GluonNLP.
  name: Natural Language Processing
- description: Build time series forecasting models using the GluonTS toolkit for probabilistic forecasting.
  name: Time Series Forecasting
- description: Train large neural networks across multiple GPUs and nodes using Parameter Server or Horovod.
  name: Distributed Deep Learning
- description: Rapid prototyping of novel deep learning architectures using the Gluon imperative API.
  name: Research Prototyping
website: https://mxnet.apache.org/
---
