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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/delta-io/delta/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/delta-io/delta/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/delta-io/delta/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/delta-io/delta/blob/master/LICENSE
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
overview: 'Delta Lake publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Data Lake, Lakehouse, Linux Foundation, and Open-Source.


  Delta Lake''s developer surface includes documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Delta Lake Plans Pricing
  plan_count: 3
  slug: delta-lake-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Delta Lake Rate Limits
  slug: delta-lake-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 23.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Open-Source
- Storage
- Streaming
website: https://delta.io/
---
