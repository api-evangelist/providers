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
- description: Etleap's external REST API for creating and managing connections, pipelines, models, dbt schedules, teams, and users. Uses HTTP Basic authentication.
  name: Etleap API v2
  slug: etleap-api-v2
artifact_total: 3
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.etleap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.etleap.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.etleap.com/docs/api-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.etleap.com/documentation/quickstarts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/etleap
- group: company
  title: ''
  type: Blog
  url: https://etleap.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.etleap.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://etleap.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://etleap.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.etleap.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/etleap-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/etleap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/etleap-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/etleap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/etleap-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/etleap-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/etleap-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/etleap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/etleap-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/etleap-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/etleap-domain-security.yml
created: '2026-07-17'
description: 'Etleap is a managed ETL and data-integration platform that streamlines data ingestion, transformation, and observability so data teams can build cloud data warehouses and lakes with minimal engineering effort. Originally built as an "autopilot" for Amazon Redshift, S3, and AWS Glue, Etleap now centers on Apache Iceberg as a data foundation: it continuously ingests operational data from 50+ databases, SaaS applications, event streams, and files; shapes it with visual data wrangling and dbt Core in a single pipeline; and keeps destination tables healthy with automated maintenance. Destinations include Amazon Redshift, Snowflake, Databricks, Amazon S3, and Iceberg. Etleap exposes a REST API v2 for creating and managing connections, pipelines, models, teams, and users, and ships an official Terraform provider generated from that API.'
image: https://framerusercontent.com/images/4uqulfTuAM7iY7udMPgBO6bEqME.png
layout: provider
modified: '2026-07-19'
name: Etleap
nav: Providers
network: true
overview: 'Etleap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, ETL, ELT, and Data Pipeline.


  Etleap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 27.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/etleap/refs/heads/main/screenshots/etleap-2026-07-25T213654.png
security:
- kind: authentication
  name: Etleap Authentication
  slug: etleap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Etleap Domain Security
  slug: etleap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: etleap
tags:
- Company
- Data Integration
- ETL
- ELT
- Data Pipeline
- Data Warehouse
- Data Lake
- Apache Iceberg
- Analytics
website: https://docs.etleap.com/
---
