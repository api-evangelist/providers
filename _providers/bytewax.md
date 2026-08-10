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
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: Open-source Python library for building distributed stream processing dataflows. Provides bytewax.dataflow, bytewax.operators (including windowing), bytewax.inputs, bytewax.outputs, and a connectors p
  name: Bytewax Python Library
  slug: python-library
- description: Built-in connector modules for integrating Bytewax dataflows with external systems, including Kafka (with operators and serialization submodules), files, stdio, and demo sources. Custom connectors are
  name: Bytewax Connectors
  slug: connectors
- description: 'Self-hosted control plane for securely building, deploying, and scaling Bytewax workloads on Kubernetes. Managed through the waxctl CLI and Helm chart, with deployment options including AWS, GCP, and '
  name: Bytewax Platform
  slug: platform
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bytewax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bytewax.io
- group: start
  title: ''
  type: Portal
  url: https://docs.bytewax.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bytewax.io
- group: commercial
  title: ''
  type: Pricing
  url: https://bytewax.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://bytewax.io/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bytewax
- group: other
  title: ''
  type: Repository
  url: https://github.com/bytewax/bytewax
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/bytewax/
- group: other
  title: ''
  type: Products
  url: https://bytewax.io/products
- group: build
  title: ''
  type: Examples
  url: https://docs.bytewax.io/guide/getting-started/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bytewax.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bytewax.io/privacy-policy
- group: operate
  title: ''
  type: Community
  url: https://bytewax.io/slack
created: '2026-05-23'
description: Bytewax is a Python-native distributed stream processing framework built on a Rust runtime. Developers define dataflows using the bytewax.dataflow API, composing operators (map, filter, reduce, joins, windowing) over connectors for Kafka, files, stdio, demos, and custom sources/sinks. The Bytewax Platform layers a self-hostable Kubernetes-based control plane on top, managed with the waxctl CLI and Helm chart, with deployment targets that include AWS, GCP, and the AWS Marketplace.
finops:
- name: Bytewax Finops
  service_category: API
  slug: bytewax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bytewax.png
layout: provider
modified: '2026-05-23'
name: Bytewax
nav: Providers
network: true
overview: 'Bytewax publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Stream Processing, Python, Dataflow, Real-Time, and Kafka.


  Bytewax''s developer surface includes developer portal, documentation, pricing, engineering blog, GitHub presence, code examples, and 8 more developer resources.'
plans:
- name: Bytewax Plans Pricing
  plan_count: 1
  slug: bytewax-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 2
  name: Bytewax Rate Limits
  slug: bytewax-rate-limits
score:
  band: thin
  composite: 29.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bytewax/refs/heads/main/screenshots/bytewax-2026-06-20T173827.png
security:
- kind: domain-security
  name: Bytewax Domain Security
  slug: bytewax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bytewax
tags:
- Stream Processing
- Python
- Dataflow
- Real-Time
- Kafka
- Windowing
- Connectors
- Distributed Systems
- Kubernetes
- Open Source
website: https://bytewax.io
---
