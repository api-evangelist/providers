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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: REST API for the Polymer embedded analytics platform. Manage workspaces and users, connect and sync data sources (Snowflake, BigQuery, uploads), create and update datasets, compose boards from visuali
  name: Polymer Embedded Analytics API
  slug: polymer-embedded-analytics-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polymer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.polymersearch.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.polymersearch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.polymersearch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.polymersearch.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.polymersearch.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://www.polymersearch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.polymersearch.com/blog
- group: operate
  title: ''
  type: Support
  url: https://polymersearch.notion.site/Help-Center-1b21de28d1504770bf79beaeb2610bc1
- group: start
  title: ''
  type: SignUp
  url: https://v3.polymersearch.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polymersearch.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polymersearch.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PolymerSearch
- group: operate
  title: ''
  type: StatusPage
  url: https://status.polymersearch.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/polymer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polymer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/polymer-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/polymer-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/polymer-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polymer-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polymer-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/polymer-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polymer-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polymer-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/polymer-well-known.yml
created: '2026-07-17'
description: Polymer (Polymer Search) is an AI-driven embedded analytics and business intelligence platform that lets teams and product developers turn raw spreadsheet, database, and SaaS data into interactive dashboards, charts, and visualizations without a data analyst. Its REST API lets developers create workspaces, connect data sources (Snowflake, BigQuery, CSV/JSON uploads), build boards composed of visualization blocks, and embed white-labeled, permission-scoped dashboards directly into their own applications with a few lines of code. Authentication is via API key, with short-lived embed tokens for end-user access. Polymer is backed by Sierra Ventures and 500 Global.
image: https://www.polymersearch.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Polymer MCP Server (candidate)
  slug: polymer-mcp-server-candidate
modified: '2026-07-20'
name: Polymer
nav: Providers
network: true
overview: 'Polymer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Business Intelligence, Data Visualization, and Embedded Analytics.


  Polymer''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 18 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 28.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Polymer Authentication
  slug: polymer-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Polymer Domain Security
  slug: polymer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polymer
tags:
- Company
- Analytics
- Business Intelligence
- Data Visualization
- Embedded Analytics
- Dashboards
- Data
- Artificial Intelligence
website: https://www.polymersearch.com
---
