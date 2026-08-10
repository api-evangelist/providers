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
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: The core specification for the Parquet columnar storage format.
  name: Apache Parquet Format Specification
  slug: format-specification
- description: Python library for reading and writing Parquet files, distributed as part of Apache Arrow.
  name: PyArrow Parquet Python API
  slug: pyarrow
- description: Java implementation for reading and writing Parquet files.
  name: Parquet Java API
  slug: java
- description: C++ implementation as part of Apache Arrow.
  name: Parquet C++ API
  slug: cpp
- description: R package for reading and writing Parquet files via Apache Arrow.
  name: Parquet R API
  slug: r
- description: Alternative Python implementation for Parquet files.
  name: FastParquet Python API
  slug: fastparquet
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parquet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parquet-domain-security.yml
- group: other
  title: ''
  type: Mailing Lists
  url: https://parquet.apache.org/community/
- group: operate
  title: ''
  type: Issue Tracker
  url: https://issues.apache.org/jira/projects/PARQUET
- group: company
  title: ''
  type: Blog
  url: https://parquet.apache.org/blog/
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/parquet-format/blob/master/LICENSE
created: '2024-01-01'
description: APIs and tools for working with Apache Parquet, the open source columnar storage format for efficient analytics workloads. This index covers the format specification along with the major language implementations.
finops:
- name: Parquet Finops
  service_category: API
  slug: parquet-finops
image: https://parquet.apache.org/assets/img/parquet-logo.png
layout: provider
modified: '2026-04-28'
name: Apache Parquet
nav: Providers
network: true
overview: 'Apache Parquet publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Big Data, Columnar Storage, Data Format, and Parquet.


  Apache Parquet''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Parquet Plans Pricing
  plan_count: 3
  slug: parquet-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Parquet Rate Limits
  slug: parquet-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 19.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parquet/refs/heads/main/screenshots/parquet-2026-06-20T191417.png
security:
- kind: domain-security
  name: Parquet Domain Security
  slug: parquet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Parquet Vulnerability Disclosure
  slug: parquet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: parquet
tags:
- Apache
- Big Data
- Columnar Storage
- Data Format
- Parquet
---
