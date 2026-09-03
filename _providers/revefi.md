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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://gateway.revefi.com/api/v1/
  baseurl_source: declared
  description: The Create a Custom Data Quality Monitor API from Revefi — 1 operation(s) for create a custom data quality monitor.
  name: Revefi Create a Custom Data Quality Monitor API
  slug: revefi-create-a-custom-data-quality-monitor-api
- baseURL: https://gateway.revefi.com/api/v1/
  baseurl_source: declared
  description: The Delete an existing Custom Data Quality Monitor API from Revefi — 1 operation(s) for delete an existing custom data quality monitor.
  name: Revefi Delete an existing Custom Data Quality Monitor API
  slug: revefi-delete-an-existing-custom-data-quality-monitor-api
- baseURL: https://gateway.revefi.com/api/v1/
  baseurl_source: declared
  description: The Get Custom Data Quality Monitors API from Revefi — 1 operation(s) for get custom data quality monitors.
  name: Revefi Get Custom Data Quality Monitors API
  slug: revefi-get-custom-data-quality-monitors-api
- baseURL: https://gateway.revefi.com/api/v1/
  baseurl_source: declared
  description: The Get Custom Data Quality Monitors by Artifact API from Revefi — 1 operation(s) for get custom data quality monitors by artifact.
  name: Revefi Get Custom Data Quality Monitors by Artifact API
  slug: revefi-get-custom-data-quality-monitors-by-artifact-api
- baseURL: https://gateway.revefi.com/api/v1/
  baseurl_source: declared
  description: The Run Monitors API from Revefi — 1 operation(s) for run monitors.
  name: Revefi Run Monitors API
  slug: revefi-run-monitors-api
- baseURL: https://gateway.revefi.com/api/v1/
  baseurl_source: declared
  description: The Update an existing Custom Data Quality Monitor API from Revefi — 1 operation(s) for update an existing custom data quality monitor.
  name: Revefi Update an existing Custom Data Quality Monitor API
  slug: revefi-update-an-existing-custom-data-quality-monitor-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Data Quality Monitors Create a Custom Data Quality Monitor API
  slug: open-revefi-create-a-custom-data-quality-monitor-api
- collection_type: open
  name: Data Quality Monitors Create a Custom Data Quality Monitor Delete an existing Custom Data Quality Monitor API
  slug: open-revefi-delete-an-existing-custom-data-quality-monitor-api
- collection_type: open
  name: Data Quality Monitors Create a Custom Data Quality Monitor Get Custom Data Quality Monitors API
  slug: open-revefi-get-custom-data-quality-monitors-api
- collection_type: open
  name: Data Quality Monitors Create a Custom Data Quality Monitor Get Custom Data Quality Monitors by Artifact API
  slug: open-revefi-get-custom-data-quality-monitors-by-artifact-api
- collection_type: open
  name: Data Quality Monitors Create a Custom Data Quality Monitor Run Monitors API
  slug: open-revefi-run-monitors-api
- collection_type: open
  name: Data Quality Monitors Create a Custom Data Quality Monitor Update an existing Custom Data Quality Monitor API
  slug: open-revefi-update-an-existing-custom-data-quality-monitor-api
common:
- group: company
  title: ''
  type: Website
  url: https://revefi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.revefi.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.revefi.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.revefi.com/reference/getmonitors
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.revefi.com/docs/publicapis
- group: auth
  title: ''
  type: Authentication
  url: authentication/revefi-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revefi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revefi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revefi-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revefi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revefi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revefi-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/revefi-data-quality-monitors-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revefi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revefi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.revefi.com/docs/security-and-compliance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revefi-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.revefi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revefi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.revefi.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.revefi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.revefi.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revefi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.revefi.com/contact
created: '2026-07-17'
description: Revefi is an AI-powered data operations platform that delivers FinOps, observability, and optimization for modern data warehouses and AI/LLM workloads. Its zero-touch "data copilot" (Raden) autonomously monitors data quality, spend, performance, and usage across Snowflake, Databricks, BigQuery, and Redshift, extracting only metadata, query logs, and aggregated statistics (never PII). Revefi exposes a Public API for programmatically managing custom data quality monitors and a hosted Model Context Protocol (MCP) server so AI assistants can query metadata and operate on warehouse data. The company is SOC 2 Type II certified and HIPAA compliant, and is backed by Mayfield.
image: https://www.revefi.com/favicon.ico
layout: provider
mcp_servers:
- description: Revefi exposes a hosted Model Context Protocol (MCP) HTTP endpoint that lets MCP-compatible clients (Claude Code, Cursor, Claude Desktop, etc.) call Revefi tools to query metadata and operate on wareh
  name: Revefi MCP Server
  slug: revefi-mcp-server
modified: '2026-07-20'
name: Revefi
nav: Providers
network: true
overview: 'Revefi publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Create a Custom Data Quality Monitor API, Delete an existing Custom Data Quality Monitor API, Get Custom Data Quality Monitors API, and 3 more. Tagged areas include Data, Data Quality, Data Observability, FinOps, and Cost Optimization.


  Revefi''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 59.2
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 42.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revefi/refs/heads/main/screenshots/revefi-2026-08-17T081541.png
security:
- kind: authentication
  name: Revefi Authentication
  slug: revefi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Revefi Domain Security
  slug: revefi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revefi
tags:
- Data
- Data Quality
- Data Observability
- FinOps
- Cost Optimization
- Analytics
- Snowflake
- Databricks
- BigQuery
- Artificial Intelligence
- MCP
website: https://revefi.com
---
