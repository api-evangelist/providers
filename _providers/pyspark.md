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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Core Spark functionality including RDDs, SparkContext, and basic operations.
  name: PySpark Core API
  slug: pyspark-core-api
- description: Structured data processing with DataFrame and SQL operations.
  name: PySpark SQL
  slug: pyspark-sql
- description: Real-time stream processing capabilities using DStreams and Structured Streaming.
  name: PySpark Streaming
  slug: pyspark-streaming
- description: Machine learning library with scalable algorithms for classification, regression, clustering, and more.
  name: PySpark MLlib
  slug: pyspark-mllib
- description: DataFrame-based machine learning API with pipelines and feature transformers.
  name: PySpark ML (DataFrame-based)
  slug: pyspark-ml
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pyspark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pyspark-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apachespark
- group: company
  title: ''
  type: Website
  url: https://spark.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/spark
- group: start
  title: ''
  type: GettingStarted
  url: https://spark.apache.org/docs/latest/api/python/getting_started/install.html
- group: start
  title: ''
  type: GettingStarted
  url: https://spark.apache.org/docs/latest/quick-start.html
- group: other
  title: ''
  type: Downloads
  url: https://spark.apache.org/downloads.html
- group: operate
  title: ''
  type: Community
  url: https://spark.apache.org/community.html
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/projects/SPARK
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://spark.apache.org/releases/
- group: auth
  title: ''
  type: Security
  url: https://spark.apache.org/security.html
created: '2024-01-01'
description: Python API for Apache Spark - A unified analytics engine for large-scale data processing supporting batch processing, streaming, machine learning, and graph computing.
finops:
- name: Pyspark Finops
  service_category: API
  slug: pyspark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pyspark.png
layout: provider
modified: '2026-04-28'
name: Apache PySpark
nav: Providers
network: true
overview: 'Apache PySpark publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Big Data, Data Processing, Distributed Computing, Machine-Learning, and Python.


  Apache PySpark''s developer surface includes getting-started guide, release notes, and 10 more developer resources.'
plans:
- name: Pyspark Plans Pricing
  plan_count: 3
  slug: pyspark-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Pyspark Rate Limits
  slug: pyspark-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pyspark/refs/heads/main/screenshots/pyspark-2026-06-20T192331.png
security:
- kind: domain-security
  name: Pyspark Domain Security
  slug: pyspark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pyspark Vulnerability Disclosure
  slug: pyspark-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pyspark
tags:
- Big Data
- Data Processing
- Distributed Computing
- Machine-Learning
- Python
- Streaming
website: https://spark.apache.org/
---
