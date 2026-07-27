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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 21.2
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Etleap's external REST API for creating and managing connections, pipelines, models, dbt schedules, teams, and users. Uses HTTP Basic authentication.
  name: Etleap API v2
  slug: etleap-api-v2
artifact_total: 4
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: etleap-mcp.yml
  slug: etleap-mcpyml
modified: '2026-07-19'
name: Etleap
nav: Providers
network: true
overview: 'Etleap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, ETL, ELT, and Data Pipelines.


  Etleap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 15 more developer resources.'
random_paper: 23
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Data Pipelines
- Data Warehouse
- Data Lake
- Apache Iceberg
- Analytics
website: https://docs.etleap.com/
---
