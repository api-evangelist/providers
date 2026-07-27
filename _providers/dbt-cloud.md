---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Dbt Cloud Agentic Access
  operation_count: 18
  slug: dbt-cloud-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 7
apis:
- description: GraphQL API for fetching metadata about the state and health of a dbt project - models, sources, tests, exposures, lineage/DAG, and execution results - queried with a Metadata Only service token again
  name: dbt Cloud Discovery (Metadata) API
  slug: dbt-cloud-discovery-api
- description: APIs for querying governed metrics and dimensions defined in the dbt Semantic Layer - a GraphQL API and a JDBC driver (ArrowFlight SQL) - with standard metadata functionality, authorized via service t
  name: dbt Cloud Semantic Layer API
  slug: dbt-cloud-semantic-layer-api
- description: Account configuration and details.
  name: dbt Cloud Accounts API
  slug: dbt-cloud-accounts-api
- description: Job definitions and triggering of job runs.
  name: dbt Cloud Jobs API
  slug: dbt-cloud-jobs-api
- description: dbt projects within an account.
  name: dbt Cloud Projects API
  slug: dbt-cloud-projects-api
- description: Artifacts (manifest, catalog, run results) produced by runs.
  name: dbt Cloud Run Artifacts API
  slug: dbt-cloud-run-artifacts-api
- description: Job run history, status, and lifecycle.
  name: dbt Cloud Runs API
  slug: dbt-cloud-runs-api
artifact_total: 15
collections:
- collection_type: open
  name: dbt Cloud Administrative API
  slug: open-dbt-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dbt-cloud-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dbt-cloud-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dbt-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dbt-cloud-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dbt-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dbtlabsinc
- group: company
  title: ''
  type: Website
  url: https://www.getdbt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getdbt.com/docs/dbt-cloud-apis/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/dbt-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dbt-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dbt-cloud-finops.yml
created: '2026-06-21'
description: dbt Cloud is the analytics-engineering platform from dbt Labs for transforming data in the warehouse. It exposes the Administrative API for managing accounts, projects, jobs, runs, and environments, the Discovery (Metadata) API for project metadata and lineage via GraphQL, and the Semantic Layer API for querying governed metrics over GraphQL and JDBC.
finops:
- name: Dbt Cloud Finops
  service_category: Analytics
  slug: dbt-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dbt-cloud.png
layout: provider
modified: '2026-06-21'
name: dbt Cloud
nav: Providers
network: true
overview: 'dbt Cloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Jobs API, Projects API, and 2 more. Tagged areas include Data, Analytics Engineering, Data Transformation, ELT, and Semantic Layer.


  dbt Cloud''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Dbt Cloud Plans Pricing
  plan_count: 4
  slug: dbt-cloud-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Dbt Cloud Rate Limits
  slug: dbt-cloud-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dbt-cloud/refs/heads/main/screenshots/dbt-cloud-2026-07-25T211455.png
security:
- kind: authentication
  name: Dbt Cloud Authentication
  slug: dbt-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dbt Cloud Domain Security
  slug: dbt-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dbt Cloud Trust Center
  slug: dbt-cloud-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: dbt-cloud
tags:
- Data
- Analytics Engineering
- Data Transformation
- ELT
- Semantic Layer
website: https://www.getdbt.com
---
