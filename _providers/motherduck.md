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
    agent_skills: true
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
  score: 7.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Clients connect to MotherDuck through DuckDB's native protocol using a connection string of the form `md:` plus an access token. Officially supported clients include DuckDB CLI, Python, Node.js, JDBC,
  name: MotherDuck DuckDB Connection
  slug: motherduck-duckdb-protocol
artifact_total: 29
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motherduck-domain-security.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/motherduckdb/agent-skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/motherduckdb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/motherduck
- group: company
  title: ''
  type: Website
  url: https://motherduck.com/
- group: start
  title: ''
  type: Portal
  url: https://motherduck.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://motherduck.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/motherduck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/motherduck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/motherduck-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://motherduck.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://motherduck.com/rss.xml
created: '2026-05-08'
description: MotherDuck is a serverless cloud data warehouse built on DuckDB. Connectivity is via DuckDB clients (Python, Node.js, Wasm, Go, JDBC) using access tokens or SSO; the service does not publicly document a separate REST management API.
finops:
- name: Motherduck Finops
  service_category: API
  slug: motherduck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/motherduck.png
layout: provider
modified: '2026-05-08'
name: MotherDuck
nav: Providers
network: true
overview: 'MotherDuck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Warehouse, Serverless, DuckDB, SQL, and Analytics.


  MotherDuck''s developer surface includes developer portal, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Motherduck Plans Pricing
  plan_count: 3
  slug: motherduck-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Motherduck Rate Limits
  slug: motherduck-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motherduck/refs/heads/main/screenshots/motherduck-2026-06-20T185824.png
security:
- kind: domain-security
  name: Motherduck Domain Security
  slug: motherduck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 56
skills:
- name: motherduck-build-cfa-app
  slug: motherduck-build-cfa-app-2
- name: motherduck-build-cfa-app
  slug: motherduck-build-cfa-app-3
- name: motherduck-build-cfa-app
  slug: motherduck-build-cfa-app
- name: motherduck-build-dashboard
  slug: motherduck-build-dashboard-2
- name: motherduck-build-dashboard
  slug: motherduck-build-dashboard-3
- name: motherduck-build-dashboard
  slug: motherduck-build-dashboard
- name: motherduck-build-data-pipeline
  slug: motherduck-build-data-pipeline-2
- name: motherduck-build-data-pipeline
  slug: motherduck-build-data-pipeline-3
- name: motherduck-build-data-pipeline
  slug: motherduck-build-data-pipeline
- name: motherduck-connect
  slug: motherduck-connect-2
- name: motherduck-connect
  slug: motherduck-connect-3
- name: motherduck-connect
  slug: motherduck-connect
- name: motherduck-create-dive
  slug: motherduck-create-dive-2
- name: motherduck-create-dive
  slug: motherduck-create-dive-3
- name: motherduck-create-dive
  slug: motherduck-create-dive
- name: motherduck-create-flight
  slug: motherduck-create-flight-2
- name: motherduck-create-flight
  slug: motherduck-create-flight
- name: motherduck-duckdb-sql
  slug: motherduck-duckdb-sql-2
- name: motherduck-duckdb-sql
  slug: motherduck-duckdb-sql-3
- name: motherduck-duckdb-sql
  slug: motherduck-duckdb-sql
- name: motherduck-ducklake
  slug: motherduck-ducklake-2
- name: motherduck-ducklake
  slug: motherduck-ducklake-3
- name: motherduck-ducklake
  slug: motherduck-ducklake
- name: motherduck-enable-self-serve-analytics
  slug: motherduck-enable-self-serve-analytics-2
slug: motherduck
tags:
- Data Warehouse
- Serverless
- DuckDB
- SQL
- Analytics
website: https://motherduck.com/
---
