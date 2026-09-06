---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Control-plane REST API for Onehouse — a SQL Command API to create and manage lakehouse resources (lakes, databases, tables, flows, clusters, jobs, transformations) plus a Status API to poll the return
  name: Onehouse API
  slug: onehouse-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://onehouse.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.onehouse.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onehouse.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onehouse.ai/api/overview
- group: company
  title: ''
  type: Blog
  url: https://www.onehouse.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onehouseinc
- group: start
  title: ''
  type: SignUp
  url: https://cloud.onehouse.ai/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.onehouse.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onehouse.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onehouse.ai/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onehouse.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.onehouse.ai/releases/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onehouse-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/onehouse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onehouse-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/onehouse-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onehouse-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onehouse-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onehouse-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onehouse-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onehouse-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.onehouse.ai/product/security
- group: design
  title: ''
  type: DataModel
  url: data-model/onehouse-data-model.yml
created: '2026-07-17'
description: Onehouse is a fully managed universal data lakehouse platform, built by the original creators of Apache Hudi. It provides near real-time data ingestion (CDC and streaming), incremental ETL/ELT pipelines, automated table optimization (compaction, clustering, cleaning), and open table-format interoperability across Apache Hudi, Apache Iceberg, and Delta Lake via Apache XTable. Onehouse Cloud, the Quanton execution engine, OneFlow ingestion, Open Engines, and LakeView are exposed programmatically through a control-plane SQL Command API plus Status API, an official Python SDK, an `oh` CLI, and a Terraform provider, letting data teams manage lakes, databases, tables, flows, and clusters as code while data stays in the customer's own VPC.
image: https://cdn.prod.website-files.com/61f2440c9fcbc37831846652/61fa103590582964035abe0a_onehouse_wheel_256x256.png
layout: provider
modified: '2026-07-20'
name: Onehouse
nav: Providers
network: true
overview: 'Onehouse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Data Lakehouse, Data Engineering, and ETL.


  Onehouse''s developer surface includes documentation, API reference, engineering blog, signup flow, changelog, CLI, authentication, and 16 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onehouse/refs/heads/main/screenshots/onehouse-2026-08-07T190333.png
security:
- kind: authentication
  name: Onehouse Authentication
  slug: onehouse-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Onehouse Domain Security
  slug: onehouse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: onehouse
tags:
- Company
- Developer Tools
- Data Lakehouse
- Data Engineering
- ETL
- Apache Hudi
- Analytics
- Data Infrastructure
website: https://onehouse.ai
---
