---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: S3-compatible REST API exposed by every Alluxio worker (HTTP port 29998, HTTPS 29996) that lets applications built for Amazon S3 read and write cached data without code changes. Path-style requests on
  name: Alluxio S3 API
  slug: alluxio-s3-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alluxio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alluxio.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.alluxio.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.alluxio.io/ee-ai-en/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.alluxio.io/ee-ai-en/start.md
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.alluxio.io/ee-ai-en/data-access.md
- group: company
  title: ''
  type: Blog
  url: https://www.alluxio.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alluxio
- group: operate
  title: ''
  type: Support
  url: https://www.alluxio.io/community
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alluxio.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.alluxio.io/alluxio-ai-free-trial-c
- group: build
  title: ''
  type: Packages
  url: packages/alluxio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alluxio-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alluxio-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alluxio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alluxio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alluxio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alluxio-changelog.yml
created: '2026-07-17'
description: Alluxio is a data platform company providing a distributed caching and data-orchestration layer that sits between compute engines and persistent storage to accelerate I/O-intensive AI/ML and analytics workloads. Its high-throughput, low-latency cache serves data to PyTorch, TensorFlow, Spark, Ray and other frameworks across AWS, GCP, Azure and Oracle Cloud, mounting underlying object and file stores (S3, GCS, Azure Blob, HDFS, OSS, COS, TOS) and exposing them through an S3-compatible REST API, a FUSE-based POSIX API, and a Python FSSpec client. The Apache-2.0 open-source project (github.com/Alluxio/alluxio) underpins the commercial Alluxio Enterprise AI product. Alluxio is a portfolio company of a16z.
image: https://avatars.githubusercontent.com/u/16203694?v=4
layout: provider
modified: '2026-07-17'
name: Alluxio
nav: Providers
network: true
overview: 'Alluxio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Orchestration, Data Caching, AI Infrastructure, and Machine Learning.


  Alluxio''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, pricing, signup flow, and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 27.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 77.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alluxio/refs/heads/main/screenshots/alluxio-2026-07-25T195727.png
security:
- kind: authentication
  name: Alluxio Authentication
  slug: alluxio-authentication
  summary_line: http-signature/none/tls-mutual · 4 schemes
- kind: domain-security
  name: Alluxio Domain Security
  slug: alluxio-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alluxio
tags:
- Company
- Data Orchestration
- Data Caching
- AI Infrastructure
- Machine Learning
- Analytics
- Distributed Storage
- Object Storage
- S3
- Open Source
website: https://www.alluxio.io
---
