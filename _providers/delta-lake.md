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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Delta Lake storage framework defines the on-disk transaction log and protocol that adds ACID transactions, schema enforcement, and time travel to Parquet-based data lakes. Delta Lake exposes Spark
  name: Delta Lake Storage Framework
  slug: delta-lake-storage
- baseURL: https://sharing.delta.io/delta-sharing/
  baseurl_source: declared
  description: Delta Sharing is an open protocol for secure data sharing across organizations, defined as a REST API specification. Sharing servers expose endpoints for listing shares, schemas, and tables, and for r
  name: Delta Sharing Protocol
  slug: delta-sharing
- description: Catalog-managed Delta tables delegate table scan planning to an external catalog using the Iceberg REST Catalog protocol, enabling interoperability with Unity Catalog and other catalog services.
  name: Delta Catalog-Managed Tables
  slug: delta-catalog
artifact_total: 8
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/delta-lake-authentication.yml
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
  url: https://github.com/delta-io/delta/blob/master/LICENSE.txt
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
- group: build
  title: ''
  type: Packages
  url: packages/delta-lake-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/delta-lake-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/delta-lake-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/delta-lake-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/delta-lake-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/delta-lake-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/delta-lake-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/delta-lake-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/delta-lake-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/delta-lake-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/delta-lake-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/delta-lake-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.delta.io/delta-apidoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://delta.io/learn/getting-started
- group: operate
  title: ''
  type: Support
  url: https://delta.io/resources/getting-help
- group: operate
  title: ''
  type: Roadmap
  url: https://delta.io/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lfprojects.org/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lfprojects.org/policies/privacy-policy/
created: '2026-03-16'
description: Delta Lake is a graduated project of the Linux Foundation AI & Data Foundation providing an open source storage framework for building Lakehouse architectures. Originally contributed by Databricks, it adds reliability, quality, and performance to data lakes with ACID transactions, schema enforcement, time travel, and Iceberg/Hudi interoperability via UniForm. Delta Lake projects also include Delta Sharing (an open protocol for secure data sharing) and catalog-managed tables built on the Iceberg REST Catalog protocol.
finops:
- name: Delta Lake Finops
  service_category: API
  slug: delta-lake-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delta-lake.png
layout: provider
modified: '2026-09-05'
name: Delta Lake
nav: Providers
network: true
overview: 'Delta Lake publishes 1 API on the [APIs.io](https://apis.io/) network: Delta Sharing Protocol. Tagged areas include Data, Data Lake, Lakehouse, Linux Foundation, and Open-Source.


  Delta Lake''s developer surface includes authentication, documentation, engineering blog, changelog, sandbox, API reference, getting-started guide, and 26 more developer resources.'
plans:
- name: Delta Lake Plans Pricing
  plan_count: 0
  slug: delta-lake-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Delta Lake Rate Limits
  slug: delta-lake-rate-limits
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 33.3
    contract_quality: 50.9
    developer_ergonomics: 63.7
    discoverability: 72.2
    governance: 33.3
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 65.0
  previous_composite: 23.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/delta-lake/refs/heads/main/screenshots/delta-lake-2026-06-20T175901.png
security:
- kind: authentication
  name: Delta Lake Authentication
  slug: delta-lake-authentication
  summary_line: http · 1 scheme
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
