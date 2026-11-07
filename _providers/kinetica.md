---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-11-06'
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
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/kinetica/plans/kinetica-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kinetica-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/kinetica/security/kinetica-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kinetica-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/kinetica/security/kinetica-domain-security.yml
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
  href: https://artifacts.apis.io/kinetica/changelog/kinetica-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kinetica-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.kinetica.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/kinetica/well-known/kinetica-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kinetica-security.txt
- group: agent
  href: https://artifacts.apis.io/kinetica/well-known/kinetica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kinetica-well-known.yml
- group: other
  href: https://artifacts.apis.io/kinetica/a2a/kinetica-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kinetica-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kinetica/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kinetica/mcp/kinetica-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kinetica-mcp.yml
- group: build
  href: https://artifacts.apis.io/kinetica/packages/kinetica-packages.yml
  title: ''
  type: Packages
  url: packages/kinetica-packages.yml
- group: build
  href: https://artifacts.apis.io/kinetica/packages/kinetica-packages.yml
  title: ''
  type: SDKs
  url: packages/kinetica-packages.yml
- group: agent
  href: https://artifacts.apis.io/kinetica/llms/kinetica-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kinetica-llms.txt
- group: auth
  href: https://artifacts.apis.io/kinetica/authentication/kinetica-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kinetica-authentication.yml
- group: auth
  href: https://artifacts.apis.io/kinetica/scopes/kinetica-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/kinetica-scopes.yml
- group: design
  href: https://artifacts.apis.io/kinetica/conventions/kinetica-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kinetica-conventions.yml
- group: design
  href: https://artifacts.apis.io/kinetica/errors/kinetica-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/kinetica-error-codes.yml
- group: design
  href: https://artifacts.apis.io/kinetica/lifecycle/kinetica-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kinetica-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kinetica/conformance/kinetica-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kinetica-conformance.yml
- group: build
  href: https://artifacts.apis.io/kinetica/cli/kinetica-cli.yml
  title: ''
  type: CLI
  url: cli/kinetica-cli.yml
- group: design
  href: https://artifacts.apis.io/kinetica/components/kinetica-components.yml
  title: ''
  type: Components
  url: components/kinetica-components.yml
- group: start
  href: https://artifacts.apis.io/kinetica/sandbox/kinetica-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kinetica-sandbox.yml
created: '2026-08-04'
description: Kinetica is a GPU-accelerated, real-time analytical database that unifies relational (SQL), vector, graph, geospatial, time-series and OLAP workloads in a single query engine, aimed at applications needing millisecond-latency analytics over continuously streaming data. Grown out of a GPU-accelerated geospatial and temporal engine built for U.S. Army Intelligence (INSCOM) in 2009, it is deployed today as the retrieval and reasoning layer behind AI agents and LLM-powered systems. The database is consumed through a POST-only JSON REST API (/execute/sql, /show/table, /insert/records/json, /filter/*, /aggregate/*, /match/graph and friends) served from each deployment on port 9191, plus first-party client libraries for Python, Java, C++, C#, JavaScript/Node.js and Go, JDBC/ODBC drivers, and the KiSQL command-line client. For agents, Kinetica publishes an A2A agent card and an installable Agent Skills package on its documentation host, and ships Toolbelt — an OAuth-protected hosted
  MCP server exposing toolbelt_* tools for SQL, vector search, graph traversal, schema introspection and ingest-job inspection.
finops:
- has_sources: true
  method: derived
  name: Kinetica Finops
  primary_unit: hour
  service_category: ''
  slug: kinetica-finops
  template: false
image: https://kinetica-web-assets.s3.us-east-1.amazonaws.com/assets/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.toolbelt.ai over HTTP; 5 tools listed.
  name: Kinetica MCP Server
  slug: toolbelt
- description: Remote MCP server at kinetica.main-kill-isr.mintlify.me over HTTP; 3 tools listed.
  name: Kinetica Docs
  slug: kinetica-docs
modified: '2026-08-04'
name: Kinetica
nav: Providers
network: true
overview: 'Kinetica is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Database, Analytics, gpu-acceleration, Real-Time Analytics, and Vector Search.


  Kinetica''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Kinetica Plans Pricing
  plan_count: 3
  slug: kinetica-plans-pricing
random_paper: 0
scopes:
- name: Kinetica Scopes
  scope_count: 2
  slug: kinetica-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 55.0
    catalog_earned_first_party: 12.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 80.0
    operational_transparency: 28.9
  previous_composite: 49.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kinetica/kinetica-2026-08-07T171232.png
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
skill_count: 1
skills:
- name: Kinetica
  slug: kinetica-kinetica
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
- Agent-Native
- RAG
- A2A
website: https://www.kinetica.com/
---
