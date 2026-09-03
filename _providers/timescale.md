---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 57
  human_in_the_loop: 5
  name: Timescale Agentic Access
  operation_count: 87
  slug: timescale-agentic-access
  summary_line: 87 operations · 57 acting · 5 human-in-the-loop
api_count: 2
apis:
- description: A publicly reachable, anonymous Model Context Protocol server (server name pg-aiguide) serving hybrid semantic + BM25 search over Tiger Cloud, TimescaleDB, PostgreSQL and PostGIS documentation, plus a
  name: Tiger Docs MCP Server
  slug: tiger-docs-mcp-server
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Analytics API from Timescale — 2 operation(s) for analytics.
  name: Timescale Analytics API
  slug: timescale-analytics-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Auth API from Timescale — 2 operation(s) for auth.
  name: Timescale Auth API
  slug: timescale-auth-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Feedback API from Timescale — 1 operation(s) for feedback.
  name: Timescale Feedback API
  slug: timescale-feedback-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Health API from Timescale — 1 operation(s) for health.
  name: Timescale Health API
  slug: timescale-health-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Invites API from Timescale — 3 operation(s) for invites.
  name: Timescale Invites API
  slug: timescale-invites-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Pricing API from Timescale — 1 operation(s) for pricing.
  name: Timescale Pricing API
  slug: timescale-pricing-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Projects API from Timescale — 1 operation(s) for projects.
  name: Timescale Projects API
  slug: timescale-projects-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Read Replica Sets API from Timescale — 6 operation(s) for read replica sets.
  name: Timescale Read Replica Sets API
  slug: timescale-read-replica-sets-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: Manage services, read replicas, and their associated actions.
  name: Timescale Services API
  slug: timescale-services-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Spaces API from Timescale — 31 operation(s) for spaces.
  name: Timescale Spaces API
  slug: timescale-spaces-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: Manage VPCs and their peering connections.
  name: Timescale VP Cs API
  slug: timescale-vpcs-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Timescale Analytics API
  slug: open-timescale-analytics-api
- collection_type: open
  name: Timescale Auth API
  slug: open-timescale-auth-api
- collection_type: open
  name: Ghost Feedback API
  slug: open-timescale-feedback-api
- collection_type: open
  name: Ghost Health API
  slug: open-timescale-health-api
- collection_type: open
  name: Ghost Invites API
  slug: open-timescale-invites-api
- collection_type: open
  name: Ghost Pricing API
  slug: open-timescale-pricing-api
- collection_type: open
  name: Tiger Cloud Projects API
  slug: open-timescale-projects-api
- collection_type: open
  name: Tiger Cloud Read Replica Sets API
  slug: open-timescale-read-replica-sets-api
- collection_type: open
  name: Tiger Cloud Services API
  slug: open-timescale-services-api
- collection_type: open
  name: Ghost Spaces API
  slug: open-timescale-spaces-api
- collection_type: open
  name: Tiger Cloud VP Cs API
  slug: open-timescale-vpcs-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/timescale-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/timescale-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/timescale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/timescale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/timescale-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tigerdata.com/security/vulnerability-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://www.tigerdata.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/timescale-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/timescale-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/timescale-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/timescale-vector/
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@timescaledb/typeorm
- group: build
  title: ''
  type: Ruby SDK
  url: https://rubygems.org/gems/timescaledb
- group: build
  title: ''
  type: CLI
  url: cli/timescale-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/timescale-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/timescale-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/timescale-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/timescale-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/timescale-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/timescale-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/timescale-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/timescale-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/timescale-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tigerdata.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/timescale-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.tigerdata.com/docs/get-started/news/new
- group: start
  title: ''
  type: Sandbox
  url: sandbox/timescale-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://console.cloud.tigerdata.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/timescale-tiger-cloud-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.tigerdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tigerdata.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.tigerdata.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.tigerdata.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tigerdata.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.tigerdata.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.tigerdata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/timescale
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tigerdata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.timescale.com/signup
- group: start
  title: ''
  type: Login
  url: https://console.cloud.timescale.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tigerdata.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tigerdata.com/legal/privacy
- group: operate
  title: ''
  type: SLA
  url: https://www.tigerdata.com/legal/service-level-agreement
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/timescale_stock/
created: '2026-08-05'
description: Timescale — rebranded as Tiger Data in 2025 — is the PostgreSQL data platform company behind TimescaleDB, the open-source PostgreSQL extension for time-series and real-time analytics, and Tiger Cloud, a fully managed PostgreSQL cloud service on AWS and Azure. The platform adds hypertables (automatic time-based partitioning), Hypercore hybrid row-columnar storage, native columnar compression, continuous aggregates, tiered storage to S3, database forks, read replica sets and connection pooling on top of standard PostgreSQL. The company also ships pg_textsearch (BM25 full-text search in Postgres), pgvectorscale and pgai for vector and AI workloads, the Tiger Cloud REST API for programmatic service management, the Tiger CLI with a built-in MCP server, and Ghost, an agent-oriented Postgres provisioning service at ghost.build.
image: https://www.tigerdata.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Timescale MCP Server
  slug: timescale-mcp-server
modified: '2026-08-05'
name: Timescale
nav: Providers
network: true
overview: 'Timescale publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Feedback API, and 8 more. Tagged areas include Company, Database, PostgreSQL, Time Series, and Analytics.


  Timescale''s developer surface includes authentication, CLI, changelog, release notes, sandbox, developer console, documentation, and 38 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 51.1
    developer_ergonomics: 82.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/screenshots/timescale-2026-08-17T082356.png
security:
- kind: authentication
  name: Timescale Authentication
  slug: timescale-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Timescale Domain Security
  slug: timescale-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Timescale Vulnerability Disclosure
  slug: timescale-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Timescale Trust Center
  slug: timescale-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: timescale
tags:
- Company
- Database
- PostgreSQL
- Time Series
- Analytics
- Cloud Infrastructure
- Data Platform
- Vector Search
- Developer Tools
- Open-Source
website: https://www.tigerdata.com/
---
