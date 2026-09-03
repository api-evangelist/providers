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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'HTTP API behind the Upsolver SQLake platform, used by the first-party Python SDK (DB API 2.0), CLI, and dbt adapter to execute SQLake SQL statements (DDL, DML, continuous data loading). Authenticated '
  name: Upsolver SQLake API
  slug: upsolver-sqlake-api
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/qlik/
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
overview: 'Upsolver publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Pipeline, Data Lakehouse, and Streaming.


  Upsolver''s developer surface includes documentation, changelog, CLI, authentication, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 17.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upsolver/refs/heads/main/screenshots/upsolver-2026-09-02T165119.png
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
- Data Pipeline
- Data Lakehouse
- Streaming
- ETL
- SQL
- Apache Iceberg
website: https://www.upsolver.com/
---
