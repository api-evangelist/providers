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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Sifflet''s public REST API for programmatically managing data observability resources — assets and workspaces, monitors/rules and rule runs, sources (V2), credentials, domains, calendars, notification '
  name: Sifflet Public API
  slug: sifflet-public-api
artifact_total: 7
asyncapis:
- description: ''
  name: Sifflet Webhooks
  slug: sifflet-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.siffletdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.siffletdata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.siffletdata.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.siffletdata.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.siffletdata.com/docs/cli-command-line-interface
- group: company
  title: ''
  type: Blog
  url: https://www.siffletdata.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.siffletdata.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siffletdata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siffletdata.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/siffletdata
- group: operate
  title: ''
  type: StatusPage
  url: https://status.siffletdata.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.siffletdata.com/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: security/sifflet-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.siffletdata.com/product-security
- group: auth
  title: ''
  type: Security
  url: https://docs.siffletdata.com/docs/how-to-report-a-security-incident
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sifflet-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sifflet-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sifflet-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/sifflet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sifflet-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sifflet-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sifflet-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sifflet-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sifflet-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sifflet-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sifflet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sifflet-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sifflet-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sifflet-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sifflet-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sifflet-vulnerability-disclosure.yml
created: '2026-07-17'
description: Sifflet is a data observability platform positioned as the control plane for Data and AI. It catches data issues before they reach the business, traces them to their root cause, and helps teams fix them fast. The platform unifies a data catalog, data quality monitoring, end-to-end data lineage (including field-level lineage), built-in security and access control, and AI-powered agents (Sentinel auto-monitoring, Sage root-cause analysis, and an AI chat/assistant) into one product. It integrates with major data platforms and tools including Snowflake, Databricks, BigQuery, Amazon Redshift, dbt, Apache Airflow, Fivetran, Tableau, Looker, and Power BI. Developers automate Sifflet through a public REST API (Bearer Access Token auth), a Python CLI, a Terraform provider, Airflow operators, outbound webhooks, and an official MCP server. Sifflet is a portfolio company of EQT Ventures.
image: https://cdn.prod.website-files.com/6745ca418d70ad1c8e2b8442/67915a6a3d805d3e9c024aff_sifflet-logo-color.svg
layout: provider
mcp_servers:
- description: Official Sifflet MCP (Model Context Protocol) Server. Bridges Sifflet's data observability APIs into IDEs and agent tools (e.g. Cursor). Authenticates with a Sifflet Access Token.
  name: Sifflet MCP Server
  slug: sifflet-mcp-server
modified: '2026-07-21'
name: Sifflet
nav: Providers
network: true
overview: 'Sifflet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Data Observability, Data Quality, and Data Catalog.


  The Sifflet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sifflet''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, changelog, authentication, and 24 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 44.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sifflet/refs/heads/main/screenshots/sifflet-2026-08-17T081845.png
security:
- kind: authentication
  name: Sifflet Authentication
  slug: sifflet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sifflet Domain Security
  slug: sifflet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sifflet Vulnerability Disclosure
  slug: sifflet-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Sifflet Trust Center
  slug: sifflet-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: sifflet
tags:
- Company
- Data Analytics
- Data Observability
- Data Quality
- Data Catalog
- Data Lineage
- Data Governance
- Monitoring
- Metadata
- AI Agents
website: https://www.siffletdata.com/
---
