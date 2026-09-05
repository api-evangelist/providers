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
  scored_at: '2026-09-04'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/parquet-format/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/parquet-format/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/parquet-format/blob/master/CONTRIBUTING.md
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


  Apache Parquet''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Parquet Plans Pricing
  plan_count: 3
  slug: parquet-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Parquet Rate Limits
  slug: parquet-rate-limits
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 18.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
