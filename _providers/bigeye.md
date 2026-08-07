---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 158
  human_in_the_loop: 5
  name: Bigeye Agentic Access
  operation_count: 263
  slug: bigeye-agentic-access
  summary_line: 263 operations · 158 acting · 5 human-in-the-loop
api_count: 4
apis:
- description: 'The Bigeye Metadata API covers the data catalog and workspace administration surface: sources, schemas, tables, columns and virtual tables; catalog rebuilds and schema-change tracking; lineage (v1 and'
  name: Bigeye Metadata API
  slug: bigeye-metadata-api
- description: 'The Bigeye Observability API covers monitoring and data quality: metrics (monitors) and metric templates, custom SQL rules, autometrics, backfills and batch metric runs, collections of monitors, delta'
  name: Bigeye Observability API
  slug: bigeye-observability-api
- description: 'The Bigeye Sensitivity API covers sensitive data discovery and classification: classifiers, data classes and data class categories, scan jobs and scan job configuration, scan runs, and the aggregate a'
  name: Bigeye Sensitivity API
  slug: bigeye-sensitivity-api
- description: The Bigeye MCP Gateway is a hosted Model Context Protocol server at https://mcpgateway.bigeye.com/mcp that exposes 56 tools over the Bigeye platform for AI assistants and agents — listing and triaging
  name: Bigeye MCP Gateway
  slug: bigeye-mcp-gateway
artifact_total: 11
asyncapis:
- description: ''
  name: Bigeye Webhooks
  slug: bigeye-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigeye-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bigeye-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bigeye-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigeye-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigeye-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigeye.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bigeye.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bigeye.com/docs/api-user-guide
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bigeye.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bigeye.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.bigeye.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.bigeye.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigeyedata
- group: start
  title: ''
  type: SignUp
  url: https://app.bigeye.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigeye.com/terms/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigeye.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigeye.com/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.bigeye.com/docs/security-and-compliance
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bigeye.com/docs/release-notes
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bigeye-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bigeye-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/bigeye-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bigeye-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/bigeye-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bigeye-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bigeye-cli.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bigeye-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bigeye-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bigeye-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bigeye-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bigeye-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bigeye-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bigeye-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bigeye.com/platform/security
- group: other
  title: ''
  type: Overlay
  url: overlays/bigeye-metadata-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bigeye-changelog.yml
created: '2026-08-02'
description: 'Bigeye is an enterprise data observability and AI trust platform that monitors data quality, detects schema changes and anomalies, classifies sensitive data, and maps column-level lineage across warehouses, lakes, BI tools and ETL pipelines. The platform combines automated data quality monitoring, ML-powered anomaly detection and lineage-based root-cause and downstream-impact analysis so teams can find and resolve data issues before they reach dashboards, reports or AI systems. Bigeye is API-first: its REST API is published as three OpenAPI 3.0 definitions (Metadata, Observability and Sensitivity) covering 263 operations, and it ships a first-party Python SDK, a Python CLI, Airflow operators, YAML-based observability-as-code configuration, and a hosted Model Context Protocol gateway that exposes 56 agent tools over the same platform.'
image: https://cdn.prod.website-files.com/64b205c9041f2a26ac7cb23f/69135c34ecede8d3fb8c6be8_bigeye-logo-1200x1200.jpg
layout: provider
mcp_servers:
- description: ''
  name: bigeye-mcp.yml
  slug: bigeye-mcpyml
modified: '2026-08-02'
name: Bigeye
nav: Providers
network: true
overview: 'Bigeye publishes 3 APIs on the [APIs.io](https://apis.io/) network: Metadata API, Observability API, and Sensitivity API. Tagged areas include Company, Data Observability, Data Quality, Data Lineage, and Data Governance.


  The Bigeye catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bigeye''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 30 more developer resources.'
random_paper: 64
score:
  band: strong
  composite: 57.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.1
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Bigeye Authentication
  slug: bigeye-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bigeye Domain Security
  slug: bigeye-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bigeye Vulnerability Disclosure
  slug: bigeye-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Bigeye Trust Center
  slug: bigeye-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
slug: bigeye
tags:
- Company
- Data Observability
- Data Quality
- Data Lineage
- Data Governance
- Metadata Management
- Data Catalog
- Sensitive Data Discovery
- Monitoring
- Analytics
- AI Trust
- Snowflake
- Databricks
website: https://www.bigeye.com/
---
