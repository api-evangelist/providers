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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The CARTO Cloud-Native (v3) REST API surface — SQL API (query and async SQL jobs against a connected data warehouse), Maps API (vector/tile map instantiation), Import/Export API, Location Data Service
  name: CARTO Cloud-Native API
  slug: carto-cloud-native-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.carto.com/carto-for-developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.carto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.carto.com/carto-for-developers/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.carto.com/carto-for-developers/overview
- group: operate
  title: ''
  type: Support
  url: https://docs.carto.com/carto-user-manual/carto-support
- group: company
  title: ''
  type: Blog
  url: https://carto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CartoDB
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.carto.com/whats-new
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cartodb-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://carto.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.carto.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.carto.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carto.com/legal/tcs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carto.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cartodb-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cartodb-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cartodb-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cartodb-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/cartodb-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cartodb-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cartodb-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cartodb-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cartodb-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cartodb-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carto.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/cartodb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cartodb-domain-security.yml
created: '2026-07-17'
description: 'CARTO (formerly CartoDB) is a cloud-native location intelligence and spatial analytics platform that runs directly on top of modern cloud data warehouses including Google BigQuery, Snowflake, Amazon Redshift, Databricks, PostgreSQL and Oracle. Developers use the CARTO Cloud-Native (v3) APIs — SQL API, Maps API, Import/Export API, Location Data Services (geocoding, routing, isolines) and the Data Observatory — together with the deck.gl visualization stack, the CARTO for React library, and Python packages to build interactive geospatial applications and analytical workflows. CARTO is notably agent-native: it ships a hosted MCP Server, a first-party `carto` CLI, and a public catalog of 23 Agent Skills for spatial analysis. Authentication is via permanent API Access Tokens or Auth0-backed OAuth (SPA authorization-code and machine-to-machine client-credentials) scoped to the `carto-cloud-native-api` audience.'
image: https://carto.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: cartodb-mcp.yml
  slug: cartodb-mcpyml
modified: '2026-07-18'
name: CARTO
nav: Providers
network: true
overview: 'CARTO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Location Intelligence, Geospatial, and Maps.


  CARTO''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 21 more developer resources.'
random_paper: 39
scopes:
- name: Cartodb Scopes
  scope_count: 4
  slug: cartodb-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 40.5
  delta: -1.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 41.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cartodb/refs/heads/main/screenshots/cartodb-2026-07-25T204652.png
security:
- kind: authentication
  name: Cartodb Authentication
  slug: cartodb-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Cartodb Domain Security
  slug: cartodb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cartodb Trust Center
  slug: cartodb-trust-center
  summary_line: trust center published
slug: cartodb
tags:
- Company
- Developer Tools
- Location Intelligence
- Geospatial
- Maps
- Spatial Analytics
- Data Warehouse
- GIS
- Agents
website: https://docs.carto.com/carto-for-developers
---
