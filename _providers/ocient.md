---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.3
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: The Ocient HTTP Query API executes SQL statements against an Ocient System over HTTPS and returns results as JSON. It runs on the SQL Nodes of an Ocient deployment behind an OpenAPI-enabled connectivi
  name: Ocient HTTP Query API
  slug: http-query-api
- description: Read-only REST endpoints exposed by Ocient System nodes for operational visibility. They return the software version, the running status of the node, per-node database statistics, the JSON configurati
  name: Ocient System Information REST Endpoints
  slug: system-information-rest-endpoints
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ocient-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ocient-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ocient.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ocient.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ocient.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ocient.com/ocient-http-query-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ocient.com/connect-to-ocient
- group: company
  title: ''
  type: Blog
  url: https://ocient.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://ocient.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ocient
- group: operate
  title: ''
  type: Support
  url: https://ocient.com/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://ocient.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ocient.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ocient.com/privacy-statement/
- group: auth
  title: ''
  type: Compliance
  url: https://ocient.com/security-and-compliance/
- group: docs
  title: ''
  type: SecurityGuide
  url: https://docs.ocient.com/ocient-security-guide
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ocient-http-query-api-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/ocient-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ocient-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ocient-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ocient-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ocient-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ocient-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/ocient-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ocient-lifecycle.yml
- group: design
  title: ''
  type: VersionCompatibility
  url: https://docs.ocient.com/version-compatibility
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ocient-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ocient-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ocient-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ocient-http-query-api-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ocient-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocient-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ocient-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ocient-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/ocient-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Ocient is a Chicago-based data platform company founded in 2016 that builds OcientAIQ, a unified data platform for petabyte-scale analytics and production AI. Its Compute-Adjacent Storage Architecture (CASA) colocates NVMe storage with compute so that ingest, query optimization, machine learning, geospatial analysis, security and governance run against very large datasets without moving the data. The platform is reached with standard SQL over a JDBC driver, the pyocient Python DB-API 2.0 driver, a SQLAlchemy dialect, an Apache Spark connector, and an HTTP Query API that executes SQL statements over REST and returns JSON. Ocient serves communications service providers, national security and intelligence, adtech, and financial services customers, and offers OcientCloud, customer-deployed, and hybrid deployment models.
image: https://ocient.com/wp-content/uploads/2024/03/logo_adjust-2r.png
layout: provider
mcp_servers:
- description: ''
  name: ocient-mcp.yml
  slug: ocient-mcpyml
modified: '2026-08-02'
name: Ocient
nav: Providers
network: true
overview: 'Ocient publishes 2 APIs on the [APIs.io](https://apis.io/) network: HTTP Query API and System Information REST Endpoints. Tagged areas include Company, Data, Analytics, Data Warehouse, and Database.


  Ocient''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, CLI, and 29 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 52.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 52.7
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Ocient Authentication
  slug: ocient-authentication
  summary_line: http/openIdConnect · 0 schemes
- kind: domain-security
  name: Ocient Domain Security
  slug: ocient-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ocient Trust Center
  slug: ocient-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: ocient
tags:
- Company
- Data
- Analytics
- Data Warehouse
- Database
- SQL
- Artificial Intelligence
- Machine Learning
- Big Data
- Geospatial
website: https://ocient.com/
---
