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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Delta Lake storage framework defines the on-disk transaction log and protocol that adds ACID transactions, schema enforcement, and time travel to Parquet-based data lakes. Delta Lake exposes Spark
  name: Delta Lake Storage Framework
  slug: delta-lake-storage
- description: Delta Sharing is an open protocol for secure data sharing across organizations, defined as a REST API specification. Sharing servers expose endpoints for listing shares, schemas, and tables, and for r
  name: Delta Sharing Protocol
  slug: delta-sharing
- description: Catalog-managed Delta tables delegate table scan planning to an external catalog using the Iceberg REST Catalog protocol, enabling interoperability with Unity Catalog and other catalog services.
  name: Delta Catalog-Managed Tables
  slug: delta-catalog
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delta-lake-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deltalake
- group: company
  title: ''
  type: Website
  url: https://delta.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.delta.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/delta-io
- group: company
  title: ''
  type: Blog
  url: https://delta.io/blog/
- group: other
  title: ''
  type: LinuxFoundation
  url: https://lfaidata.foundation/projects/delta-lake/
- group: operate
  title: ''
  type: Slack
  url: https://go.delta.io/slack
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/delta-lake-vocabulary.yml
created: '2026-03-16'
description: Delta Lake is a graduated project of the Linux Foundation AI & Data Foundation providing an open source storage framework for building Lakehouse architectures. Originally contributed by Databricks, it adds reliability, quality, and performance to data lakes with ACID transactions, schema enforcement, time travel, and Iceberg/Hudi interoperability via UniForm. Delta Lake projects also include Delta Sharing (an open protocol for secure data sharing) and catalog-managed tables built on the Iceberg REST Catalog protocol.
finops:
- name: Delta Lake Finops
  service_category: API
  slug: delta-lake-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delta-lake.png
layout: provider
modified: '2026-04-28'
name: Delta Lake
nav: Providers
network: true
overview: 'Delta Lake publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Data Lake, Lakehouse, Linux Foundation, and Open Source.


  Delta Lake''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Delta Lake Plans Pricing
  plan_count: 3
  slug: delta-lake-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Delta Lake Rate Limits
  slug: delta-lake-rate-limits
score:
  band: emerging
  composite: 22.6
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 10.4
    operational_transparency: 36.8
  previous_composite: 25.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/delta-lake/refs/heads/main/screenshots/delta-lake-2026-06-20T175901.png
security:
- kind: domain-security
  name: Delta Lake Domain Security
  slug: delta-lake-domain-security
  summary_line: TLSv1.3 · HSTS
slug: delta-lake
tags:
- Data
- Data Lake
- Lakehouse
- Linux Foundation
- Open Source
- Storage
- Streaming
website: https://delta.io/
---
