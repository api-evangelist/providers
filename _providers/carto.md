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
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Carto Agentic Access
  operation_count: 4
  slug: carto-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 10
apis:
- description: Serves vector tables, SQL-query-backed tilesets, tileset sources, and raster/H3/quadbin tilesets for visualization in deck.gl, MapLibre, Google Maps, Amazon Location, or Mapbox GL clients.
  name: CARTO Maps API
  slug: maps-api
- description: Executes SQL (including CARTO's spatial functions and analytics extensions) against a connected data warehouse from applications, returning GeoJSON / JSON results for spatial analysis, scoring, and da
  name: CARTO SQL API
  slug: sql-api
- description: Executes visually-designed CARTO Workflows (spatial data pipelines) programmatically, enabling scheduled, CI-driven, or application- triggered spatial analytics runs.
  name: CARTO Workflows API
  slug: workflows-api
- description: Ingests files and URLs (CSV, GeoJSON, Shapefile, etc.) into a user's connected CARTO data warehouse for downstream spatial analysis and mapping.
  name: CARTO Import API
  slug: import-api
- description: Curated catalog of third-party spatial datasets (demographics, POIs, mobility, financial, environmental) accessible via subscription and queryable directly from the customer's cloud data warehouse.
  name: CARTO Data Observatory
  slug: data-observatory
- description: Manages CARTO user accounts, organizations, and API access tokens, including OAuth clients used for secure programmatic access.
  name: CARTO Accounts API
  slug: accounts-api
- description: Client library providing deck.gl layers for CARTO vector, H3, quadbin, raster, and query sources, simplifying application-layer integration with the Maps API.
  name: CARTO for deck.gl
  slug: deck-gl
- description: React library of components and hooks for building CARTO-powered location intelligence applications with widgets, filters, and deck.gl map integration.
  name: CARTO for React
  slug: carto-for-react
- description: The Jobs API from Carto — 2 operation(s) for jobs.
  name: Carto Jobs API
  slug: carto-jobs-api
- description: The SQL API from Carto — 1 operation(s) for sql.
  name: Carto SQL API
  slug: carto-sql-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CARTO Platform Jobs API
  slug: open-carto-jobs-api
- collection_type: open
  name: CARTO Platform Jobs SQL API
  slug: open-carto-sql-api
- collection_type: open
  name: CARTO Platform API
  slug: open-carto
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carto-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/CartoDB/agent-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carto
- group: company
  title: ''
  type: Website
  url: https://carto.com
- group: start
  title: ''
  type: Portal
  url: https://docs.carto.com/
- group: other
  title: ''
  type: Developer
  url: https://docs.carto.com/carto-for-developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.carto.com/getting-started/quickstart-guides
- group: auth
  title: ''
  type: Authentication
  url: https://docs.carto.com/carto-for-developers/fundamentals/authorization
- group: operate
  title: ''
  type: FAQ
  url: https://docs.carto.com/faqs
- group: other
  title: ''
  type: WhatsNew
  url: https://docs.carto.com/whats-new
- group: other
  title: ''
  type: Glossary
  url: https://carto.com/glossary
- group: learn
  title: ''
  type: Webinars
  url: https://carto.com/webinars
- group: company
  title: ''
  type: Blog
  url: https://carto.com/blog
- group: company
  title: ''
  type: Partners
  url: https://carto.com/partners
- group: commercial
  title: ''
  type: Pricing
  url: https://carto.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://docs.carto.com/faqs/support-packages
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carto.com
- group: start
  title: ''
  type: Login
  url: https://auth.carto.com/u/login
- group: start
  title: ''
  type: Signup
  url: https://auth.carto.com/u/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carto.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carto.com/privacy
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/CartoDB
- group: agent
  title: ''
  type: MCPServer
  url: https://carto.com/blog/carto-mcp-server-turn-your-ai-agents-into-geospatial-experts/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.carto.com/llms.txt
created: '2025-01-08'
description: CARTO is a cloud-native location intelligence platform that lets developers and analysts build spatial applications directly on top of modern data warehouses (BigQuery, Snowflake, Redshift, Databricks). It exposes a Maps API for vector and tileset map data, an SQL API for spatial analytics, a Workflows API for executing no-code spatial pipelines, an Import API for data ingestion, and the Data Observatory for curated third-party spatial datasets — all backed by OAuth access tokens and API access tokens.
finops:
- name: Carto Finops
  service_category: API
  slug: carto-finops
graphqls:
- description: This conceptual GraphQL schema models the CARTO location intelligence and spatial analytics platform. CARTO exposes REST APIs for Maps, SQL analytics, Workflows, Data Import, Data Observatory, and Acc
  name: CARTO GraphQL Schema
  slug: carto-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carto.png
jsonld:
- class_count: 0
  name: Carto Context
  property_count: 9
  slug: carto-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Carto
nav: Providers
network: true
overview: 'Carto publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jobs API and SQL API. Tagged areas include Location Intelligence, Geospatial, Mapping, GIS, and SQL.


  The Carto catalog on APIs.io includes 1 JSON-LD context.


  Carto''s developer surface includes authentication, developer portal, getting-started guide, FAQ, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Carto Plans Pricing
  plan_count: 3
  slug: carto-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Carto Rate Limits
  slug: carto-rate-limits
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.1
    developer_ergonomics: 52.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carto/refs/heads/main/screenshots/carto-2026-06-20T174026.png
security:
- kind: authentication
  name: Carto Authentication
  slug: carto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Carto Domain Security
  slug: carto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 23
skills:
- name: carto-arcgis-migration
  slug: carto-arcgis-migration
- name: carto-basics
  slug: carto-basics
- name: carto-composite-scoring
  slug: carto-composite-scoring
- name: carto-connect-datawarehouse
  slug: carto-connect-datawarehouse
- name: carto-create-builder-maps
  slug: carto-create-builder-maps
- name: carto-create-workflow
  slug: carto-create-workflow
- name: carto-develop-app
  slug: carto-develop-app
- name: carto-explore-datawarehouse
  slug: carto-explore-datawarehouse
- name: carto-find-spatial-data
  slug: carto-find-spatial-data
- name: carto-geocoding
  slug: carto-geocoding
- name: carto-gwr
  slug: carto-gwr
- name: carto-hotspot-analysis
  slug: carto-hotspot-analysis
- name: carto-import-export-data
  slug: carto-import-export-data
- name: carto-manage-platform
  slug: carto-manage-platform
- name: carto-preview-builder-map
  slug: carto-preview-builder-map
- name: carto-query-datawarehouse
  slug: carto-query-datawarehouse
- name: carto-render-inline-map
  slug: carto-render-inline-map
- name: carto-routing-od-analysis
  slug: carto-routing-od-analysis
- name: carto-site-selection
  slug: carto-site-selection
- name: carto-spatial-autocorrelation
  slug: carto-spatial-autocorrelation
- name: carto-spatial-enrichment
  slug: carto-spatial-enrichment
- name: carto-territory-planning
  slug: carto-territory-planning
- name: carto-trade-area-analysis
  slug: carto-trade-area-analysis
slug: carto
tags:
- Location Intelligence
- Geospatial
- Mapping
- GIS
- SQL
- BigQuery
- Snowflake
- Data Warehouse
website: https://carto.com
---
