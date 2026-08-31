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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Monte Carlo Agentic Access
  operation_count: 1
  slug: monte-carlo-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: GraphQL API for the Monte Carlo data observability platform. Provides programmatic access to monitors, incidents, assets, lineage, custom rules, warehouses, lakes, metastores, and alerts. Authenticati
  name: Monte Carlo GraphQL API
  slug: graphql-api
- description: The Graphql API from Monte Carlo — 1 operation(s) for graphql.
  name: Monte Carlo Graphql API
  slug: monte-carlo-graphql-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Monte Carlo Graphql API
  slug: open-monte-carlo-graphql-api
- collection_type: open
  name: Monte Carlo GraphQL API
  slug: open-monte-carlo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monte-carlo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monte-carlo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monte-carlo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monte-carlo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monte-carlo-data
- group: company
  title: ''
  type: Website
  url: https://www.montecarlodata.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmontecarlo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monte-carlo-data
- group: commercial
  title: ''
  type: Pricing
  url: https://www.montecarlodata.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.montecarlodata.com/request-a-demo/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.getmontecarlo.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://montecarlodata.com/blog/feed/
created: '2026-05-11'
description: Monte Carlo is a data and AI observability platform that monitors data warehouses, lakes, and pipelines for freshness, volume, schema, and quality anomalies, helping data teams detect, resolve, and prevent data downtime across Snowflake, Databricks, BigQuery, Redshift, and other modern data stack tools. Monte Carlo exposes a GraphQL API at https://api.getmontecarlo.com/graphql used for programmatic access to monitors, incidents, lineage, assets, alerts, custom rules, and lake/metastore integrations, with a supporting Python SDK and CLI (pycarlo / montecarlo). Authentication uses an API Key ID and Token pair sent via headers.
graphqls:
- description: GraphQL API for the Monte Carlo data observability platform. Provides programmatic access to monitors, incidents, assets, lineage, custom rules, warehouses, lakes, metastores, and alerts. Authenticati
  name: Monte Carlo GraphQL API
  slug: monte-carlo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monte-carlo.png
layout: provider
modified: '2026-05-11'
name: Monte Carlo
nav: Providers
network: true
overview: 'Monte Carlo publishes 1 API on the [APIs.io](https://apis.io/) network: Graphql API. Tagged areas include Data Observability, Data Quality, Data Reliability, Data Lake, and Data Warehouse.


  Monte Carlo''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 59.9
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monte-carlo/refs/heads/main/screenshots/monte-carlo-2026-06-20T185743.png
security:
- kind: authentication
  name: Monte Carlo Authentication
  slug: monte-carlo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Monte Carlo Domain Security
  slug: monte-carlo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Monte Carlo Trust Center
  slug: monte-carlo-trust-center
  summary_line: SOC 2, ISO 27001
slug: monte-carlo
tags:
- Data Observability
- Data Quality
- Data Reliability
- Data Lake
- Data Warehouse
- Lineage
- Monitoring
- AI Observability
website: https://www.montecarlodata.com
---
