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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'HTTP API behind the Upsolver SQLake platform, used by the first-party Python SDK (DB API 2.0), CLI, and dbt adapter to execute SQLake SQL statements (DDL, DML, continuous data loading). Authenticated '
  name: Upsolver SQLake API
  slug: upsolver-sqlake-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.upsolver.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.qlik.com/en-US/upsolver/sqlake/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Upsolver
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/upsolver-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upsolver-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/upsolver-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/upsolver-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/upsolver-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upsolver-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upsolver-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upsolver-domain-security.yml
created: '2026-07-17'
description: Upsolver is a cloud data ingestion and lakehouse pipeline company whose SQLake platform lets teams build and deploy high-scale streaming data pipelines using familiar SQL, with automatic schema evolution and Apache Iceberg optimization. Upsolver was acquired by Qlik and the product now continues as Qlik Open Lakehouse; the standalone Upsolver (SQLake) product is legacy, with documentation maintained under Qlik's help site and first-party Python SDK, CLI, and dbt tooling still published on PyPI.
image: https://avatars.githubusercontent.com/u/11595894?v=4
layout: provider
modified: '2026-07-21'
name: Upsolver
nav: Providers
network: true
overview: 'Upsolver publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Pipelines, Data Lakehouse, and Streaming.


  Upsolver''s developer surface includes documentation, changelog, CLI, authentication, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.0
  delta: -0.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Upsolver Authentication
  slug: upsolver-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Upsolver Domain Security
  slug: upsolver-domain-security
  summary_line: TLSv1.3 · DMARC
slug: upsolver
tags:
- Company
- Data
- Data Pipelines
- Data Lakehouse
- Streaming
- ETL
- SQL
- Apache Iceberg
website: https://www.upsolver.com/
---
