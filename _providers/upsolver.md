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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
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
  href: https://artifacts.apis.io/upsolver/changelog/upsolver-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/upsolver-changelog.yml
- group: design
  href: https://artifacts.apis.io/upsolver/lifecycle/upsolver-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/upsolver-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/upsolver/packages/upsolver-packages.yml
  title: ''
  type: Packages
  url: packages/upsolver-packages.yml
- group: build
  href: https://artifacts.apis.io/upsolver/packages/upsolver-packages.yml
  title: ''
  type: SDKs
  url: packages/upsolver-packages.yml
- group: build
  href: https://artifacts.apis.io/upsolver/cli/upsolver-cli.yml
  title: ''
  type: CLI
  url: cli/upsolver-cli.yml
- group: auth
  href: https://artifacts.apis.io/upsolver/authentication/upsolver-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upsolver-authentication.yml
- group: agent
  href: https://artifacts.apis.io/upsolver/llms/upsolver-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upsolver-llms.txt
- group: auth
  href: https://artifacts.apis.io/upsolver/security/upsolver-domain-security.yml
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
overview: 'Upsolver is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Pipeline, Data Lakehouse, and Streaming.


  Upsolver''s developer surface includes documentation, changelog, CLI, authentication, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 16.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/upsolver/upsolver-2026-09-02T165119.png
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
