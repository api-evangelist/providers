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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for Dremio Cloud covering the Open Catalog (sources, folders, tables, views, wikis, tags, lineage), SQL query execution and job management, Reflections, engines, projects, users, roles, grant
  name: Dremio Cloud REST API
  slug: dremio-cloud-rest-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dremio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dremio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dremio.com/dremio-cloud/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dremio.com/dremio-cloud/get-started/quick-tour
- group: start
  title: ''
  type: SignUp
  url: https://www.dremio.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dremio.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dremio.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dremio.com/legal/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.dremio.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://community.dremio.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dremio
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dremio.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.dremio.com/current/release-notes/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dremio.com/dremio-cloud/changelog/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.dremio.com/dremio-cloud/security/compliance
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dremio-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/dremio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dremio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dremio-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dremio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dremio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/dremio-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dremio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dremio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dremio-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dremio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dremio.com/platform/security/responsible-disclosure-limitations/
- group: auth
  title: ''
  type: TrustCenter
  url: security/dremio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dremio-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dremio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dremio-changelog.yml
created: '2026-07-17'
description: Dremio is a data lakehouse platform for running high-performance SQL queries directly on cloud object storage and data lakes without moving or copying data. It combines an Apache Arrow-based MPP query engine, Autonomous Reflections for acceleration, and an Apache Iceberg / Apache Polaris-powered Open Catalog into a self-service semantic layer for analytics and agentic AI. Dremio is delivered as a fully managed service (Dremio Cloud) and a self-managed deployment (Dremio Enterprise), and exposes a REST API, Apache Arrow Flight SQL, Arrow Flight SQL JDBC/ODBC drivers, a developer CLI, a dbt adapter, and an official Model Context Protocol (MCP) server for connecting AI agents to the lakehouse.
image: https://www.dremio.com/wp-content/uploads/2023/01/dremio-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Dremio MCP Server
  slug: dremio-mcp-server
modified: '2026-07-18'
name: Dremio
nav: Providers
network: true
overview: 'Dremio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Lakehouse, Analytics, SQL Query Engine, and Apache Iceberg.


  Dremio''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 24 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 43.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dremio/refs/heads/main/screenshots/dremio-2026-07-25T212402.png
security:
- kind: authentication
  name: Dremio Authentication
  slug: dremio-authentication
  summary_line: http/oauth2/apiKey · 4 schemes
- kind: domain-security
  name: Dremio Domain Security
  slug: dremio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dremio Vulnerability Disclosure
  slug: dremio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dremio Trust Center
  slug: dremio-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, HIPAA, GDPR, CCPA/CPRA
slug: dremio
tags:
- Company
- Data Lakehouse
- Analytics
- SQL Query Engine
- Apache Iceberg
- Apache Arrow
- Data Catalog
- Semantic Layer
- AI Agents
- MCP
website: https://docs.dremio.com/
---
