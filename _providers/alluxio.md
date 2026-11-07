---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: S3-compatible REST API exposed by every Alluxio worker (HTTP port 29998, HTTPS 29996) that lets applications built for Amazon S3 read and write cached data without code changes. Path-style requests on
  name: Alluxio S3 API
  slug: alluxio-s3-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/alluxio/plans/alluxio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alluxio-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.alluxio.io/blog/rss.xml
- group: auth
  href: https://artifacts.apis.io/alluxio/security/alluxio-domain-security.yml
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
  href: https://artifacts.apis.io/alluxio/packages/alluxio-packages.yml
  title: ''
  type: Packages
  url: packages/alluxio-packages.yml
- group: build
  href: https://artifacts.apis.io/alluxio/packages/alluxio-packages.yml
  title: ''
  type: SDKs
  url: packages/alluxio-packages.yml
- group: agent
  href: https://artifacts.apis.io/alluxio/llms/alluxio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alluxio-llms.txt
- group: auth
  href: https://artifacts.apis.io/alluxio/authentication/alluxio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alluxio-authentication.yml
- group: design
  href: https://artifacts.apis.io/alluxio/conventions/alluxio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alluxio-conventions.yml
- group: design
  href: https://artifacts.apis.io/alluxio/lifecycle/alluxio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alluxio-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/alluxio/changelog/alluxio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alluxio-changelog.yml
created: '2026-07-17'
description: Alluxio is a data platform company providing a distributed caching and data-orchestration layer that sits between compute engines and persistent storage to accelerate I/O-intensive AI/ML and analytics workloads. Its high-throughput, low-latency cache serves data to PyTorch, TensorFlow, Spark, Ray and other frameworks across AWS, GCP, Azure and Oracle Cloud, mounting underlying object and file stores (S3, GCS, Azure Blob, HDFS, OSS, COS, TOS) and exposing them through an S3-compatible REST API, a FUSE-based POSIX API, and a Python FSSpec client. The Apache-2.0 open-source project (github.com/Alluxio/alluxio) underpins the commercial Alluxio Enterprise AI product. Alluxio is a portfolio company of a16z.
image: https://avatars.githubusercontent.com/u/16203694?v=4
layout: provider
modified: '2026-10-06'
name: Alluxio
nav: Providers
network: true
overview: 'Alluxio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Orchestration, Data Caching, AI Infrastructure, and Machine Learning.


  Alluxio''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Alluxio Plans Pricing
  plan_count: 2
  slug: alluxio-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 30.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/alluxio/alluxio-2026-07-25T195727.png
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
