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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The SystemDS Python API (systemds) provides a Python interface for building end-to-end ML pipelines. It includes Matrix and Frame types for distributed data manipulation, built-in algorithms for prepr
  name: Apache SystemDS Python API
  slug: apache-systemds-python-api
artifact_total: 18
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/systemds/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/systemds/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-systemds-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-systemds-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/systemds
- group: docs
  title: ''
  type: Documentation
  url: https://apache.github.io/systemds/
- group: start
  title: ''
  type: Portal
  url: https://systemds.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://apache.github.io/systemds/get-started
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/systemds/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: Apache SystemDS is an open-source ML system for the end-to-end data science lifecycle from data integration, cleaning, and feature engineering to model training, debugging, and deployment. It provides a declarative machine learning language (DML), automatic optimization for different execution backends (local, distributed Spark), and a Python API (SystemDS Python). SystemDS is an Apache Software Foundation top-level project designed for scalable ML workflows.
features:
- description: High-level R-like language for specifying ML algorithms with automatic optimization.
  name: Declarative ML Language (DML)
- description: Query optimization, memory management, and execution plan selection for ML workloads.
  name: Automatic Optimization
- description: Privacy-preserving federated ML across distributed data silos without data sharing.
  name: Federated Learning
- description: 50+ built-in ML algorithms including linear models, neural networks, clustering, and ensemble methods.
  name: Built-In Algorithms
- description: Pythonic API for ML pipeline development with lazy evaluation and distributed execution.
  name: Python API
- description: Automated data cleaning, imputation, encoding, and normalization pipelines.
  name: Data Cleaning Pipelines
finops:
- name: Apache Systemds Finops
  service_category: API
  slug: apache-systemds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-systemds.png
integrations:
- description: Native Spark backend for distributed matrix operations and ML training.
  name: Apache Spark
- description: Python API with NumPy-compatible Matrix type for local and distributed computation.
  name: Python
- description: Kubernetes deployment support for SystemDS runtime via Helm charts.
  name: Kubernetes
layout: provider
modified: '2026-04-19'
name: Apache SystemDS
nav: Providers
network: true
overview: 'Apache SystemDS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AutoML, Data Science, Distributed Computing, Machine Learning, and Open Source.


  Apache SystemDS''s developer surface includes documentation, developer portal, getting-started guide, release notes, and 7 more developer resources.'
plans:
- name: Apache Systemds Plans Pricing
  plan_count: 3
  slug: apache-systemds-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Apache Systemds Rate Limits
  slug: apache-systemds-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 19.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-systemds/refs/heads/main/screenshots/apache-systemds-2026-06-20T172150.png
security:
- kind: domain-security
  name: Apache Systemds Domain Security
  slug: apache-systemds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Systemds Vulnerability Disclosure
  slug: apache-systemds-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-systemds
tags:
- AutoML
- Data Science
- Distributed Computing
- Machine Learning
- Open Source
use_cases:
- description: Train large-scale ML models distributed across Apache Spark clusters.
  name: Distributed ML Training
- description: Cross-silo federated learning for privacy-sensitive healthcare and finance data.
  name: Federated Machine Learning
- description: Integrated data preparation, feature engineering, training, and serving pipelines.
  name: End-to-End ML Pipelines
website: https://systemds.apache.org/
---
