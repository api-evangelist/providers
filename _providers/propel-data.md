---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Propel Data Agentic Access
  operation_count: 2
  slug: propel-data-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: The GraphQL API from Propel — 1 operation(s) for graphql.
  name: Propel GraphQL API
  slug: propel-data-graphql-api
- description: The OAuth2 API from Propel — 1 operation(s) for oauth2.
  name: Propel OAuth2 API
  slug: propel-data-oauth2-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Propel GraphQL API
  slug: open-propel-data-graphql-api
- collection_type: open
  name: Propel GraphQL OAuth2 API
  slug: open-propel-data-oauth2-api
- collection_type: open
  name: Propel API
  slug: open-propel-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/propel-data-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/propel-data-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/propel-data-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/propeldata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/propeldata
- group: company
  title: ''
  type: Website
  url: https://www.propeldata.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.propeldata.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/propel-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/propel-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/propel-data-finops.yml
created: '2026-06-20'
description: Propel is a customer-facing analytics platform that puts a fast GraphQL analytics API in front of a data warehouse. Teams connect a Data Source (Snowflake, BigQuery, S3, Redshift, ClickHouse, Postgres, Kafka, webhooks), sync it into high-speed Data Pools, define Metrics, and serve sub-second Counter, Time Series, and Leaderboard queries to in-product dashboards, with multi-tenant Policies and OAuth2 Applications for access control.
finops:
- name: Propel Data Finops
  service_category: Analytics
  slug: propel-data-finops
graphqls:
- description: GraphQL interface for the [Propel](https://www.propeldata.com/) customer-facing
  name: Propel GraphQL API
  slug: propel-data-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/propel-data.png
layout: provider
modified: '2026-06-20'
name: Propel
nav: Providers
network: true
overview: 'Propel publishes 2 APIs on the [APIs.io](https://apis.io/) network: GraphQL API and OAuth2 API. Tagged areas include Analytics, GraphQL, Data Warehouse, Metrics, and Customer Facing Analytics.


  Propel''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Propel Data Plans Pricing
  plan_count: 3
  slug: propel-data-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Propel Data Rate Limits
  slug: propel-data-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.7
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/propel-data/refs/heads/main/screenshots/propel-data-2026-06-20T192200.png
security:
- kind: authentication
  name: Propel Data Authentication
  slug: propel-data-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Propel Data Domain Security
  slug: propel-data-domain-security
  summary_line: TLSv1.3 · DMARC
slug: propel-data
tags:
- Analytics
- GraphQL
- Data Warehouse
- Metrics
- Customer Facing Analytics
website: https://www.propeldata.com
---
