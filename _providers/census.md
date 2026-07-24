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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Census Agentic Access
  operation_count: 27
  slug: census-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 10
apis:
- description: The Census Activations REST API (formerly Census Management API) lets teams programmatically manage reverse ETL pipelines, sources, models, destinations, syncs, and sync runs. The API is region-scoped
  name: Census Activations REST API
  slug: census-activations-api
- description: 'Custom Destinations API lets partners declare the type of data a destination can process, the operations allowed on that data, and the loading mechanism so that Activations can orchestrate loads into '
  name: Census Custom Destinations API
  slug: census-custom-destinations-api
- description: Connect Links enable embedded Activations flows for Powered by Fivetran partners, letting end users configure destinations and syncs from within a host application via hosted URLs.
  name: Census Connect Links (Powered by Fivetran)
  slug: census-connect-links-api
- description: Destination connections to operational systems
  name: Census Destinations API
  slug: census-destinations-api
- description: Modeled queries that drive activations
  name: Census Models API
  slug: census-models-api
- description: Audience segments
  name: Census Segments API
  slug: census-segments-api
- description: Source connections to data warehouses
  name: Census Sources API
  slug: census-sources-api
- description: Sync executions
  name: Census SyncRuns API
  slug: census-syncruns-api
- description: Sync configurations
  name: Census Syncs API
  slug: census-syncs-api
- description: Organization-level workspace management
  name: Census Workspaces API
  slug: census-workspaces-api
artifact_total: 19
collections:
- collection_type: open
  name: Census Activations REST API
  slug: open-census
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/census-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/census-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/census-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/census-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getcensus
- group: company
  title: ''
  type: Website
  url: https://www.getcensus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fivetran.com/docs/activations/
- group: docs
  title: ''
  type: Reference
  url: https://fivetran.com/docs/activations/rest-api/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getcensus.com/basics/getting-started
- group: other
  title: ''
  type: Parent Company
  url: https://www.fivetran.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sutrolabs
created: '2026-03-27'
description: Census is a reverse ETL and data activation platform that syncs data from cloud data warehouses (Snowflake, BigQuery, Databricks, Redshift) into operational SaaS applications. Census was acquired by Fivetran and is now branded as Fivetran Activations, offering a REST API for managing workspaces, datasets, syncs, destinations, and custom destinations, plus embedded Activations (Connect Links) for Powered by Fivetran use cases.
finops:
- name: Census Finops
  service_category: API
  slug: census-finops
graphqls:
- description: Census (now Fivetran Activations) is a reverse ETL and data activation platform that syncs data from cloud data warehouses such as Snowflake, BigQuery, Databricks, and Redshift into operational SaaS a
  name: Census GraphQL API
  slug: census-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/census.png
layout: provider
modified: '2026-04-23'
name: Census
nav: Providers
network: true
overview: 'Census publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Destinations API, Models API, Segments API, and 4 more. Tagged areas include Connectors, Data Activation, Data Warehouse, Destinations, and Fivetran Activations.


  Census'' developer surface includes authentication, documentation, getting-started guide, GitHub presence, and 7 more developer resources.'
plans:
- name: Census Plans Pricing
  plan_count: 3
  slug: census-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Census Rate Limits
  slug: census-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.3
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/census/refs/heads/main/screenshots/census-2026-06-20T174116.png
security:
- kind: authentication
  name: Census Authentication
  slug: census-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Census Domain Security
  slug: census-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Census Trust Center
  slug: census-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: census
tags:
- Connectors
- Data Activation
- Data Warehouse
- Destinations
- Fivetran Activations
- Reverse ETL
- Unified API
website: https://www.getcensus.com/
---
