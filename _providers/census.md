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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Census Agentic Access
  operation_count: 27
  slug: census-agentic-access
  summary_line: 27 operations · 15 acting
api_count: 1
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
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Destination connections to operational systems
  name: Census Destinations API
  slug: census-destinations-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Modeled queries that drive activations
  name: Census Models API
  slug: census-models-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Audience segments
  name: Census Segments API
  slug: census-segments-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Source connections to data warehouses
  name: Census Sources API
  slug: census-sources-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Sync executions
  name: Census SyncRuns API
  slug: census-syncruns-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Sync configurations
  name: Census Syncs API
  slug: census-syncs-api
- baseURL: https://app.getcensus.com/api/v1
  baseurl_source: spec
  description: Organization-level workspace management
  name: Census Workspaces API
  slug: census-workspaces-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Census Activations REST Destinations API
  slug: open-census-destinations-api
- collection_type: open
  name: Census Activations REST Destinations Models API
  slug: open-census-models-api
- collection_type: open
  name: Census Activations REST Destinations Segments API
  slug: open-census-segments-api
- collection_type: open
  name: Census Activations REST Destinations Sources API
  slug: open-census-sources-api
- collection_type: open
  name: Census Activations REST Destinations SyncRuns API
  slug: open-census-syncruns-api
- collection_type: open
  name: Census Activations REST Destinations Syncs API
  slug: open-census-syncs-api
- collection_type: open
  name: Census Activations REST Destinations Workspaces API
  slug: open-census-workspaces-api
- collection_type: open
  name: Census Activations REST API
  slug: open-census
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/fivetran/
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
- group: other
  title: ''
  type: Activations
  url: https://fivetran.com/docs/activations
- group: start
  title: ''
  type: Signup
  url: https://www.getcensus.com/
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
modified: '2026-08-08'
name: Census
nav: Providers
network: true
overview: 'Census publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Destinations API, Models API, Segments API, and 4 more. Tagged areas include Connectors, Data Activation, Data Warehouse, Destinations, and Fivetran Activations.


  Census'' developer surface includes authentication, documentation, getting-started guide, GitHub presence, signup flow, and 9 more developer resources.'
plans:
- name: Census Plans Pricing
  plan_count: 3
  slug: census-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Census Rate Limits
  slug: census-rate-limits
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 23.2
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 26.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/census/refs/heads/main/screenshots/census-2026-06-20T174117.png
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
- Unified-API
website: https://www.getcensus.com/
---
