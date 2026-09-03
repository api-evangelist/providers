---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: 'POST-only JSON REST API exposed by every Kinetica deployment on port 9191. Endpoints cover SQL execution (/execute/sql), record ingest and egress (/insert/records/json, /get/records/json), schema and '
  name: Kinetica Database REST API
  slug: kinetica-database-rest-api
- description: Hosted Model Context Protocol server that gives any MCP-speaking agent a single endpoint onto a Kinetica database. Exposes toolbelt_* tools for SQL execution, vector search, knowledge-graph traversal,
  name: Kinetica Toolbelt MCP Server
  slug: kinetica-toolbelt-mcp-server
- description: Read-only Model Context Protocol server over the published Kinetica documentation site, advertised from https://docs.kinetica.com/.well-known/mcp.json with authentication none. Exposes search_kinetica
  name: Kinetica Docs MCP Server
  slug: kinetica-docs-mcp-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kinetica-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kinetica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kinetica.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kinetica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kinetica.com/7.2/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kinetica.com/7.2/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kinetica.com/7.2/guides/quickstart-guide/
- group: operate
  title: ''
  type: Support
  url: https://www.kinetica.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.kinetica.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kineticadb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kinetica.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.kinetica.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kinetica.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kinetica.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kinetica.com/7.2/release/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kinetica-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kinetica.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kinetica-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kinetica-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/kinetica-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kinetica-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/kinetica-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kinetica-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kinetica-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/kinetica-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kinetica-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kinetica-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kinetica-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kinetica-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kinetica-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/kinetica-cli.yml
- group: design
  title: ''
  type: Components
  url: components/kinetica-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kinetica-sandbox.yml
created: '2026-08-04'
description: Kinetica is a GPU-accelerated, real-time analytical database that unifies relational (SQL), vector, graph, geospatial, time-series and OLAP workloads in a single query engine, aimed at applications needing millisecond-latency analytics over continuously streaming data. Grown out of a GPU-accelerated geospatial and temporal engine built for U.S. Army Intelligence (INSCOM) in 2009, it is deployed today as the retrieval and reasoning layer behind AI agents and LLM-powered systems. The database is consumed through a POST-only JSON REST API (/execute/sql, /show/table, /insert/records/json, /filter/*, /aggregate/*, /match/graph and friends) served from each deployment on port 9191, plus first-party client libraries for Python, Java, C++, C#, JavaScript/Node.js and Go, JDBC/ODBC drivers, and the KiSQL command-line client. For agents, Kinetica publishes an A2A agent card and an installable Agent Skills package on its documentation host, and ships Toolbelt — an OAuth-protected hosted
  MCP server exposing toolbelt_* tools for SQL, vector search, graph traversal, schema introspection and ingest-job inspection.
image: https://kinetica-web-assets.s3.us-east-1.amazonaws.com/assets/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Kinetica MCP Server
  slug: kinetica-mcp-server
- description: ''
  name: Kinetica Docs
  slug: kinetica-docs
modified: '2026-08-04'
name: Kinetica
nav: Providers
network: true
overview: 'Kinetica publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Analytics, gpu-acceleration, Real-Time Analytics, and Vector Search.


  Kinetica''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 0
scopes:
- name: Kinetica Scopes
  scope_count: 2
  slug: kinetica-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 37.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kinetica/refs/heads/main/screenshots/kinetica-2026-08-07T171232.png
security:
- kind: authentication
  name: Kinetica Authentication
  slug: kinetica-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Kinetica Domain Security
  slug: kinetica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kinetica Vulnerability Disclosure
  slug: kinetica-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kinetica
tags:
- Database
- Analytics
- gpu-acceleration
- Real-Time Analytics
- Vector Search
- Graph Analytics
- Geospatial
- Time Series
- SQL
- Streaming
- Data Infrastructure
- MCP
- agent-native
- RAG
website: https://www.kinetica.com/
---
